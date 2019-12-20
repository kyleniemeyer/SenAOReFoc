from PySide2.QtCore import QThread, QObject, Signal, Slot
from PySide2.QtWidgets import QApplication

import logging
import sys
import os
import argparse
import time
import h5py
import PIL.Image
import numpy as np

import log
from config import config
from HDF5_dset import make_dset, dset_append
from image_acquisition import acq_image
from centroid_acquisition import acq_centroid
from spot_sim import SpotSim

logger = log.get_logger(__name__)

class AO_Zernikes(QObject):
    """
    Runs closed-loop AO using calibrated zernike control matrix
    """
    start = Signal()
    write = Signal()
    done = Signal()
    error = Signal(object)
    image = Signal(object)
    message = Signal(object)
    info = Signal(object)

    def __init__(self, sensor, mirror, settings):

        # Get search block settings
        self.SB_settings = settings['SB_info']

        # Get mirror settings
        self.mirror_settings = settings['mirror_info']

        # Get AO settings
        self.AO_settings = settings['AO_info']

        # Get sensor instance
        self.sensor = sensor

        # Get mirror instance
        self.mirror = mirror

        # Initialise AO information parameter
        self.AO_info = {}

        # Initialise zernike coefficient array
        self.zern_coeff = np.zeros([config['AO']['control_coeff_num'], 1])
        
        # Initialise array to record root mean square error after each iteration
        self.loop_rms = np.zeros(config['AO']['loop_max'])

        super().__init__()

    @Slot(object)
    def run1(self):
        try:
            # Set process flags
            self.loop = True 
            self.log = True

            # Start thread
            self.start.emit()

            """
            Normal closed-loop AO process WITH A FIXED GAIN, iterated until residual phase error is below value given by Marechel 
            criterion or iteration has reached maximum
            """   
            # Get pseudo-inverse of slope - zernike conversion matrix to translate zernike coefficients into slopes           
            conv_matrix_inv = np.linalg.pinv(self.mirror_settings['conv_matrix'])
        
            # Open HDF5 file and create new dataset to store closed-loop AO data
            data_set_img = np.zeros([self.SB_settings['sensor_width'], self.SB_settings['sensor_height']])
            data_set_cent = np.zeros(self.SB_settings['act_ref_cent_num'])
            data_set_slope = np.zeros([self.SB_settings['act_ref_cent_num'] * 2, 1])
            data_set_zern = np.zeros([config['AO']['control_coeff_num'], 1])
            data_file = h5py.File('data_info.h5', 'a')
            grp1 = data_file['AO_img']
            grp2 = data_file['AO_info']
            data_set_1 = grp1.create_group('zern_AO_1')
            data_set_2 = grp2.create_group('zern_AO_1')
            key_list_1 = ['dummy_AO_img', 'dummy_spot_slope_x', 'dummy_spot_slope_y', 'dummy_spot_slope', 'dummy_spot_zern_err']
            key_list_2 = ['real_AO_img', 'real_spot_slope_x', 'real_spot_slope_y', 'real_spot_slope', 'real_spot_zern_err']

            if config['dummy']:
                for k in key_list_1:
                    if k in data_set_1:
                        del data_set_1[k]
                    elif k in data_set_2:
                        del data_set_2[k]
                    if k == 'dummy_AO_img':
                        make_dset(data_set_1, k, data_set_img)
                    elif k in {'dummy_spot_slope_x', 'dummy_spot_slope_y'}:
                        make_dset(data_set_2, k, data_set_cent)
                    elif k in {'dummy_spot_slope'}:
                        make_dset(data_set_2, k, data_set_slope)
                    elif k in {'dummy_spot_zern_err'}:
                        make_dset(data_set_2, k, data_set_zern)
            else:
                for k in key_list_2:
                    if k in data_set_1:
                        del data_set_1[k]
                    elif k in data_set_2:
                        del data_set_2[k]
                    if k == 'real_AO_img':
                        make_dset(data_set_1, k, data_set_img)
                    elif k in {'real_spot_slope_x', 'real_spot_slope_y'}:
                        make_dset(data_set_2, k, data_set_cent)
                    elif k in {'real_spot_slope'}:
                        make_dset(data_set_2, k, data_set_slope)
                    elif k in {'real_spot_zern_err'}:
                        make_dset(data_set_2, k, data_set_zern)

            self.message.emit('Process started for closed-loop AO via Zernikes...')

            # Initialise deformable mirror voltage array
            voltages = np.zeros(config['DM']['actuator_num'])

            prev1 = time.perf_counter()

            # Run closed-loop control until residual phase error is below a certain value or iteration has reached specified maximum
            for i in range(config['AO']['loop_max']):
                
                if self.loop:

                    try:
                        if config['dummy']:

                            pass
                        else:

                            # Update mirror control voltages
                            if i == 0:
                                voltages = config['DM']['vol_bias']
                            else:
                                voltages -= config['AO']['loop_gain'] * np.dot(self.mirror_settings['control_matrix_zern'], zern_err)                        

                            # Send values vector to mirror
                            self.mirror.Send(voltages)
                            
                            # Wait for DM to settle
                            time.sleep(config['DM']['settling_time'])
                        
                            # Acquire S-H spots using camera and append to list
                            AO_image = acq_image(self.sensor, self.SB_settings['sensor_width'], self.SB_settings['sensor_height'], acq_mode = 0)
                            dset_append(data_set_1, 'real_AO_img', AO_image)

                        # Image thresholding to remove background
                        AO_image = AO_image - config['image']['threshold'] * np.amax(AO_image)
                        AO_image[AO_image < 0] = 0
                        self.image.emit(AO_image)

                        # Calculate centroids of S-H spots
                        act_cent_coord, act_cent_coord_x, act_cent_coord_y, slope_x, slope_y = acq_centroid(self.SB_settings, flag = 3)
                        act_cent_coord, act_cent_coord_x, act_cent_coord_y = map(np.asarray, [act_cent_coord, act_cent_coord_x, act_cent_coord_y])

                        # Draw actual S-H spot centroids on image layer
                        AO_image.ravel()[act_cent_coord.astype(int)] = 0
                        self.image.emit(AO_image)

                        # Concatenate slopes into one slope matrix
                        slope = (np.concatenate((slope_x, slope_y), axis = 1)).T

                        # Get detected zernike coefficients from slope matrix
                        self.zern_coeff_detect = np.dot(self.mirror_settings['conv_matrix'], slope)

                        # Get phase residual (zernike coefficient residual error) and calculate root mean square (rms) error
                        zern_err = self.zern_coeff_detect.copy()
                        rms = np.sqrt((zern_err ** 2).mean(axis = 0))[0]
                        self.loop_rms[i] = rms

                        print('Root mean square error {} is {}'.format(i + 1, rms))                        

                        # Append data to list
                        if config['dummy']:
                            dset_append(data_set_2, 'dummy_spot_slope_x', slope_x)
                            dset_append(data_set_2, 'dummy_spot_slope_y', slope_y)
                            dset_append(data_set_2, 'dummy_spot_slope', slope)
                            dset_append(data_set_2, 'dummy_spot_zern_err', zern_err)
                        else:
                            dset_append(data_set_2, 'real_spot_slope_x', slope_x)
                            dset_append(data_set_2, 'real_spot_slope_y', slope_y)
                            dset_append(data_set_2, 'real_spot_slope', slope)
                            dset_append(data_set_2, 'real_spot_zern_err', zern_err)

                        # Compare rms error with tolerance factor (Marechel criterion) and decide whether to break from loop
                        if rms <= config['AO']['tolerance_fact_zern']:
                            break                 

                    except Exception as e:
                        print(e)
                else:

                    self.done.emit()

            # Close HDF5 file
            data_file.close()

            self.message.emit('Process complete.')
            print('Final root mean square error of detected wavefront is: {} microns'.format(rms))

            prev2 = time.perf_counter()
            print('Time for closed-loop AO process is:', (prev2 - prev1))

            """
            Returns closed-loop AO information into self.AO_info
            """             
            if self.log:

                self.AO_info['zern_AO_1']['loop_num'] = i
                self.AO_info['zern_AO_1']['residual_phase_err_1'] = self.loop_rms

                self.info.emit(self.AO_info)
                self.write.emit()
            else:

                self.done.emit()

            # Finished closed-loop AO process
            self.done.emit()

        except Exception as e:
            raise
            self.error.emit(e)

    @Slot(object)
    def run2(self):
        try:
            # Set process flags
            self.loop = True 
            self.log = True

            # Start thread
            self.start.emit()

            """
            Closed-loop AO process to handle obscured S-H spots using a FIXED GAIN, iterated until residual phase error is below value 
            given by Marechel criterion or iteration has reached maximum
            """   
            # Get pseudo-inverse of slope - zernike conversion matrix to translate zernike coefficients into slopes           
            conv_matrix_inv = np.linalg.pinv(self.mirror_settings['conv_matrix'])
        
            # Open HDF5 file and create new dataset to store closed-loop AO data
            data_set_img = np.zeros([self.SB_settings['sensor_width'], self.SB_settings['sensor_height']])
            data_set_cent = np.zeros(self.SB_settings['act_ref_cent_num'])
            data_set_slope = np.zeros([self.SB_settings['act_ref_cent_num'] * 2, 1])
            data_set_zern = np.zeros([config['AO']['control_coeff_num'], 1])
            data_file = h5py.File('data_info.h5', 'a')
            grp1 = data_file['AO_img']
            grp2 = data_file['AO_info']
            data_set_1 = grp1.create_group('zern_AO_2')
            data_set_2 = grp2.create_group('zern_AO_2')
            key_list_1 = ['dummy_AO_img', 'dummy_spot_slope_x', 'dummy_spot_slope_y', 'dummy_spot_slope', 'dummy_spot_zern_err']
            key_list_2 = ['real_AO_img', 'real_spot_slope_x', 'real_spot_slope_y', 'real_spot_slope', 'real_spot_zern_err']

            if config['dummy']:
                for k in key_list_1:
                    if k in data_set_1:
                        del data_set_1[k]
                    elif k in data_set_2:
                        del data_set_2[k]
                    if k == 'dummy_AO_img':
                        make_dset(data_set_1, k, data_set_img)
                    elif k in {'dummy_spot_slope_x', 'dummy_spot_slope_y'}:
                        make_dset(data_set_2, k, data_set_cent)
                    elif k in {'dummy_spot_slope'}:
                        make_dset(data_set_2, k, data_set_slope)
                    elif k in {'dummy_spot_zern_err'}:
                        make_dset(data_set_2, k, data_set_zern)
            else:
                for k in key_list_2:
                    if k in data_set_1:
                        del data_set_1[k]
                    elif k in data_set_2:
                        del data_set_2[k]
                    if k == 'real_AO_img':
                        make_dset(data_set_1, k, data_set_img)
                    elif k in {'real_spot_slope_x', 'real_spot_slope_y'}:
                        make_dset(data_set_2, k, data_set_cent)
                    elif k in {'real_spot_slope'}:
                        make_dset(data_set_2, k, data_set_slope)
                    elif k in {'real_spot_zern_err'}:
                        make_dset(data_set_2, k, data_set_zern)

            self.message.emit('Process started for closed-loop AO via Zernikes with obscured subapertures...')

            # Initialise deformable mirror voltage array
            voltages = np.zeros(config['DM']['actuator_num'])

            prev1 = time.perf_counter()

            # Run closed-loop control until residual phase error is below a certain value or iteration has reached specified maximum
            for i in range(config['AO']['loop_max']):
                
                if self.loop:

                    try:
                        if config['dummy']:

                            pass
                        else:

                            # Update mirror control voltages
                            if i == 0:
                                voltages = config['DM']['vol_bias']
                            else:
                                voltages -= config['AO']['loop_gain'] * np.dot(control_matrix_zern, zern_err)                        

                            # Send values vector to mirror
                            self.mirror.Send(voltages)
                            
                            # Wait for DM to settle
                            time.sleep(config['DM']['settling_time'])
                        
                            # Acquire S-H spots using camera and append to list
                            AO_image = acq_image(self.sensor, self.SB_settings['sensor_width'], self.SB_settings['sensor_height'], acq_mode = 0)
                            dset_append(data_set_1, 'real_AO_img', AO_image)

                        # Image thresholding to remove background
                        AO_image = AO_image - config['image']['threshold'] * np.amax(AO_image)
                        AO_image[AO_image < 0] = 0
                        self.image.emit(AO_image)

                        # Calculate centroids of S-H spots
                        act_cent_coord, act_cent_coord_x, act_cent_coord_y, slope_x, slope_y = acq_centroid(self.SB_settings, flag = 5)
                        act_cent_coord, act_cent_coord_x, act_cent_coord_y = map(np.asarray, [act_cent_coord, act_cent_coord_x, act_cent_coord_y])

                        # Remove corresponding elements from slopes and rows from influence function matrix, zernike matrix and zernike derivative matrix
                        index_remove = np.where(slope_x + self.mirror_settings['act_ref_cent_coord_x'] == 0)[0]
                        index_remove_inf = np.concatenate((index_remove, index_remove + self.SB_settings['act_ref_cent_num']), axis = None)
                        slope_x = np.argwhere(slope_x + self.mirror_settings['act_ref_cent_coord_x'])
                        slope_y = np.argwhere(slope_y + self.mirror_settings['act_ref_cent_coord_y'])
                        act_cent_coord = np.delete(act_cent_coord, index_remove, axis = None)
                        inf_matrix_slopes = np.delete(self.mirror_settings['inf_matrix_slopes'].copy(), index_remove_inf, axis = 0)
                        zern_matrix = np.delete(self.mirror_settings['zern_matrix'].copy(), index_remove_inf, axis = 0)
                        diff_matrix = np.delete(self.mirror_settings['diff_matrix'].copy(), index_remove_inf, axis = 0)

                        # print('The number of obscured subapertures is: {}'.format(len(index_remove)))
                        # print('The shapes of slope_x, slope_y, and inf_matrix_slopes are: {}, {}, and {}'.format(np.shape(slope_x), np.shape(slope_y),\
                        #     np.shape(inf_matrix_slopes)))

                        # Draw actual S-H spot centroids on image layer
                        AO_image.ravel()[act_cent_coord.astype(int)] = 0
                        self.image.emit(AO_image)

                        # Recalculate Cholesky decomposition of np.dot(zern_matrix.T, zern_matrix)
                        p_matrix = np.linalg.cholesky(np.dot(zern_matrix.T, zern_matrix))

                        # Recalculate conversion matrix
                        conv_matrix = np.dot(p_matrix, np.linalg.pinv(diff_matrix))

                        # Recalculate control function via zernikes
                        control_matrix_zern = np.linalg.pinv(np.dot(conv_matrix, inf_matrix_slopes))

                        # Concatenate slopes into one slope matrix
                        slope = (np.concatenate((slope_x, slope_y), axis = 1)).T

                        # Get detected zernike coefficients from slope matrix
                        self.zern_coeff_detect = np.dot(conv_matrix, slope)

                        # Get phase residual (zernike coefficient residual error) and calculate root mean square (rms) error
                        zern_err = self.zern_coeff_detect.copy()
                        rms = np.sqrt((zern_err ** 2).mean(axis = 0))[0]
                        self.loop_rms[i] = rms

                        print('Root mean square error {} is {}'.format(i + 1, rms))                        

                        # Append data to list
                        if config['dummy']:
                            dset_append(data_set_2, 'dummy_spot_slope_x', slope_x)
                            dset_append(data_set_2, 'dummy_spot_slope_y', slope_y)
                            dset_append(data_set_2, 'dummy_spot_slope', slope)
                            dset_append(data_set_2, 'dummy_spot_zern_err', zern_err)
                        else:
                            dset_append(data_set_2, 'real_spot_slope_x', slope_x)
                            dset_append(data_set_2, 'real_spot_slope_y', slope_y)
                            dset_append(data_set_2, 'real_spot_slope', slope)
                            dset_append(data_set_2, 'real_spot_zern_err', zern_err)

                        # Compare rms error with tolerance factor (Marechel criterion) and decide whether to break from loop
                        if rms <= config['AO']['tolerance_fact_zern']:
                            break                 

                    except Exception as e:
                        print(e)
                else:

                    self.done.emit()

            # Close HDF5 file
            data_file.close()

            self.message.emit('Process complete.')
            print('Final root mean square error of detected wavefront is: {} microns'.format(rms))

            prev2 = time.perf_counter()
            print('Time for closed-loop AO process is:', (prev2 - prev1))

            """
            Returns closed-loop AO information into self.AO_info
            """             
            if self.log:

                self.AO_info['zern_AO_2']['loop_num'] = i
                self.AO_info['zern_AO_2']['residual_phase_err_1'] = self.loop_rms

                self.info.emit(self.AO_info)
                self.write.emit()
            else:

                self.done.emit()

            # Finished closed-loop AO process
            self.done.emit()

        except Exception as e:
            raise
            self.error.emit(e)

     @Slot(object)
    def run3(self):
        try:
            # Set process flags
            self.loop = True 
            self.log = True

            # Start thread
            self.start.emit()

            """
            Closed-loop AO process to handle partial correction using a FIXED GAIN, iterated until residual phase error is below value 
            given by Marechel criterion or iteration has reached maximum            
            """   
            # Get pseudo-inverse of slope - zernike conversion matrix to translate zernike coefficients into slopes           
            conv_matrix_inv = np.linalg.pinv(self.mirror_settings['conv_matrix'])
        
            # Open HDF5 file and create new dataset to store closed-loop AO data
            data_set_img = np.zeros([self.SB_settings['sensor_width'], self.SB_settings['sensor_height']])
            data_set_cent = np.zeros(self.SB_settings['act_ref_cent_num'])
            data_set_slope = np.zeros([self.SB_settings['act_ref_cent_num'] * 2, 1])
            data_set_zern = np.zeros([config['AO']['control_coeff_num'], 1])
            data_file = h5py.File('data_info.h5', 'a')
            grp1 = data_file['AO_img']
            grp2 = data_file['AO_info']
            data_set_1 = grp1.create_group('zern_AO_3')
            data_set_2 = grp2.create_group('zern_AO_3')
            key_list_1 = ['dummy_AO_img', 'dummy_spot_slope_x', 'dummy_spot_slope_y', 'dummy_spot_slope', 'dummy_spot_zern_err']
            key_list_2 = ['real_AO_img', 'real_spot_slope_x', 'real_spot_slope_y', 'real_spot_slope', 'real_spot_zern_err']

            if config['dummy']:
                for k in key_list_1:
                    if k in data_set_1:
                        del data_set_1[k]
                    elif k in data_set_2:
                        del data_set_2[k]
                    if k == 'dummy_AO_img':
                        make_dset(data_set_1, k, data_set_img)
                    elif k in {'dummy_spot_slope_x', 'dummy_spot_slope_y'}:
                        make_dset(data_set_2, k, data_set_cent)
                    elif k in {'dummy_spot_slope'}:
                        make_dset(data_set_2, k, data_set_slope)
                    elif k in {'dummy_spot_zern_err'}:
                        make_dset(data_set_2, k, data_set_zern)
            else:
                for k in key_list_2:
                    if k in data_set_1:
                        del data_set_1[k]
                    elif k in data_set_2:
                        del data_set_2[k]
                    if k == 'real_AO_img':
                        make_dset(data_set_1, k, data_set_img)
                    elif k in {'real_spot_slope_x', 'real_spot_slope_y'}:
                        make_dset(data_set_2, k, data_set_cent)
                    elif k in {'real_spot_slope'}:
                        make_dset(data_set_2, k, data_set_slope)
                    elif k in {'real_spot_zern_err'}:
                        make_dset(data_set_2, k, data_set_zern)

            self.message.emit('Process started for closed-loop AO via Zernikes with partial correction...')

            # Initialise deformable mirror voltage array
            voltages = np.zeros(config['DM']['actuator_num'])

            prev1 = time.perf_counter()

            # Run closed-loop control until residual phase error is below a certain value or iteration has reached specified maximum
            for i in range(config['AO']['loop_max']):
                
                if self.loop:

                    try:
                        if config['dummy']:

                            pass
                        else:

                            # Update mirror control voltages
                            if i == 0:
                                voltages = config['DM']['vol_bias']
                            else:
                                zern_err[0 : 2, 0] = 0
                                voltages -= config['AO']['loop_gain'] * np.dot(self.mirror_settings['control_matrix_zern'], zern_err)                        

                            # Send values vector to mirror
                            self.mirror.Send(voltages)
                            
                            # Wait for DM to settle
                            time.sleep(config['DM']['settling_time'])
                        
                            # Acquire S-H spots using camera and append to list
                            AO_image = acq_image(self.sensor, self.SB_settings['sensor_width'], self.SB_settings['sensor_height'], acq_mode = 0)
                            dset_append(data_set_1, 'real_AO_img', AO_image)

                        # Image thresholding to remove background
                        AO_image = AO_image - config['image']['threshold'] * np.amax(AO_image)
                        AO_image[AO_image < 0] = 0
                        self.image.emit(AO_image)

                        # Calculate centroids of S-H spots
                        act_cent_coord, act_cent_coord_x, act_cent_coord_y, slope_x, slope_y = acq_centroid(self.SB_settings, flag = 7)
                        act_cent_coord, act_cent_coord_x, act_cent_coord_y = map(np.asarray, [act_cent_coord, act_cent_coord_x, act_cent_coord_y])

                        # Draw actual S-H spot centroids on image layer
                        AO_image.ravel()[act_cent_coord.astype(int)] = 0
                        self.image.emit(AO_image)

                        # Concatenate slopes into one slope matrix
                        slope = (np.concatenate((slope_x, slope_y), axis = 1)).T

                        # Get detected zernike coefficients from slope matrix
                        self.zern_coeff_detect = np.dot(self.mirror_settings['conv_matrix'], slope)

                        # Get phase residual (zernike coefficient residual error) and calculate root mean square (rms) error
                        zern_err = self.zern_coeff_detect.copy()
                        rms = np.sqrt((zern_err ** 2).mean(axis = 0))[0]
                        self.loop_rms[i] = rms

                        print('Root mean square error {} is {}'.format(i + 1, rms))                        

                        # Append data to list
                        if config['dummy']:
                            dset_append(data_set_2, 'dummy_spot_slope_x', slope_x)
                            dset_append(data_set_2, 'dummy_spot_slope_y', slope_y)
                            dset_append(data_set_2, 'dummy_spot_slope', slope)
                            dset_append(data_set_2, 'dummy_spot_zern_err', zern_err)
                        else:
                            dset_append(data_set_2, 'real_spot_slope_x', slope_x)
                            dset_append(data_set_2, 'real_spot_slope_y', slope_y)
                            dset_append(data_set_2, 'real_spot_slope', slope)
                            dset_append(data_set_2, 'real_spot_zern_err', zern_err)

                        # Compare rms error with tolerance factor (Marechel criterion) and decide whether to break from loop
                        if rms <= config['AO']['tolerance_fact_zern']:
                            break                 

                    except Exception as e:
                        print(e)
                else:

                    self.done.emit()

            # Close HDF5 file
            data_file.close()

            self.message.emit('Process complete.')
            print('Final root mean square error of detected wavefront is: {} microns'.format(rms))

            prev2 = time.perf_counter()
            print('Time for closed-loop AO process is:', (prev2 - prev1))

            """
            Returns closed-loop AO information into self.AO_info
            """             
            if self.log:

                self.AO_info['zern_AO_3']['loop_num'] = i
                self.AO_info['zern_AO_3']['residual_phase_err_1'] = self.loop_rms

                self.info.emit(self.AO_info)
                self.write.emit()
            else:

                self.done.emit()

            # Finished closed-loop AO process
            self.done.emit()

        except Exception as e:
            raise
            self.error.emit(e)

    @Slot(object)
    def run4(self):
        try:
            # Set process flags
            self.loop = True 
            self.log = True

            # Start thread
            self.start.emit()

            """
            Closed-loop AO process to handle both obscured S-H spots and partial correction using a FIXED GAIN, iterated until residual phase 
            error is below value given by Marechel criterion or iteration has reached maximum
            """   
            # Get pseudo-inverse of slope - zernike conversion matrix to translate zernike coefficients into slopes           
            conv_matrix_inv = np.linalg.pinv(self.mirror_settings['conv_matrix'])

            # Open HDF5 file and create new dataset to store closed-loop AO data
            data_set_img = np.zeros([self.SB_settings['sensor_width'], self.SB_settings['sensor_height']])
            data_set_cent = np.zeros(self.SB_settings['act_ref_cent_num'])
            data_set_slope = np.zeros([self.SB_settings['act_ref_cent_num'] * 2, 1])
            data_set_zern = np.zeros([config['AO']['control_coeff_num'], 1])
            data_file = h5py.File('data_info.h5', 'a')
            grp1 = data_file['AO_img']
            grp2 = data_file['AO_info']
            data_set_1 = grp1.create_group('zern_AO_4')
            data_set_2 = grp2.create_group('zern_AO_4')
            key_list_1 = ['dummy_AO_img', 'dummy_spot_slope_x', 'dummy_spot_slope_y', 'dummy_spot_slope', 'dummy_spot_zern_err']
            key_list_2 = ['real_AO_img', 'real_spot_slope_x', 'real_spot_slope_y', 'real_spot_slope', 'real_spot_zern_err']

            if config['dummy']:
                for k in key_list_1:
                    if k in data_set_1:
                        del data_set_1[k]
                    elif k in data_set_2:
                        del data_set_2[k]
                    if k == 'dummy_AO_img':
                        make_dset(data_set_1, k, data_set_img)
                    elif k in {'dummy_spot_slope_x', 'dummy_spot_slope_y'}:
                        make_dset(data_set_2, k, data_set_cent)
                    elif k in {'dummy_spot_slope'}:
                        make_dset(data_set_2, k, data_set_slope)
                    elif k in {'dummy_spot_zern_err'}:
                        make_dset(data_set_2, k, data_set_zern)
            else:
                for k in key_list_2:
                    if k in data_set_1:
                        del data_set_1[k]
                    elif k in data_set_2:
                        del data_set_2[k]
                    if k == 'real_AO_img':
                        make_dset(data_set_1, k, data_set_img)
                    elif k in {'real_spot_slope_x', 'real_spot_slope_y'}:
                        make_dset(data_set_2, k, data_set_cent)
                    elif k in {'real_spot_slope'}:
                        make_dset(data_set_2, k, data_set_slope)
                    elif k in {'real_spot_zern_err'}:
                        make_dset(data_set_2, k, data_set_zern)

            self.message.emit('Process started for full closed-loop AO via Zernikes...')

            # Initialise deformable mirror voltage array
            voltages = np.zeros(config['DM']['actuator_num'])

            prev1 = time.perf_counter()

            # Run closed-loop control until residual phase error is below a certain value or iteration has reached specified maximum
            for i in range(config['AO']['loop_max']):
                
                if self.loop:

                    try:
                        if config['dummy']:

                            pass
                        else:

                            # Update mirror control voltages
                            if i == 0:
                                voltages = config['DM']['vol_bias']
                            else:
                                zern_err[0 : 2, 0] = 0
                                voltages -= config['AO']['loop_gain'] * np.dot(control_matrix_zern, zern_err)                        

                            # Send values vector to mirror
                            self.mirror.Send(voltages)
                            
                            # Wait for DM to settle
                            time.sleep(config['DM']['settling_time'])
                        
                            # Acquire S-H spots using camera and append to list
                            AO_image = acq_image(self.sensor, self.SB_settings['sensor_width'], self.SB_settings['sensor_height'], acq_mode = 0)
                            dset_append(data_set_1, 'real_AO_img', AO_image)

                        # Image thresholding to remove background
                        AO_image = AO_image - config['image']['threshold'] * np.amax(AO_image)
                        AO_image[AO_image < 0] = 0
                        self.image.emit(AO_image)

                        # Calculate centroids of S-H spots
                        act_cent_coord, act_cent_coord_x, act_cent_coord_y, slope_x, slope_y = acq_centroid(self.SB_settings, flag = 9)
                        act_cent_coord, act_cent_coord_x, act_cent_coord_y = map(np.asarray, [act_cent_coord, act_cent_coord_x, act_cent_coord_y])

                        # Remove corresponding elements from slopes and rows from influence function matrix, zernike matrix and zernike derivative matrix
                        index_remove = np.where(slope_x + self.mirror_settings['act_ref_cent_coord_x'] == 0)[0]
                        index_remove_inf = np.concatenate((index_remove, index_remove + self.SB_settings['act_ref_cent_num']), axis = None)
                        slope_x = np.argwhere(slope_x + self.mirror_settings['act_ref_cent_coord_x'])
                        slope_y = np.argwhere(slope_y + self.mirror_settings['act_ref_cent_coord_y'])
                        act_cent_coord = np.delete(act_cent_coord, index_remove, axis = None)
                        inf_matrix_slopes = np.delete(self.mirror_settings['inf_matrix_slopes'].copy(), index_remove_inf, axis = 0)
                        zern_matrix = np.delete(self.mirror_settings['zern_matrix'].copy(), index_remove_inf, axis = 0)
                        diff_matrix = np.delete(self.mirror_settings['diff_matrix'].copy(), index_remove_inf, axis = 0)

                        # print('The number of obscured subapertures is: {}'.format(len(index_remove)))
                        # print('The shapes of slope_x, slope_y, and inf_matrix_slopes are: {}, {}, and {}'.format(np.shape(slope_x), np.shape(slope_y),\
                        #     np.shape(inf_matrix_slopes)))

                        # Draw actual S-H spot centroids on image layer
                        AO_image.ravel()[act_cent_coord.astype(int)] = 0
                        self.image.emit(AO_image)

                        # Recalculate Cholesky decomposition of np.dot(zern_matrix.T, zern_matrix)
                        p_matrix = np.linalg.cholesky(np.dot(zern_matrix.T, zern_matrix))

                        # Recalculate conversion matrix
                        conv_matrix = np.dot(p_matrix, np.linalg.pinv(diff_matrix))

                        # Recalculate control function via zernikes
                        control_matrix_zern = np.linalg.pinv(np.dot(conv_matrix, inf_matrix_slopes))

                        # Concatenate slopes into one slope matrix
                        slope = (np.concatenate((slope_x, slope_y), axis = 1)).T

                        # Get detected zernike coefficients from slope matrix
                        self.zern_coeff_detect = np.dot(conv_matrix, slope)

                        # Get phase residual (zernike coefficient residual error) and calculate root mean square (rms) error
                        zern_err = self.zern_coeff_detect.copy()
                        rms = np.sqrt((zern_err ** 2).mean(axis = 0))[0]
                        self.loop_rms[i] = rms

                        print('Root mean square error {} is {}'.format(i + 1, rms))                        

                        # Append data to list
                        if config['dummy']:
                            dset_append(data_set_2, 'dummy_spot_slope_x', slope_x)
                            dset_append(data_set_2, 'dummy_spot_slope_y', slope_y)
                            dset_append(data_set_2, 'dummy_spot_slope', slope)
                            dset_append(data_set_2, 'dummy_spot_zern_err', zern_err)
                        else:
                            dset_append(data_set_2, 'real_spot_slope_x', slope_x)
                            dset_append(data_set_2, 'real_spot_slope_y', slope_y)
                            dset_append(data_set_2, 'real_spot_slope', slope)
                            dset_append(data_set_2, 'real_spot_zern_err', zern_err)

                        # Compare rms error with tolerance factor (Marechel criterion) and decide whether to break from loop
                        if rms <= config['AO']['tolerance_fact_zern']:
                            break                 

                    except Exception as e:
                        print(e)
                else:

                    self.done.emit()

            # Close HDF5 file
            data_file.close()

            self.message.emit('Process complete.')
            print('Final root mean square error of detected wavefront is: {} microns'.format(rms))

            prev2 = time.perf_counter()
            print('Time for closed-loop AO process is:', (prev2 - prev1))

            """
            Returns closed-loop AO information into self.AO_info
            """             
            if self.log:

                self.AO_info['zern_AO_4']['loop_num'] = i
                self.AO_info['zern_AO_4']['residual_phase_err_1'] = self.loop_rms

                self.info.emit(self.AO_info)
                self.write.emit()
            else:

                self.done.emit()

            # Finished closed-loop AO process
            self.done.emit()

        except Exception as e:
            raise
            self.error.emit(e)

    @Slot(object)
    def stop(self):
        self.loop = False
        self.log = False


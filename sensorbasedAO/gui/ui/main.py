# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Tue Aug 25 16:07:33 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1580, 1180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1580, 1180))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icons/AO.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.mainContentLayout = QtWidgets.QVBoxLayout()
        self.mainContentLayout.setObjectName("mainContentLayout")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.initialiseBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.initialiseBtn.sizePolicy().hasHeightForWidth())
        self.initialiseBtn.setSizePolicy(sizePolicy)
        self.initialiseBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.initialiseBtn.setFont(font)
        self.initialiseBtn.setCheckable(True)
        self.initialiseBtn.setObjectName("initialiseBtn")
        self.horizontalLayout_1.addWidget(self.initialiseBtn)
        self.positionBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.positionBtn.sizePolicy().hasHeightForWidth())
        self.positionBtn.setSizePolicy(sizePolicy)
        self.positionBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.positionBtn.setFont(font)
        self.positionBtn.setCheckable(True)
        self.positionBtn.setObjectName("positionBtn")
        self.horizontalLayout_1.addWidget(self.positionBtn)
        self.centroidBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.centroidBtn.sizePolicy().hasHeightForWidth())
        self.centroidBtn.setSizePolicy(sizePolicy)
        self.centroidBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.centroidBtn.setFont(font)
        self.centroidBtn.setCheckable(True)
        self.centroidBtn.setObjectName("centroidBtn")
        self.horizontalLayout_1.addWidget(self.centroidBtn)
        self.mainContentLayout.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.calibrateBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.calibrateBtn.sizePolicy().hasHeightForWidth())
        self.calibrateBtn.setSizePolicy(sizePolicy)
        self.calibrateBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.calibrateBtn.setFont(font)
        self.calibrateBtn.setCheckable(True)
        self.calibrateBtn.setObjectName("calibrateBtn")
        self.horizontalLayout_2.addWidget(self.calibrateBtn)
        self.conversionBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.conversionBtn.sizePolicy().hasHeightForWidth())
        self.conversionBtn.setSizePolicy(sizePolicy)
        self.conversionBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.conversionBtn.setFont(font)
        self.conversionBtn.setCheckable(True)
        self.conversionBtn.setObjectName("conversionBtn")
        self.horizontalLayout_2.addWidget(self.conversionBtn)
        self.calibrateBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.calibrateBtn_2.sizePolicy().hasHeightForWidth())
        self.calibrateBtn_2.setSizePolicy(sizePolicy)
        self.calibrateBtn_2.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.calibrateBtn_2.setFont(font)
        self.calibrateBtn_2.setCheckable(True)
        self.calibrateBtn_2.setObjectName("calibrateBtn_2")
        self.horizontalLayout_2.addWidget(self.calibrateBtn_2)
        self.mainContentLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ZernikeArrEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.ZernikeArrEdt.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeArrEdt.setFont(font)
        self.ZernikeArrEdt.setText("")
        self.ZernikeArrEdt.setObjectName("ZernikeArrEdt")
        self.gridLayout.addWidget(self.ZernikeArrEdt, 2, 0, 1, 1)
        self.ZernikeCoeffSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.ZernikeCoeffSpin.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeCoeffSpin.setFont(font)
        self.ZernikeCoeffSpin.setMinimum(1)
        self.ZernikeCoeffSpin.setMaximum(200)
        self.ZernikeCoeffSpin.setProperty("value", 1)
        self.ZernikeCoeffSpin.setDisplayIntegerBase(10)
        self.ZernikeCoeffSpin.setObjectName("ZernikeCoeffSpin")
        self.gridLayout.addWidget(self.ZernikeCoeffSpin, 1, 0, 1, 1)
        self.ZernikeLbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.ZernikeLbl.setFont(font)
        self.ZernikeLbl.setObjectName("ZernikeLbl")
        self.gridLayout.addWidget(self.ZernikeLbl, 0, 0, 1, 1)
        self.ZernikeOKBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ZernikeOKBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.ZernikeOKBtn.setCheckable(True)
        self.ZernikeOKBtn.setObjectName("ZernikeOKBtn")
        self.gridLayout.addWidget(self.ZernikeOKBtn, 2, 1, 1, 1)
        self.ZernikeValSpin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ZernikeValSpin.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeValSpin.setFont(font)
        self.ZernikeValSpin.setMinimum(-99.99)
        self.ZernikeValSpin.setSingleStep(0.05)
        self.ZernikeValSpin.setObjectName("ZernikeValSpin")
        self.gridLayout.addWidget(self.ZernikeValSpin, 1, 1, 1, 1)
        self.mainContentLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ZernikeAOBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.ZernikeAOBtn_3.sizePolicy().hasHeightForWidth())
        self.ZernikeAOBtn_3.setSizePolicy(sizePolicy)
        self.ZernikeAOBtn_3.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeAOBtn_3.setFont(font)
        self.ZernikeAOBtn_3.setCheckable(True)
        self.ZernikeAOBtn_3.setObjectName("ZernikeAOBtn_3")
        self.gridLayout_2.addWidget(self.ZernikeAOBtn_3, 2, 0, 1, 1)
        self.slopeAOBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.slopeAOBtn_3.sizePolicy().hasHeightForWidth())
        self.slopeAOBtn_3.setSizePolicy(sizePolicy)
        self.slopeAOBtn_3.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.slopeAOBtn_3.setFont(font)
        self.slopeAOBtn_3.setCheckable(True)
        self.slopeAOBtn_3.setObjectName("slopeAOBtn_3")
        self.gridLayout_2.addWidget(self.slopeAOBtn_3, 2, 1, 1, 1)
        self.ZernikeAOBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.ZernikeAOBtn_2.sizePolicy().hasHeightForWidth())
        self.ZernikeAOBtn_2.setSizePolicy(sizePolicy)
        self.ZernikeAOBtn_2.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeAOBtn_2.setFont(font)
        self.ZernikeAOBtn_2.setCheckable(True)
        self.ZernikeAOBtn_2.setObjectName("ZernikeAOBtn_2")
        self.gridLayout_2.addWidget(self.ZernikeAOBtn_2, 1, 0, 1, 1)
        self.slopeAOBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.slopeAOBtn_2.sizePolicy().hasHeightForWidth())
        self.slopeAOBtn_2.setSizePolicy(sizePolicy)
        self.slopeAOBtn_2.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.slopeAOBtn_2.setFont(font)
        self.slopeAOBtn_2.setCheckable(True)
        self.slopeAOBtn_2.setObjectName("slopeAOBtn_2")
        self.gridLayout_2.addWidget(self.slopeAOBtn_2, 1, 1, 1, 1)
        self.ZernikeAOBtn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.ZernikeAOBtn_1.sizePolicy().hasHeightForWidth())
        self.ZernikeAOBtn_1.setSizePolicy(sizePolicy)
        self.ZernikeAOBtn_1.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeAOBtn_1.setFont(font)
        self.ZernikeAOBtn_1.setCheckable(True)
        self.ZernikeAOBtn_1.setObjectName("ZernikeAOBtn_1")
        self.gridLayout_2.addWidget(self.ZernikeAOBtn_1, 0, 0, 1, 1)
        self.slopeAOBtn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.slopeAOBtn_1.sizePolicy().hasHeightForWidth())
        self.slopeAOBtn_1.setSizePolicy(sizePolicy)
        self.slopeAOBtn_1.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.slopeAOBtn_1.setFont(font)
        self.slopeAOBtn_1.setCheckable(True)
        self.slopeAOBtn_1.setObjectName("slopeAOBtn_1")
        self.gridLayout_2.addWidget(self.slopeAOBtn_1, 0, 1, 1, 1)
        self.ZernikeTestBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(130)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.ZernikeTestBtn.sizePolicy().hasHeightForWidth())
        self.ZernikeTestBtn.setSizePolicy(sizePolicy)
        self.ZernikeTestBtn.setMinimumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeTestBtn.setFont(font)
        self.ZernikeTestBtn.setCheckable(True)
        self.ZernikeTestBtn.setObjectName("ZernikeTestBtn")
        self.gridLayout_2.addWidget(self.ZernikeTestBtn, 2, 2, 1, 1)
        self.ZernikeFullBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(130)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.ZernikeFullBtn.sizePolicy().hasHeightForWidth())
        self.ZernikeFullBtn.setSizePolicy(sizePolicy)
        self.ZernikeFullBtn.setMinimumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeFullBtn.setFont(font)
        self.ZernikeFullBtn.setCheckable(True)
        self.ZernikeFullBtn.setObjectName("ZernikeFullBtn")
        self.gridLayout_2.addWidget(self.ZernikeFullBtn, 0, 2, 1, 1)
        self.slopeFullBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(130)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.slopeFullBtn.sizePolicy().hasHeightForWidth())
        self.slopeFullBtn.setSizePolicy(sizePolicy)
        self.slopeFullBtn.setMinimumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.slopeFullBtn.setFont(font)
        self.slopeFullBtn.setCheckable(True)
        self.slopeFullBtn.setObjectName("slopeFullBtn")
        self.gridLayout_2.addWidget(self.slopeFullBtn, 1, 2, 1, 1)
        self.mainContentLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imageAcqLbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageAcqLbl.sizePolicy().hasHeightForWidth())
        self.imageAcqLbl.setSizePolicy(sizePolicy)
        self.imageAcqLbl.setMinimumSize(QtCore.QSize(170, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.imageAcqLbl.setFont(font)
        self.imageAcqLbl.setObjectName("imageAcqLbl")
        self.horizontalLayout_4.addWidget(self.imageAcqLbl)
        self.liveAcqBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.liveAcqBtn.sizePolicy().hasHeightForWidth())
        self.liveAcqBtn.setSizePolicy(sizePolicy)
        self.liveAcqBtn.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.liveAcqBtn.setFont(font)
        self.liveAcqBtn.setCheckable(True)
        self.liveAcqBtn.setObjectName("liveAcqBtn")
        self.horizontalLayout_4.addWidget(self.liveAcqBtn)
        self.burstAcqBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.burstAcqBtn.sizePolicy().hasHeightForWidth())
        self.burstAcqBtn.setSizePolicy(sizePolicy)
        self.burstAcqBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.burstAcqBtn.setFont(font)
        self.burstAcqBtn.setCheckable(True)
        self.burstAcqBtn.setObjectName("burstAcqBtn")
        self.horizontalLayout_4.addWidget(self.burstAcqBtn)
        self.singleAcqBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.singleAcqBtn.sizePolicy().hasHeightForWidth())
        self.singleAcqBtn.setSizePolicy(sizePolicy)
        self.singleAcqBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.singleAcqBtn.setFont(font)
        self.singleAcqBtn.setCheckable(True)
        self.singleAcqBtn.setObjectName("singleAcqBtn")
        self.horizontalLayout_4.addWidget(self.singleAcqBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.mainContentLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.deviceRstLbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceRstLbl.sizePolicy().hasHeightForWidth())
        self.deviceRstLbl.setSizePolicy(sizePolicy)
        self.deviceRstLbl.setMinimumSize(QtCore.QSize(170, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deviceRstLbl.setFont(font)
        self.deviceRstLbl.setObjectName("deviceRstLbl")
        self.horizontalLayout_5.addWidget(self.deviceRstLbl)
        self.DMRstBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.DMRstBtn.sizePolicy().hasHeightForWidth())
        self.DMRstBtn.setSizePolicy(sizePolicy)
        self.DMRstBtn.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DMRstBtn.setFont(font)
        self.DMRstBtn.setCheckable(True)
        self.DMRstBtn.setObjectName("DMRstBtn")
        self.horizontalLayout_5.addWidget(self.DMRstBtn)
        self.scannerRstBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.scannerRstBtn.sizePolicy().hasHeightForWidth())
        self.scannerRstBtn.setSizePolicy(sizePolicy)
        self.scannerRstBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scannerRstBtn.setFont(font)
        self.scannerRstBtn.setCheckable(True)
        self.scannerRstBtn.setObjectName("scannerRstBtn")
        self.horizontalLayout_5.addWidget(self.scannerRstBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.mainContentLayout.addLayout(self.horizontalLayout_5)
        self.remoteFocusLbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remoteFocusLbl.sizePolicy().hasHeightForWidth())
        self.remoteFocusLbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.remoteFocusLbl.setFont(font)
        self.remoteFocusLbl.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.remoteFocusLbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.remoteFocusLbl.setLineWidth(2)
        self.remoteFocusLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.remoteFocusLbl.setObjectName("remoteFocusLbl")
        self.mainContentLayout.addWidget(self.remoteFocusLbl)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scanFocusCheck = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanFocusCheck.sizePolicy().hasHeightForWidth())
        self.scanFocusCheck.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.scanFocusCheck.setFont(font)
        self.scanFocusCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scanFocusCheck.setObjectName("scanFocusCheck")
        self.verticalLayout_3.addWidget(self.scanFocusCheck)
        self.focusDepthLbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.focusDepthLbl.setFont(font)
        self.focusDepthLbl.setObjectName("focusDepthLbl")
        self.verticalLayout_3.addWidget(self.focusDepthLbl)
        self.focusDepthSpin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.focusDepthSpin.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.focusDepthSpin.setFont(font)
        self.focusDepthSpin.setDecimals(2)
        self.focusDepthSpin.setMaximum(80.0)
        self.focusDepthSpin.setSingleStep(0.5)
        self.focusDepthSpin.setObjectName("focusDepthSpin")
        self.verticalLayout_3.addWidget(self.focusDepthSpin)
        self.stepIncreLbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepIncreLbl.setFont(font)
        self.stepIncreLbl.setObjectName("stepIncreLbl")
        self.verticalLayout_3.addWidget(self.stepIncreLbl)
        self.stepIncreSpin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.stepIncreSpin.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepIncreSpin.setFont(font)
        self.stepIncreSpin.setDecimals(2)
        self.stepIncreSpin.setMaximum(80.0)
        self.stepIncreSpin.setSingleStep(0.5)
        self.stepIncreSpin.setObjectName("stepIncreSpin")
        self.verticalLayout_3.addWidget(self.stepIncreSpin)
        self.stepNumLbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepNumLbl.setFont(font)
        self.stepNumLbl.setObjectName("stepNumLbl")
        self.verticalLayout_3.addWidget(self.stepNumLbl)
        self.stepNumSpin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.stepNumSpin.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepNumSpin.setFont(font)
        self.stepNumSpin.setDecimals(0)
        self.stepNumSpin.setMaximum(80.0)
        self.stepNumSpin.setObjectName("stepNumSpin")
        self.verticalLayout_3.addWidget(self.stepNumSpin)
        self.startDepthLbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startDepthLbl.setFont(font)
        self.startDepthLbl.setObjectName("startDepthLbl")
        self.verticalLayout_3.addWidget(self.startDepthLbl)
        self.startDepthSpin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.startDepthSpin.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startDepthSpin.setFont(font)
        self.startDepthSpin.setDecimals(2)
        self.startDepthSpin.setMaximum(80.0)
        self.startDepthSpin.setSingleStep(0.5)
        self.startDepthSpin.setObjectName("startDepthSpin")
        self.verticalLayout_3.addWidget(self.startDepthSpin)
        self.pauseTimeLbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pauseTimeLbl.setFont(font)
        self.pauseTimeLbl.setObjectName("pauseTimeLbl")
        self.verticalLayout_3.addWidget(self.pauseTimeLbl)
        self.pauseTimeSpin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pauseTimeSpin.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pauseTimeSpin.setFont(font)
        self.pauseTimeSpin.setObjectName("pauseTimeSpin")
        self.verticalLayout_3.addWidget(self.pauseTimeSpin)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.AOTypeLbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AOTypeLbl.sizePolicy().hasHeightForWidth())
        self.AOTypeLbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AOTypeLbl.setFont(font)
        self.AOTypeLbl.setObjectName("AOTypeLbl")
        self.verticalLayout_5.addWidget(self.AOTypeLbl)
        self.AOTypeCombo = QtWidgets.QComboBox(self.centralwidget)
        self.AOTypeCombo.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AOTypeCombo.setFont(font)
        self.AOTypeCombo.setMouseTracking(True)
        self.AOTypeCombo.setEditable(False)
        self.AOTypeCombo.setObjectName("AOTypeCombo")
        self.AOTypeCombo.addItem("")
        self.AOTypeCombo.addItem("")
        self.AOTypeCombo.addItem("")
        self.AOTypeCombo.addItem("")
        self.AOTypeCombo.addItem("")
        self.verticalLayout_5.addWidget(self.AOTypeCombo)
        self.moveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.moveBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.moveBtn.setFont(font)
        self.moveBtn.setCheckable(True)
        self.moveBtn.setObjectName("moveBtn")
        self.verticalLayout_5.addWidget(self.moveBtn)
        self.scanBtn = QtWidgets.QPushButton(self.centralwidget)
        self.scanBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scanBtn.setFont(font)
        self.scanBtn.setCheckable(True)
        self.scanBtn.setObjectName("scanBtn")
        self.verticalLayout_5.addWidget(self.scanBtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.mainContentLayout.addLayout(self.horizontalLayout_3)
        self.MLDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MLDataBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MLDataBtn.setFont(font)
        self.MLDataBtn.setCheckable(True)
        self.MLDataBtn.setObjectName("MLDataBtn")
        self.mainContentLayout.addWidget(self.MLDataBtn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainContentLayout.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.displayBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayBox.sizePolicy().hasHeightForWidth())
        self.displayBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.displayBox.setFont(font)
        self.displayBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displayBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.displayBox.setLineWidth(2)
        self.displayBox.setCenterOnScroll(False)
        self.displayBox.setObjectName("displayBox")
        self.verticalLayout.addWidget(self.displayBox)
        self.mainContentLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)
        self.stopBtn.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.stopBtn.setFont(font)
        self.stopBtn.setObjectName("stopBtn")
        self.verticalLayout_2.addWidget(self.stopBtn)
        self.quitBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitBtn.sizePolicy().hasHeightForWidth())
        self.quitBtn.setSizePolicy(sizePolicy)
        self.quitBtn.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.quitBtn.setFont(font)
        self.quitBtn.setObjectName("quitBtn")
        self.verticalLayout_2.addWidget(self.quitBtn)
        self.mainContentLayout.addLayout(self.verticalLayout_2)
        self.mainLayout.addLayout(self.mainContentLayout)
        self.SHViewer = SHViewer(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SHViewer.sizePolicy().hasHeightForWidth())
        self.SHViewer.setSizePolicy(sizePolicy)
        self.SHViewer.setMinimumSize(QtCore.QSize(1046, 1046))
        self.SHViewer.setObjectName("SHViewer")
        self.mainLayout.addWidget(self.SHViewer)
        self.horizontalLayout.addLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "SensorbasedAO", None, -1))
        self.initialiseBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Initialise SB", None, -1))
        self.positionBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Position SB", None, -1))
        self.centroidBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Centroid Spots", None, -1))
        self.calibrateBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Calibrate-S", None, -1))
        self.conversionBtn.setText(QtWidgets.QApplication.translate("MainWindow", "S-Z Conv", None, -1))
        self.calibrateBtn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Calibrate-Z", None, -1))
        self.ZernikeArrEdt.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Separate coefficients with space", None, -1))
        self.ZernikeLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike coefficients (microns)", None, -1))
        self.ZernikeOKBtn.setText(QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))
        self.ZernikeAOBtn_3.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike AO 3", None, -1))
        self.slopeAOBtn_3.setText(QtWidgets.QApplication.translate("MainWindow", "Slope AO 3", None, -1))
        self.ZernikeAOBtn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike AO 2", None, -1))
        self.slopeAOBtn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Slope AO 2", None, -1))
        self.ZernikeAOBtn_1.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike AO 1", None, -1))
        self.slopeAOBtn_1.setText(QtWidgets.QApplication.translate("MainWindow", "Slope AO 1", None, -1))
        self.ZernikeTestBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike Test", None, -1))
        self.ZernikeFullBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike Full", None, -1))
        self.slopeFullBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Slope Full", None, -1))
        self.imageAcqLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Image Acquisition", None, -1))
        self.liveAcqBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Live Acq", None, -1))
        self.burstAcqBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Burst Acq", None, -1))
        self.singleAcqBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Single Acq", None, -1))
        self.deviceRstLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Device Reset", None, -1))
        self.DMRstBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Reset DM", None, -1))
        self.scannerRstBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Reset Scanner", None, -1))
        self.remoteFocusLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Remote Focusing Unit", None, -1))
        self.scanFocusCheck.setText(QtWidgets.QApplication.translate("MainWindow", "Scan Focus", None, -1))
        self.focusDepthLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Focus Depth (microns)", None, -1))
        self.stepIncreLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Step Increment (microns)", None, -1))
        self.stepNumLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Step Number", None, -1))
        self.startDepthLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Start Depth (microns)", None, -1))
        self.pauseTimeLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Depth Pause Time (s)", None, -1))
        self.AOTypeLbl.setText(QtWidgets.QApplication.translate("MainWindow", "AO Correction Type", None, -1))
        self.AOTypeCombo.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "None", None, -1))
        self.AOTypeCombo.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Zernike AO 3", None, -1))
        self.AOTypeCombo.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Zernike Full", None, -1))
        self.AOTypeCombo.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Slope AO 3", None, -1))
        self.AOTypeCombo.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "Slope Full", None, -1))
        self.moveBtn.setText(QtWidgets.QApplication.translate("MainWindow", "MOVE", None, -1))
        self.scanBtn.setText(QtWidgets.QApplication.translate("MainWindow", "SCAN", None, -1))
        self.MLDataBtn.setText(QtWidgets.QApplication.translate("MainWindow", "ML Dataset", None, -1))
        self.displayBox.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Sensorbased AO Software", None, -1))
        self.stopBtn.setText(QtWidgets.QApplication.translate("MainWindow", "STOP", None, -1))
        self.quitBtn.setText(QtWidgets.QApplication.translate("MainWindow", "QUIT", None, -1))

from sensorbasedAO.gui.SHViewer import SHViewer

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


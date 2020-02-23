# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Wed Dec 18 12:08:28 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 1000)  # 1080
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1360, 1000))  # 1080
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
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        self.ZernikeArrEdt.setText("")
        self.ZernikeArrEdt.setObjectName("ZernikeArrEdt")
        self.gridLayout.addWidget(self.ZernikeArrEdt, 2, 0, 1, 1)
        self.ZernikeCoeffSpin = QtWidgets.QSpinBox(self.centralwidget)
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
        self.ZernikeOKBtn.setCheckable(True)
        self.ZernikeOKBtn.setObjectName("ZernikeOKBtn")
        self.gridLayout.addWidget(self.ZernikeOKBtn, 2, 1, 1, 1)
        self.ZernikeValSpin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ZernikeValSpin.setMinimum(-99.99)
        self.ZernikeValSpin.setObjectName("ZernikeValSpin")
        self.gridLayout.addWidget(self.ZernikeValSpin, 1, 1, 1, 1)
        self.mainContentLayout.addLayout(self.gridLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ZernikeTestBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZernikeTestBtn.sizePolicy().hasHeightForWidth())
        self.ZernikeTestBtn.setSizePolicy(sizePolicy)
        self.ZernikeTestBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeTestBtn.setFont(font)
        self.ZernikeTestBtn.setCheckable(True)
        self.ZernikeTestBtn.setObjectName("ZernikeTestBtn")
        self.horizontalLayout_4.addWidget(self.ZernikeTestBtn)
        self.mainContentLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ZernikeAOBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZernikeAOBtn_3.sizePolicy().hasHeightForWidth())
        self.ZernikeAOBtn_3.setSizePolicy(sizePolicy)
        self.ZernikeAOBtn_3.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeAOBtn_3.setFont(font)
        self.ZernikeAOBtn_3.setCheckable(True)
        self.ZernikeAOBtn_3.setObjectName("ZernikeAOBtn_3")
        self.gridLayout_2.addWidget(self.ZernikeAOBtn_3, 0, 2, 1, 1)
        self.ZernikeAOBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZernikeAOBtn_2.sizePolicy().hasHeightForWidth())
        self.ZernikeAOBtn_2.setSizePolicy(sizePolicy)
        self.ZernikeAOBtn_2.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeAOBtn_2.setFont(font)
        self.ZernikeAOBtn_2.setCheckable(True)
        self.ZernikeAOBtn_2.setObjectName("ZernikeAOBtn_2")
        self.gridLayout_2.addWidget(self.ZernikeAOBtn_2, 0, 1, 1, 1)
        self.slopeAOBtn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slopeAOBtn_1.sizePolicy().hasHeightForWidth())
        self.slopeAOBtn_1.setSizePolicy(sizePolicy)
        self.slopeAOBtn_1.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.slopeAOBtn_1.setFont(font)
        self.slopeAOBtn_1.setCheckable(True)
        self.slopeAOBtn_1.setObjectName("slopeAOBtn_1")
        self.gridLayout_2.addWidget(self.slopeAOBtn_1, 1, 0, 1, 1)
        self.slopeAOBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slopeAOBtn_2.sizePolicy().hasHeightForWidth())
        self.slopeAOBtn_2.setSizePolicy(sizePolicy)
        self.slopeAOBtn_2.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.slopeAOBtn_2.setFont(font)
        self.slopeAOBtn_2.setCheckable(True)
        self.slopeAOBtn_2.setObjectName("slopeAOBtn_2")
        self.gridLayout_2.addWidget(self.slopeAOBtn_2, 1, 1, 1, 1)
        self.slopeAOBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slopeAOBtn_3.sizePolicy().hasHeightForWidth())
        self.slopeAOBtn_3.setSizePolicy(sizePolicy)
        self.slopeAOBtn_3.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.slopeAOBtn_3.setFont(font)
        self.slopeAOBtn_3.setCheckable(True)
        self.slopeAOBtn_3.setObjectName("slopeAOBtn_3")
        self.gridLayout_2.addWidget(self.slopeAOBtn_3, 1, 2, 1, 1)
        self.ZernikeAOBtn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZernikeAOBtn_1.sizePolicy().hasHeightForWidth())
        self.ZernikeAOBtn_1.setSizePolicy(sizePolicy)
        self.ZernikeAOBtn_1.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeAOBtn_1.setFont(font)
        self.ZernikeAOBtn_1.setCheckable(True)
        self.ZernikeAOBtn_1.setObjectName("ZernikeAOBtn_1")
        self.gridLayout_2.addWidget(self.ZernikeAOBtn_1, 0, 0, 1, 1)
        self.mainContentLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ZernikeFullBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZernikeFullBtn.sizePolicy().hasHeightForWidth())
        self.ZernikeFullBtn.setSizePolicy(sizePolicy)
        self.ZernikeFullBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZernikeFullBtn.setFont(font)
        self.ZernikeFullBtn.setCheckable(True)
        self.ZernikeFullBtn.setObjectName("ZernikeFullBtn")
        self.horizontalLayout_5.addWidget(self.ZernikeFullBtn)
        self.SlopeFullBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SlopeFullBtn.sizePolicy().hasHeightForWidth())
        self.SlopeFullBtn.setSizePolicy(sizePolicy)
        self.SlopeFullBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SlopeFullBtn.setFont(font)
        self.SlopeFullBtn.setCheckable(True)
        self.SlopeFullBtn.setObjectName("SlopeFullBtn")
        self.horizontalLayout_5.addWidget(self.SlopeFullBtn)
        self.mainContentLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainContentLayout.addItem(spacerItem)
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
        self.initialiseBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Initialise", None, -1))
        self.positionBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Position SB", None, -1))
        self.centroidBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Centroid", None, -1))
        self.calibrateBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Calibrate - S", None, -1))
        self.conversionBtn.setText(QtWidgets.QApplication.translate("MainWindow", "S-Z Conv", None, -1))
        self.calibrateBtn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Calibrate - Z", None, -1))
        self.ZernikeArrEdt.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Enter Zernike coefficients with \' \' in between", None, -1))
        self.ZernikeLbl.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike coefficients (microns)", None, -1))
        self.ZernikeOKBtn.setText(QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))
        self.ZernikeTestBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike Test", None, -1))
        self.ZernikeAOBtn_3.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike AO 3", None, -1))
        self.ZernikeAOBtn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike AO 2", None, -1))
        self.slopeAOBtn_1.setText(QtWidgets.QApplication.translate("MainWindow", "Slope AO 1", None, -1))
        self.slopeAOBtn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Slope AO 2", None, -1))
        self.slopeAOBtn_3.setText(QtWidgets.QApplication.translate("MainWindow", "Slope AO 3", None, -1))
        self.ZernikeAOBtn_1.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike AO 1", None, -1))
        self.ZernikeFullBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Zernike Full", None, -1))
        self.SlopeFullBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Slope Full", None, -1))
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


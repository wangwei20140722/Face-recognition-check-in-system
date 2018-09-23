# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
# 这段代码是 主要的ui界面  包含了八个按钮 七个lable 一个进度条
# 八个按钮对应想要的八个功能 一个lable是用来显示摄像头 画面 其余六个lable是用来显示找到的人的详细信息 最多显示三个人的  进度条是当加载人脸识别模块的时候粗略显示进度的

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap,QPainter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 741)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 741))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 741))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1224, 731))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 40)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(14, -1, -1, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_5.addWidget(self.progressBar)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(800, 494))
        self.label_5.setMaximumSize(QtCore.QSize(800, 494))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(200, 247))
        self.label_7.setMaximumSize(QtCore.QSize(200, 247))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 247))
        self.label_2.setMaximumSize(QtCore.QSize(200, 247))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(200, 247))
        self.label_6.setMaximumSize(QtCore.QSize(200, 247))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(200, 247))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        self.label_4.setMaximumSize(QtCore.QSize(200, 247))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(200, 247))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_8.setText(_translate("MainWindow", "打开摄像头1"))
        self.pushButton_6.setText(_translate("MainWindow", "打开摄像头2"))
        self.pushButton_7.setText(_translate("MainWindow", "打开摄像头3"))
        self.pushButton_5.setText(_translate("MainWindow", "拍照"))
        self.pushButton_9.setText(_translate("MainWindow", "语音播报"))
        self.pushButton_4.setText(_translate("MainWindow", "人脸识别"))
        self.pushButton_3.setText(_translate("MainWindow", "语音合成"))
        self.pushButton.setText(_translate("MainWindow", "录入信息"))
        self.pushButton_2.setText(_translate("MainWindow", "查看记录"))
        self.label_5.setText(_translate("MainWindow", ""))# 摄像头视频
        self.label_7.setText(_translate("MainWindow", ""))#图片1
        self.label_2.setText(_translate("MainWindow", ""))#信息1
        self.label_6.setText(_translate("MainWindow", ""))#图片2
        self.label.setText(_translate("MainWindow", ""))#信息2
        self.label_4.setText(_translate("MainWindow", ""))#图片3
        self.label_3.setText(_translate("MainWindow", ""))# 信息3

        self.setWindowTitle("人脸识别")# 设置标题
        self.setWindowIcon(QIcon('Amg.jpg'))#设置logo
        #self.progressBar.


   #把button的背景色给改了 改成暗蓝色  这部分稍后再添加上去
        self.pushButton.setStyleSheet('QPushButton {background-color: #b4b4b4}') ##b4b4b4 银色
        self.pushButton_2.setStyleSheet('QPushButton {background-color: #b4b4b4}')
        self.pushButton_3.setStyleSheet('QPushButton {background-color: #b4b4b4}')
        self.pushButton_4.setStyleSheet('QPushButton {background-color: #b4b4b4}')
        self.pushButton_5.setStyleSheet('QPushButton {background-color: #b4b4b4}')
        self.pushButton_6.setStyleSheet('QPushButton {background-color: #b4b4b4}')
        self.pushButton_7.setStyleSheet('QPushButton {background-color: #b4b4b4}')
        self.pushButton_8.setStyleSheet('QPushButton {background-color: #b4b4b4}')
        self.pushButton_9.setStyleSheet('QPushButton {background-color: #b4b4b4}')
    #   self.label_5.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(255, 0, 0);") #设置label边框
    def paintEvent(self,event):  #设置背景图
        painter = QPainter(self)
        pixmap = QPixmap("face3.jpg")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(),pixmap)

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python-Projects\Gandhar Calculator\ui\Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calculator(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(471, 506)
        mainWindow.setMinimumSize(QtCore.QSize(471, 506))
        mainWindow.setMaximumSize(QtCore.QSize(471, 506))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buttonframe = QtWidgets.QFrame(self.frame)
        self.buttonframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe.setObjectName("buttonframe")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.buttonframe)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.buttonframe)
        self.pushButton_5.setMinimumSize(QtCore.QSize(10, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pb0 = QtWidgets.QPushButton(self.buttonframe)
        self.pb0.setMinimumSize(QtCore.QSize(10, 50))
        self.pb0.setObjectName("pb0")
        self.gridLayout_2.addWidget(self.pb0, 3, 0, 1, 1)
        self.pb7 = QtWidgets.QPushButton(self.buttonframe)
        self.pb7.setMinimumSize(QtCore.QSize(10, 50))
        self.pb7.setObjectName("pb7")
        self.gridLayout_2.addWidget(self.pb7, 0, 0, 1, 1)
        self.pbd = QtWidgets.QPushButton(self.buttonframe)
        self.pbd.setMinimumSize(QtCore.QSize(10, 50))
        self.pbd.setObjectName("pbd")
        self.gridLayout_2.addWidget(self.pbd, 3, 3, 1, 1)
        self.pbmu = QtWidgets.QPushButton(self.buttonframe)
        self.pbmu.setMinimumSize(QtCore.QSize(10, 50))
        self.pbmu.setObjectName("pbmu")
        self.gridLayout_2.addWidget(self.pbmu, 2, 3, 1, 1)
        self.pb9 = QtWidgets.QPushButton(self.buttonframe)
        self.pb9.setMinimumSize(QtCore.QSize(10, 50))
        self.pb9.setObjectName("pb9")
        self.gridLayout_2.addWidget(self.pb9, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.buttonframe)
        self.pushButton_4.setMinimumSize(QtCore.QSize(10, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 2, 1, 1)
        self.pbp = QtWidgets.QPushButton(self.buttonframe)
        self.pbp.setMinimumSize(QtCore.QSize(10, 50))
        self.pbp.setObjectName("pbp")
        self.gridLayout_2.addWidget(self.pbp, 0, 3, 1, 1)
        self.pbm = QtWidgets.QPushButton(self.buttonframe)
        self.pbm.setMinimumSize(QtCore.QSize(10, 50))
        self.pbm.setObjectName("pbm")
        self.gridLayout_2.addWidget(self.pbm, 1, 3, 1, 1)
        self.pbe = QtWidgets.QPushButton(self.buttonframe)
        self.pbe.setMinimumSize(QtCore.QSize(10, 50))
        self.pbe.setObjectName("pbe")
        self.gridLayout_2.addWidget(self.pbe, 3, 2, 1, 1)
        self.pb8 = QtWidgets.QPushButton(self.buttonframe)
        self.pb8.setMinimumSize(QtCore.QSize(10, 50))
        self.pb8.setObjectName("pb8")
        self.gridLayout_2.addWidget(self.pb8, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.buttonframe)
        self.pushButton_7.setMinimumSize(QtCore.QSize(10, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.buttonframe)
        self.pushButton_9.setMinimumSize(QtCore.QSize(10, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.buttonframe)
        self.pushButton_6.setMinimumSize(QtCore.QSize(10, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.buttonframe)
        self.pushButton_8.setMinimumSize(QtCore.QSize(10, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pbdot = QtWidgets.QPushButton(self.buttonframe)
        self.pbdot.setMinimumSize(QtCore.QSize(10, 50))
        self.pbdot.setObjectName("pbdot")
        self.gridLayout_2.addWidget(self.pbdot, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.buttonframe, 1, 0, 1, 1)
        self.topframe = QtWidgets.QFrame(self.frame)
        self.topframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topframe.setObjectName("topframe")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.topframe)
        self.gridLayout_3.setContentsMargins(0, 0, -1, 0)
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(231, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.back = QtWidgets.QPushButton(self.topframe)
        self.back.setMinimumSize(QtCore.QSize(0, 50))
        self.back.setObjectName("back")
        self.gridLayout_3.addWidget(self.back, 0, 1, 1, 1)
        self.clear = QtWidgets.QPushButton(self.topframe)
        self.clear.setMinimumSize(QtCore.QSize(0, 50))
        self.clear.setObjectName("clear")
        self.gridLayout_3.addWidget(self.clear, 0, 2, 1, 1)
        self.screen = QtWidgets.QLineEdit(self.topframe)
        self.screen.setMinimumSize(QtCore.QSize(0, 60))
        self.screen.setObjectName("screen")
        self.gridLayout_3.addWidget(self.screen, 1, 0, 1, 3)
        self.gridLayout_4.addWidget(self.topframe, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Gandhar Calculator"))
        self.pushButton_5.setText(_translate("mainWindow", "1"))
        self.pb0.setText(_translate("mainWindow", "0"))
        self.pb7.setText(_translate("mainWindow", "7"))
        self.pbd.setText(_translate("mainWindow", "/"))
        self.pbmu.setText(_translate("mainWindow", "*"))
        self.pb9.setText(_translate("mainWindow", "9"))
        self.pushButton_4.setText(_translate("mainWindow", "3"))
        self.pbp.setText(_translate("mainWindow", "+"))
        self.pbm.setText(_translate("mainWindow", "-"))
        self.pbe.setText(_translate("mainWindow", "="))
        self.pb8.setText(_translate("mainWindow", "8"))
        self.pushButton_7.setText(_translate("mainWindow", "6"))
        self.pushButton_9.setText(_translate("mainWindow", "5"))
        self.pushButton_6.setText(_translate("mainWindow", "2"))
        self.pushButton_8.setText(_translate("mainWindow", "4"))
        self.pbdot.setText(_translate("mainWindow", "."))
        self.back.setText(_translate("mainWindow", "Back"))
        self.clear.setText(_translate("mainWindow", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

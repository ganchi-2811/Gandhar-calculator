from PyQt5 import QtWidgets
from Calculator import Ui_calculator



class CalculatorWindow(QtWidgets.QMainWindow, Ui_calculator):
    firstNum = None
    secondNum = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        # connect buttons
        self.pb0.clicked.connect(self.digit_pressed)
        self.pb7.clicked.connect(self.digit_pressed)
        self.pb8.clicked.connect(self.digit_pressed)
        self.pb9.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pbdot.clicked.connect(self.decimal_pressed)

        self.pbe.clicked.connect(self.equals_pressed)

        self.pbp.clicked.connect(self.binary_operation_pressed)
        self.pbm.clicked.connect(self.binary_operation_pressed)
        self.pbd.clicked.connect(self.binary_operation_pressed)
        self.pbmu.clicked.connect(self.binary_operation_pressed)

        self.clear.clicked.connect(self.clear_pressed)

        self.pbp.setCheckable(True)
        self.pbm.setCheckable(True)
        self.pbd.setCheckable(True)
        self.pbmu.setCheckable(True)

    def digit_pressed(self):
        button = self.sender()
        if ((self.pbp.isChecked() or self.pbm.isChecked() or self.pbmu.isChecked() or self.pbd.isChecked()) and (not self.secondNum)):
            newScreen = format(float(button.text()), '.15g')
            self.secondNum = True
        else:
            if(('.' in self.screen.text()) and (button.text() == '0')):
                newScreen = format(self. screen.text()+ button.text(), '.15')
            else:
                newScreen = format(float (self. screen.text()+ button.text()), '.15g')
        self.screen.setText (newScreen)
    def decimal_pressed(self):
        self.screen.setText(self.screen.text() + '.')
    def binary_operation_pressed(self):
        button = self.sender()
        self.firstNum = float(self.screen.text())
        button.setChecked(True)
    def equals_pressed(self):
        secondNum = float(self.screen.text())
        if self.pbp.isChecked():
            labelNum = self.firstNum + secondNum
            newlabel = format(labelNum, '.15g')
            self.screen.setText(newlabel)
            self.pbp.setChecked(False)
        if self.pbm.isChecked():
            labelNum = self.firstNum - secondNum
            newlabel = format(labelNum, '.15g')
            self.screen.setText(newlabel)
            self.pbm.setChecked(False)
        elif self.pbmu.isChecked():
            labelNum = self.firstNum * secondNum
            newlabel = format(labelNum, '.15g')
            self.screen.setText(newlabel)
            self.pbmu.setChecked(False)
        elif self.pbd.isChecked():
            labelNum = self.firstNum / secondNum
            newlabel = format(labelNum, '.15g')
            self.screen.setText(newlabel)
            self.pbd.setChecked(False)
        self.secondNum = False
    def clear_pressed(self):
        self.pbp.setChecked(False)
        self.pbm.setChecked(False)
        self.pbd.setChecked(False)
        self.pbmu.setChecked(False)

        self.secondNum = False
        self.screen.setText("0")
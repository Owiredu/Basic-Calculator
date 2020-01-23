# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import math
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(534, 373)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setBaseSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("calculator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(9, 9, 516, 349))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_undo = QtWidgets.QPushButton(self.widget)
        self.pushButton_undo.setObjectName("pushButton_undo")
        self.gridLayout.addWidget(self.pushButton_undo, 2, 4, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.history_text_edit = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.history_text_edit.setFont(font)
        self.history_text_edit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.history_text_edit.setLineWidth(0)
        self.history_text_edit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.history_text_edit.setReadOnly(True)
        self.history_text_edit.setTabStopWidth(80)
        self.history_text_edit.setObjectName("history_text_edit")
        self.gridLayout.addWidget(self.history_text_edit, 0, 0, 1, 6)
        self.pushButton_closing_bracket = QtWidgets.QPushButton(self.widget)
        self.pushButton_closing_bracket.setObjectName("pushButton_closing_bracket")
        self.gridLayout.addWidget(self.pushButton_closing_bracket, 3, 5, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_redo = QtWidgets.QPushButton(self.widget)
        self.pushButton_redo.setObjectName("pushButton_redo")
        self.gridLayout.addWidget(self.pushButton_redo, 2, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.pushButton_dot = QtWidgets.QPushButton(self.widget)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.gridLayout.addWidget(self.pushButton_dot, 5, 1, 1, 1)
        self.pushButton_percent = QtWidgets.QPushButton(self.widget)
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.gridLayout.addWidget(self.pushButton_percent, 5, 2, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.widget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 5, 3, 1, 1)
        self.pushButton_subtract = QtWidgets.QPushButton(self.widget)
        self.pushButton_subtract.setObjectName("pushButton_subtract")
        self.gridLayout.addWidget(self.pushButton_subtract, 5, 4, 1, 1)
        self.pushButton_equals = QtWidgets.QPushButton(self.widget)
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.gridLayout.addWidget(self.pushButton_equals, 5, 5, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)
        self.pushButton_divide = QtWidgets.QPushButton(self.widget)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout.addWidget(self.pushButton_divide, 3, 3, 1, 1)
        self.pushButton_opening_bracket = QtWidgets.QPushButton(self.widget)
        self.pushButton_opening_bracket.setObjectName("pushButton_opening_bracket")
        self.gridLayout.addWidget(self.pushButton_opening_bracket, 3, 4, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(self.widget)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout.addWidget(self.pushButton_multiply, 4, 3, 1, 1)
        self.pushButton_squared = QtWidgets.QPushButton(self.widget)
        self.pushButton_squared.setObjectName("pushButton_squared")
        self.gridLayout.addWidget(self.pushButton_squared, 4, 4, 1, 1)
        self.pushButton_sqrt = QtWidgets.QPushButton(self.widget)
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.gridLayout.addWidget(self.pushButton_sqrt, 4, 5, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.widget)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 5, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 2, 5, 1, 1)
        self.calc_line_edit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calc_line_edit.sizePolicy().hasHeightForWidth())
        self.calc_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.calc_line_edit.setFont(font)
        self.calc_line_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.calc_line_edit.setObjectName("calc_line_edit")
        self.gridLayout.addWidget(self.calc_line_edit, 1, 0, 1, 6)

        self.retranslateUi(Form)
        self.pushButton_clear.clicked.connect(self.calc_line_edit.clear)
        self.pushButton_undo.clicked.connect(self.calc_line_edit.undo)
        self.pushButton_redo.clicked.connect(self.calc_line_edit.redo)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # add events to buttons
        self.pushButton_0.clicked.connect(lambda: self.insert_input(self.pushButton_0.text()))
        self.pushButton_1.clicked.connect(lambda: self.insert_input(self.pushButton_1.text()))
        self.pushButton_2.clicked.connect(lambda: self.insert_input(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.insert_input(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.insert_input(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.insert_input(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.insert_input(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.insert_input(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.insert_input(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.insert_input(self.pushButton_9.text()))
        self.pushButton_dot.clicked.connect(lambda: self.insert_input(self.pushButton_dot.text()))
        self.pushButton_percent.clicked.connect(lambda: self.insert_input(self.pushButton_percent.text()))
        self.pushButton_add.clicked.connect(lambda: self.insert_input(self.pushButton_add.text()))
        self.pushButton_subtract.clicked.connect(lambda: self.insert_input(self.pushButton_subtract.text()))
        self.pushButton_multiply.clicked.connect(lambda: self.insert_input(self.pushButton_multiply.text()))
        self.pushButton_divide.clicked.connect(lambda: self.insert_input(self.pushButton_divide.text()))
        self.pushButton_opening_bracket.clicked.connect(lambda: self.insert_input(self.pushButton_opening_bracket.text()))
        self.pushButton_closing_bracket.clicked.connect(lambda: self.insert_input(self.pushButton_closing_bracket.text()))
        self.pushButton_sqrt.clicked.connect(lambda: self.insert_input(self.pushButton_sqrt.text() + '('))
        self.pushButton_squared.clicked.connect(lambda: self.insert_input('^2'))

        # add event to evaluate and display expression
        self.calc_line_edit.returnPressed.connect(lambda: self.calculate(self.calc_line_edit.text()))
        self.pushButton_equals.clicked.connect(lambda: self.calculate(self.calc_line_edit.text()))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.pushButton_undo.setText(_translate("Form", "undo"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_closing_bracket.setText(_translate("Form", ")"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_redo.setText(_translate("Form", "redo"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_dot.setText(_translate("Form", "."))
        self.pushButton_percent.setText(_translate("Form", "%"))
        self.pushButton_add.setText(_translate("Form", "+"))
        self.pushButton_subtract.setText(_translate("Form", "-"))
        self.pushButton_equals.setText(_translate("Form", "="))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_divide.setText(_translate("Form", "/"))
        self.pushButton_opening_bracket.setText(_translate("Form", "("))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_multiply.setText(_translate("Form", "x"))
        self.pushButton_squared.setText(_translate("Form", "x^2"))
        self.pushButton_sqrt.setText(_translate("Form", "sqrt"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_clear.setText(_translate("Form", "clear"))

    def insert_input(self, val):
        self.calc_line_edit.setText(self.calc_line_edit.text() + str(val))

    def calculate(self, expr):
        if expr[0].isdigit() or expr.startswith('(') or expr.startswith('sqrt'):
            raw_expr = expr
            expr = expr.replace('^', '**')
            expr = expr.replace('%', '/100')
            expr = expr.replace('x', '*')
            expr = expr.replace('sqrt', 'math.sqrt')
            self.calc_line_edit.clear()
            try:
                ans = str(eval(expr))
                self.calc_line_edit.setText(ans)
                self.display_history(raw_expr, ans)
            except:
                self.calc_line_edit.setText('Error')
        elif expr.strip() == '':
            pass
        else:
            self.calc_line_edit.setText('Error')
            

    def display_history(self, raw_expr, ans):
        self.history_text_edit.append(raw_expr + '  =  ' + ans)

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


class Calculator(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(534, 373)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\iVlad\Documents\DND_Client\Trade.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1007, 651)
        self.CharacterList = QtWidgets.QListWidget(Form)
        self.CharacterList.setGeometry(QtCore.QRect(10, 40, 421, 591))
        self.CharacterList.setObjectName("CharacterList")
        self.AllList = QtWidgets.QListWidget(Form)
        self.AllList.setGeometry(QtCore.QRect(570, 40, 421, 591))
        self.AllList.setObjectName("AllList")
        self.AddButton = QtWidgets.QPushButton(Form)
        self.AddButton.setGeometry(QtCore.QRect(460, 240, 81, 51))
        self.AddButton.setObjectName("AddButton")
        self.DeleteButton = QtWidgets.QPushButton(Form)
        self.DeleteButton.setGeometry(QtCore.QRect(460, 320, 81, 51))
        self.DeleteButton.setObjectName("DeleteButton")
        self.ConfirmButton = QtWidgets.QPushButton(Form)
        self.ConfirmButton.setGeometry(QtCore.QRect(450, 560, 101, 71))
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 401, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(580, 10, 401, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.AddButton.setText(_translate("Form", "<<<<<<<<<<<<<"))
        self.DeleteButton.setText(_translate("Form", ">>>>>>>>>>>>>"))
        self.ConfirmButton.setText(_translate("Form", "Ок"))
        self.label.setText(_translate("Form", "Персонаж:"))
        self.label_2.setText(_translate("Form", "Можно выбрать:"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\danma\Documents\PlayingField\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlayingField(object):
    def setupUi(self, PlayingField):
        PlayingField.setObjectName("PlayingField")
        PlayingField.resize(1267, 613)
        self.textEdit_log = QtWidgets.QTextEdit(PlayingField)
        self.textEdit_log.setGeometry(QtCore.QRect(1010, 540, 181, 51))
        self.textEdit_log.setObjectName("textEdit_log")
        self.pushButton_log = QtWidgets.QPushButton(PlayingField)
        self.pushButton_log.setGeometry(QtCore.QRect(1200, 540, 51, 51))
        self.pushButton_log.setObjectName("pushButton_log")
        self.textBrowser_log = QtWidgets.QTextBrowser(PlayingField)
        self.textBrowser_log.setGeometry(QtCore.QRect(1010, 20, 241, 511))
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.comboBox_characteristic = QtWidgets.QComboBox(PlayingField)
        self.comboBox_characteristic.setGeometry(QtCore.QRect(130, 20, 121, 21))
        self.comboBox_characteristic.setObjectName("comboBox_characteristic")
        #self.comboBox_characteristic.addItems("Сила", "Ловкость", "Телосложение", "Интеллект", "Мудрость", "Харизма")
        self.spinBox_throwNumber = QtWidgets.QSpinBox(PlayingField)
        self.spinBox_throwNumber.setGeometry(QtCore.QRect(130, 50, 42, 22))
        self.spinBox_throwNumber.setObjectName("spinBox_throwNumber")
        self.comboBox_edgeNumber = QtWidgets.QComboBox(PlayingField)
        self.comboBox_edgeNumber.setGeometry(QtCore.QRect(130, 80, 121, 22))
        self.comboBox_edgeNumber.setObjectName("comboBox_edgeNumber")
        #self.comboBox_edgeNumber.addItems("4", "6", "8", "20", "100")
        self.spinBox_modifically = QtWidgets.QSpinBox(PlayingField)
        self.spinBox_modifically.setGeometry(QtCore.QRect(130, 110, 42, 22))
        self.spinBox_modifically.setObjectName("spinBox_modifically")
        self.comboBox_throwType = QtWidgets.QComboBox(PlayingField)
        self.comboBox_throwType.setGeometry(QtCore.QRect(130, 140, 121, 22))
        self.comboBox_throwType.setObjectName("comboBox_throwType")
        #self.comboBox_throwType.addItems
        self.label_charecteristic = QtWidgets.QLabel(PlayingField)
        self.label_charecteristic.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_charecteristic.setObjectName("label_charecteristic")
        self.label_throwNumber = QtWidgets.QLabel(PlayingField)
        self.label_throwNumber.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_throwNumber.setObjectName("label_throwNumber")
        self.label_edgeNumber = QtWidgets.QLabel(PlayingField)
        self.label_edgeNumber.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label_edgeNumber.setObjectName("label_edgeNumber")
        self.label_modifically = QtWidgets.QLabel(PlayingField)
        self.label_modifically.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_modifically.setObjectName("label_modifically")
        self.label_throwType = QtWidgets.QLabel(PlayingField)
        self.label_throwType.setGeometry(QtCore.QRect(10, 140, 111, 16))
        self.label_throwType.setObjectName("label_throwType")
        self.pushButton_throw = QtWidgets.QPushButton(PlayingField)
        self.pushButton_throw.setGeometry(QtCore.QRect(10, 170, 241, 28))
        self.pushButton_throw.setObjectName("pushButton_throw")
        self.line_2 = QtWidgets.QFrame(PlayingField)
        self.line_2.setGeometry(QtCore.QRect(990, 0, 20, 611))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.quickWidget_char = QtQuickWidgets.QQuickWidget(PlayingField)
        self.quickWidget_char.setGeometry(QtCore.QRect(279, 19, 671, 551))
        self.quickWidget_char.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget_char.setObjectName("quickWidget_char")
        self.line_3 = QtWidgets.QFrame(PlayingField)
        self.line_3.setGeometry(QtCore.QRect(250, 0, 20, 611))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(PlayingField)
        self.pushButton_log.clicked.connect(self.textEdit_log.selectAll)
        QtCore.QMetaObject.connectSlotsByName(PlayingField)

        sendThrow = pyqtSignal(string, int, string, int, string)
        pushButton_log.clicked.connect(sendMsg)

    def retranslateUi(self, PlayingField):
        _translate = QtCore.QCoreApplication.translate
        PlayingField.setWindowTitle(_translate("PlayingField", "PlayingField"))
        self.pushButton_log.setText(_translate("PlayingField", "OK"))
        self.label_charecteristic.setText(_translate("PlayingField", "Характеристика"))
        self.label_throwNumber.setText(_translate("PlayingField", "Кол-во бросков"))
        self.label_edgeNumber.setText(_translate("PlayingField", "Кол-во граней"))
        self.label_modifically.setText(_translate("PlayingField", "Модификатор"))
        self.label_throwType.setText(_translate("PlayingField", "Тип броска"))
        self.pushButton_throw.setText(_translate("PlayingField", "Сделать бросок"))

    def setCharacteristic(self, list)
        self.comboBox_characteristic.addItems(list)

    def setEdgeNumber(self, list)
        self.comboBox_edgeNumber.addItems(list)

    def setThrowType(self,list)
        self.comboBox_throwType.addItems(list)

    def getThrowData(self)
        characteristic = self.comboBox_characteristic.currentText()
        throwNumber = self.spinBox_throwNumber.value()
        edgeNumber = self.comboBox_edgeNumber.currentText()
        modifically = self.spinBox_modifically.value()
        throwType = self.comboBox_throwType.currentText()
        self.sendThrow.emit(characteristic, throwNumber, edgeNumber, modifically, throwType)

    def editLog(self, text)
        self.textBrowser_log.append(text)

    def sendMsg(self)
        self.editLog(self.editLog.toPlainText())


from PyQt5 import QtQuickWidgets

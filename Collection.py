# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\iVlad\Documents\DND_Client\Collection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class CollectionForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1198, 850)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1201, 861))
        self.tabWidget.setObjectName("tabWidget")
        self.Classes = QtWidgets.QWidget()
        self.Classes.setObjectName("Classes")
        self.CLASSES_LIST = QtWidgets.QListWidget(self.Classes)
        self.CLASSES_LIST.setGeometry(QtCore.QRect(0, 0, 256, 821))
        self.CLASSES_LIST.setObjectName("CLASSES_LIST")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.Classes)
        self.tabWidget_2.setGeometry(QtCore.QRect(260, 0, 941, 831))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName("label")
        self.HITDICE = QtWidgets.QLabel(self.tab)
        self.HITDICE.setGeometry(QtCore.QRect(90, 10, 781, 16))
        self.HITDICE.setText("")
        self.HITDICE.setObjectName("HITDICE")
        self.HP_ON_FIRST_LVL = QtWidgets.QLabel(self.tab)
        self.HP_ON_FIRST_LVL.setGeometry(QtCore.QRect(90, 30, 781, 16))
        self.HP_ON_FIRST_LVL.setText("")
        self.HP_ON_FIRST_LVL.setObjectName("HP_ON_FIRST_LVL")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.HP_UPGRADE = QtWidgets.QLabel(self.tab)
        self.HP_UPGRADE.setGeometry(QtCore.QRect(90, 50, 781, 16))
        self.HP_UPGRADE.setText("")
        self.HP_UPGRADE.setObjectName("HP_UPGRADE")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(70, 70, 851, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ARMOR = QtWidgets.QLabel(self.tab)
        self.ARMOR.setGeometry(QtCore.QRect(90, 90, 781, 16))
        self.ARMOR.setText("")
        self.ARMOR.setObjectName("ARMOR")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_5.setObjectName("label_5")
        self.WEAPON = QtWidgets.QLabel(self.tab)
        self.WEAPON.setGeometry(QtCore.QRect(90, 110, 781, 16))
        self.WEAPON.setText("")
        self.WEAPON.setObjectName("WEAPON")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_6.setObjectName("label_6")
        self.TOOLS = QtWidgets.QLabel(self.tab)
        self.TOOLS.setGeometry(QtCore.QRect(90, 130, 781, 16))
        self.TOOLS.setText("")
        self.TOOLS.setObjectName("TOOLS")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.label_7.setObjectName("label_7")
        self.SAVING_THROWS = QtWidgets.QLabel(self.tab)
        self.SAVING_THROWS.setGeometry(QtCore.QRect(90, 150, 781, 16))
        self.SAVING_THROWS.setText("")
        self.SAVING_THROWS.setObjectName("SAVING_THROWS")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_8.setObjectName("label_8")
        self.SKILLS = QtWidgets.QLabel(self.tab)
        self.SKILLS.setGeometry(QtCore.QRect(90, 170, 781, 31))
        self.SKILLS.setText("")
        self.SKILLS.setObjectName("SKILLS")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 170, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.label_10.setObjectName("label_10")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(90, 210, 831, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.INVENTORY_LIST = QtWidgets.QListView(self.tab)
        self.INVENTORY_LIST.setGeometry(QtCore.QRect(20, 270, 891, 171))
        self.INVENTORY_LIST.setObjectName("INVENTORY_LIST")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(20, 240, 611, 21))
        self.label_11.setObjectName("label_11")
        self.ALTERNATIVE = QtWidgets.QLabel(self.tab)
        self.ALTERNATIVE.setGeometry(QtCore.QRect(20, 460, 891, 61))
        self.ALTERNATIVE.setText("")
        self.ALTERNATIVE.setObjectName("ALTERNATIVE")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.CLASS_DISCRIPTION = QtWidgets.QLabel(self.tab_2)
        self.CLASS_DISCRIPTION.setGeometry(QtCore.QRect(0, 0, 931, 801))
        self.CLASS_DISCRIPTION.setText("")
        self.CLASS_DISCRIPTION.setObjectName("CLASS_DISCRIPTION")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.Spells = QtWidgets.QWidget()
        self.Spells.setObjectName("Spells")
        self.SPELL_LIST = QtWidgets.QListView(self.Spells)
        self.SPELL_LIST.setGeometry(QtCore.QRect(10, 0, 901, 801))
        self.SPELL_LIST.setObjectName("SPELL_LIST")
        self.tabWidget_2.addTab(self.Spells, "")
        self.tabWidget.addTab(self.Classes, "")
        self.Races = QtWidgets.QWidget()
        self.Races.setObjectName("Races")
        self.RACES_LIST = QtWidgets.QListWidget(self.Races)
        self.RACES_LIST.setGeometry(QtCore.QRect(0, 0, 256, 821))
        self.RACES_LIST.setObjectName("RACES_LIST")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.Races)
        self.tabWidget_3.setGeometry(QtCore.QRect(260, 0, 941, 831))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label_12.setObjectName("label_12")
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setGeometry(QtCore.QRect(110, 20, 801, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_37 = QtWidgets.QLabel(self.tab_3)
        self.label_37.setGeometry(QtCore.QRect(10, 40, 171, 21))
        self.label_37.setObjectName("label_37")
        self.ATTRIBUTE_UP = QtWidgets.QLabel(self.tab_3)
        self.ATTRIBUTE_UP.setGeometry(QtCore.QRect(190, 40, 681, 20))
        self.ATTRIBUTE_UP.setText("")
        self.ATTRIBUTE_UP.setObjectName("ATTRIBUTE_UP")
        self.SIZE = QtWidgets.QLabel(self.tab_3)
        self.SIZE.setGeometry(QtCore.QRect(190, 70, 681, 20))
        self.SIZE.setText("")
        self.SIZE.setObjectName("SIZE")
        self.label_38 = QtWidgets.QLabel(self.tab_3)
        self.label_38.setGeometry(QtCore.QRect(10, 70, 171, 21))
        self.label_38.setObjectName("label_38")
        self.SPEED = QtWidgets.QLabel(self.tab_3)
        self.SPEED.setGeometry(QtCore.QRect(190, 100, 681, 20))
        self.SPEED.setText("")
        self.SPEED.setObjectName("SPEED")
        self.label_39 = QtWidgets.QLabel(self.tab_3)
        self.label_39.setGeometry(QtCore.QRect(10, 100, 171, 21))
        self.label_39.setObjectName("label_39")
        self.IDEOLOGY = QtWidgets.QLabel(self.tab_3)
        self.IDEOLOGY.setGeometry(QtCore.QRect(190, 130, 681, 20))
        self.IDEOLOGY.setText("")
        self.IDEOLOGY.setObjectName("IDEOLOGY")
        self.label_40 = QtWidgets.QLabel(self.tab_3)
        self.label_40.setGeometry(QtCore.QRect(10, 130, 171, 21))
        self.label_40.setObjectName("label_40")
        self.AGE = QtWidgets.QLabel(self.tab_3)
        self.AGE.setGeometry(QtCore.QRect(190, 160, 681, 20))
        self.AGE.setText("")
        self.AGE.setObjectName("AGE")
        self.label_41 = QtWidgets.QLabel(self.tab_3)
        self.label_41.setGeometry(QtCore.QRect(10, 160, 171, 21))
        self.label_41.setObjectName("label_41")
        self.line_11 = QtWidgets.QFrame(self.tab_3)
        self.line_11.setGeometry(QtCore.QRect(90, 200, 821, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_48 = QtWidgets.QLabel(self.tab_3)
        self.label_48.setGeometry(QtCore.QRect(10, 190, 71, 31))
        self.label_48.setObjectName("label_48")
        self.RACE_SKILLS = QtWidgets.QListView(self.tab_3)
        self.RACE_SKILLS.setGeometry(QtCore.QRect(10, 220, 911, 571))
        self.RACE_SKILLS.setObjectName("RACE_SKILLS")
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.RACE_DISCRIPTION = QtWidgets.QLabel(self.tab_4)
        self.RACE_DISCRIPTION.setGeometry(QtCore.QRect(0, 0, 941, 811))
        self.RACE_DISCRIPTION.setText("")
        self.RACE_DISCRIPTION.setObjectName("RACE_DISCRIPTION")
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.Races, "")
        self.Background = QtWidgets.QWidget()
        self.Background.setObjectName("Background")
        self.BACKGROUND_LIST = QtWidgets.QListWidget(self.Background)
        self.BACKGROUND_LIST.setGeometry(QtCore.QRect(0, 0, 256, 821))
        self.BACKGROUND_LIST.setObjectName("BACKGROUND_LIST")
        self.line_18 = QtWidgets.QFrame(self.Background)
        self.line_18.setGeometry(QtCore.QRect(370, 9, 801, 31))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.label_74 = QtWidgets.QLabel(self.Background)
        self.label_74.setGeometry(QtCore.QRect(270, 10, 81, 31))
        self.label_74.setObjectName("label_74")
        self.BACKGROUND_ATTRIBUTES = QtWidgets.QLabel(self.Background)
        self.BACKGROUND_ATTRIBUTES.setGeometry(QtCore.QRect(390, 40, 741, 20))
        self.BACKGROUND_ATTRIBUTES.setText("")
        self.BACKGROUND_ATTRIBUTES.setObjectName("BACKGROUND_ATTRIBUTES")
        self.label_75 = QtWidgets.QLabel(self.Background)
        self.label_75.setGeometry(QtCore.QRect(270, 40, 111, 16))
        self.label_75.setObjectName("label_75")
        self.BACKGROUND_LANGUAGES = QtWidgets.QLabel(self.Background)
        self.BACKGROUND_LANGUAGES.setGeometry(QtCore.QRect(350, 70, 781, 16))
        self.BACKGROUND_LANGUAGES.setText("")
        self.BACKGROUND_LANGUAGES.setObjectName("BACKGROUND_LANGUAGES")
        self.label_76 = QtWidgets.QLabel(self.Background)
        self.label_76.setGeometry(QtCore.QRect(270, 70, 81, 16))
        self.label_76.setObjectName("label_76")
        self.BACKGROUND_EQUPMENT = QtWidgets.QLabel(self.Background)
        self.BACKGROUND_EQUPMENT.setGeometry(QtCore.QRect(350, 100, 781, 16))
        self.BACKGROUND_EQUPMENT.setText("")
        self.BACKGROUND_EQUPMENT.setObjectName("BACKGROUND_EQUPMENT")
        self.label_77 = QtWidgets.QLabel(self.Background)
        self.label_77.setGeometry(QtCore.QRect(270, 100, 81, 16))
        self.label_77.setObjectName("label_77")
        self.BACKGROUND_TOOLS = QtWidgets.QLabel(self.Background)
        self.BACKGROUND_TOOLS.setGeometry(QtCore.QRect(350, 130, 781, 16))
        self.BACKGROUND_TOOLS.setText("")
        self.BACKGROUND_TOOLS.setObjectName("BACKGROUND_TOOLS")
        self.label_78 = QtWidgets.QLabel(self.Background)
        self.label_78.setGeometry(QtCore.QRect(270, 130, 81, 16))
        self.label_78.setObjectName("label_78")
        self.label_102 = QtWidgets.QLabel(self.Background)
        self.label_102.setGeometry(QtCore.QRect(270, 161, 81, 31))
        self.label_102.setObjectName("label_102")
        self.line_24 = QtWidgets.QFrame(self.Background)
        self.line_24.setGeometry(QtCore.QRect(370, 160, 801, 31))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.BACKGROUND_SKILL = QtWidgets.QLabel(self.Background)
        self.BACKGROUND_SKILL.setGeometry(QtCore.QRect(270, 190, 911, 151))
        self.BACKGROUND_SKILL.setText("")
        self.BACKGROUND_SKILL.setObjectName("BACKGROUND_SKILL")
        self.tabWidget.addTab(self.Background, "")
        self.Items = QtWidgets.QWidget()
        self.Items.setObjectName("Items")
        self.ITEM_LIST = QtWidgets.QListWidget(self.Items)
        self.ITEM_LIST.setGeometry(QtCore.QRect(0, 0, 256, 821))
        self.ITEM_LIST.setObjectName("ITEM_LIST")
        self.CATEGORIES = QtWidgets.QLabel(self.Items)
        self.CATEGORIES.setGeometry(QtCore.QRect(390, 10, 741, 20))
        self.CATEGORIES.setText("")
        self.CATEGORIES.setObjectName("CATEGORIES")
        self.label_319 = QtWidgets.QLabel(self.Items)
        self.label_319.setGeometry(QtCore.QRect(270, 10, 111, 16))
        self.label_319.setObjectName("label_319")
        self.MASS = QtWidgets.QLabel(self.Items)
        self.MASS.setGeometry(QtCore.QRect(390, 40, 741, 20))
        self.MASS.setText("")
        self.MASS.setObjectName("MASS")
        self.label_320 = QtWidgets.QLabel(self.Items)
        self.label_320.setGeometry(QtCore.QRect(270, 40, 111, 16))
        self.label_320.setObjectName("label_320")
        self.label_321 = QtWidgets.QLabel(self.Items)
        self.label_321.setGeometry(QtCore.QRect(270, 70, 111, 16))
        self.label_321.setObjectName("label_321")
        self.PRICE = QtWidgets.QLabel(self.Items)
        self.PRICE.setGeometry(QtCore.QRect(390, 70, 741, 20))
        self.PRICE.setText("")
        self.PRICE.setObjectName("PRICE")
        self.BACKGROUND_ATTRIBUTES_14 = QtWidgets.QLabel(self.Items)
        self.BACKGROUND_ATTRIBUTES_14.setGeometry(QtCore.QRect(390, 100, 741, 20))
        self.BACKGROUND_ATTRIBUTES_14.setText("")
        self.BACKGROUND_ATTRIBUTES_14.setObjectName("BACKGROUND_ATTRIBUTES_14")
        self.label_377 = QtWidgets.QLabel(self.Items)
        self.label_377.setGeometry(QtCore.QRect(270, 101, 81, 31))
        self.label_377.setObjectName("label_377")
        self.line_91 = QtWidgets.QFrame(self.Items)
        self.line_91.setGeometry(QtCore.QRect(370, 100, 801, 31))
        self.line_91.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_91.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_91.setObjectName("line_91")
        self.PECULIARITIES = QtWidgets.QListView(self.Items)
        self.PECULIARITIES.setGeometry(QtCore.QRect(270, 130, 911, 171))
        self.PECULIARITIES.setObjectName("PECULIARITIES")
        self.line_93 = QtWidgets.QFrame(self.Items)
        self.line_93.setGeometry(QtCore.QRect(370, 309, 801, 31))
        self.line_93.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_93.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_93.setObjectName("line_93")
        self.label_378 = QtWidgets.QLabel(self.Items)
        self.label_378.setGeometry(QtCore.QRect(270, 310, 81, 31))
        self.label_378.setObjectName("label_378")
        self.ITEM_DISCRIPTION = QtWidgets.QLabel(self.Items)
        self.ITEM_DISCRIPTION.setGeometry(QtCore.QRect(270, 340, 911, 481))
        self.ITEM_DISCRIPTION.setText("")
        self.ITEM_DISCRIPTION.setObjectName("ITEM_DISCRIPTION")
        self.tabWidget.addTab(self.Items, "")
        self.Spells1 = QtWidgets.QWidget()
        self.Spells1.setObjectName("Spells1")
        self.SPELLS_LIST = QtWidgets.QListWidget(self.Spells1)
        self.SPELLS_LIST.setGeometry(QtCore.QRect(0, 0, 256, 821))
        self.SPELLS_LIST.setObjectName("SPELLS_LIST")
        self.SPELL_NAME = QtWidgets.QLabel(self.Spells1)
        self.SPELL_NAME.setGeometry(QtCore.QRect(280, 10, 891, 31))
        self.SPELL_NAME.setText("")
        self.SPELL_NAME.setObjectName("SPELL_NAME")
        self.line_92 = QtWidgets.QFrame(self.Spells1)
        self.line_92.setGeometry(QtCore.QRect(280, 50, 891, 16))
        self.line_92.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_92.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_92.setObjectName("line_92")
        self.SPELL_TAGS = QtWidgets.QLabel(self.Spells1)
        self.SPELL_TAGS.setGeometry(QtCore.QRect(280, 70, 891, 21))
        self.SPELL_TAGS.setText("")
        self.SPELL_TAGS.setObjectName("SPELL_TAGS")
        self.CAST_TIME = QtWidgets.QLabel(self.Spells1)
        self.CAST_TIME.setGeometry(QtCore.QRect(390, 110, 741, 20))
        self.CAST_TIME.setText("")
        self.CAST_TIME.setObjectName("CAST_TIME")
        self.label_490 = QtWidgets.QLabel(self.Spells1)
        self.label_490.setGeometry(QtCore.QRect(270, 110, 111, 16))
        self.label_490.setObjectName("label_490")
        self.label_491 = QtWidgets.QLabel(self.Spells1)
        self.label_491.setGeometry(QtCore.QRect(270, 140, 111, 16))
        self.label_491.setObjectName("label_491")
        self.CAST_DISTANSE = QtWidgets.QLabel(self.Spells1)
        self.CAST_DISTANSE.setGeometry(QtCore.QRect(390, 140, 741, 20))
        self.CAST_DISTANSE.setText("")
        self.CAST_DISTANSE.setObjectName("CAST_DISTANSE")
        self.label_492 = QtWidgets.QLabel(self.Spells1)
        self.label_492.setGeometry(QtCore.QRect(270, 170, 111, 16))
        self.label_492.setObjectName("label_492")
        self.CAST_COMPONENTS = QtWidgets.QLabel(self.Spells1)
        self.CAST_COMPONENTS.setGeometry(QtCore.QRect(390, 170, 741, 20))
        self.CAST_COMPONENTS.setText("")
        self.CAST_COMPONENTS.setObjectName("CAST_COMPONENTS")
        self.label_493 = QtWidgets.QLabel(self.Spells1)
        self.label_493.setGeometry(QtCore.QRect(270, 200, 111, 16))
        self.label_493.setObjectName("label_493")
        self.SPELL_DURATION = QtWidgets.QLabel(self.Spells1)
        self.SPELL_DURATION.setGeometry(QtCore.QRect(390, 200, 741, 20))
        self.SPELL_DURATION.setText("")
        self.SPELL_DURATION.setObjectName("SPELL_DURATION")
        self.label_494 = QtWidgets.QLabel(self.Spells1)
        self.label_494.setGeometry(QtCore.QRect(270, 230, 111, 16))
        self.label_494.setObjectName("label_494")
        self.SPELL_CLASSES = QtWidgets.QLabel(self.Spells1)
        self.SPELL_CLASSES.setGeometry(QtCore.QRect(390, 230, 741, 20))
        self.SPELL_CLASSES.setText("")
        self.SPELL_CLASSES.setObjectName("SPELL_CLASSES")
        self.line_125 = QtWidgets.QFrame(self.Spells1)
        self.line_125.setGeometry(QtCore.QRect(280, 260, 891, 16))
        self.line_125.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_125.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_125.setObjectName("line_125")
        self.SPELL_DISCRIPTION = QtWidgets.QLabel(self.Spells1)
        self.SPELL_DISCRIPTION.setGeometry(QtCore.QRect(270, 280, 901, 131))
        self.SPELL_DISCRIPTION.setText("")
        self.SPELL_DISCRIPTION.setObjectName("SPELL_DISCRIPTION")
        self.tabWidget.addTab(self.Spells1, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Кость хитов:"))
        self.label_2.setText(_translate("Form", "Хиты на 1ур:"))
        self.label_3.setText(_translate("Form", "Повышение хп:"))
        self.label_4.setText(_translate("Form", "ВЛАДЕНИЕ"))
        self.label_5.setText(_translate("Form", "Доспехи:"))
        self.label_6.setText(_translate("Form", "Оружие:"))
        self.label_7.setText(_translate("Form", "Инструменты:"))
        self.label_8.setText(_translate("Form", "Спасброски:"))
        self.label_9.setText(_translate("Form", "Навыки:"))
        self.label_10.setText(_translate("Form", "СНАРЯЖЕНИЕ"))
        self.label_11.setText(_translate("Form", "Вы начинаете со следующим снаряжением в дополнение к снаряжению, полученному за вашу предысторию:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("Form", "Навыки"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form", "Описание"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Spells), _translate("Form", "Заклинания"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Classes), _translate("Form", "Классы"))
        self.label_12.setText(_translate("Form", "ОСОБЕННОСТИ"))
        self.label_37.setText(_translate("Form", "Повышение характеристик:"))
        self.label_38.setText(_translate("Form", "Размер"))
        self.label_39.setText(_translate("Form", "Скорость"))
        self.label_40.setText(_translate("Form", "Мировзрение"))
        self.label_41.setText(_translate("Form", "Возраст"))
        self.label_48.setText(_translate("Form", "УМЕНИЯ"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("Form", "Навыки"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("Form", "Описание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Races), _translate("Form", "Рассы"))
        self.label_74.setText(_translate("Form", "ОСОБЕННОСТИ"))
        self.label_75.setText(_translate("Form", "Владение навыками:"))
        self.label_76.setText(_translate("Form", "Языки:"))
        self.label_77.setText(_translate("Form", "Снаряжение:"))
        self.label_78.setText(_translate("Form", "Инструменты:"))
        self.label_102.setText(_translate("Form", "УМЕНИЕ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Background), _translate("Form", "Предыстории"))
        self.label_319.setText(_translate("Form", "Категории:"))
        self.label_320.setText(_translate("Form", "Вес:"))
        self.label_321.setText(_translate("Form", "Стоимость"))
        self.label_377.setText(_translate("Form", "ОСОБЕННОСТИ"))
        self.label_378.setText(_translate("Form", "ОПИСАНИЕ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Items), _translate("Form", "Предметы"))
        self.label_490.setText(_translate("Form", "Время накладывания:"))
        self.label_491.setText(_translate("Form", "Дистанция:"))
        self.label_492.setText(_translate("Form", "Компоненты:"))
        self.label_493.setText(_translate("Form", "Длительность:"))
        self.label_494.setText(_translate("Form", "Классы:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Spells1), _translate("Form", "Заклинания"))

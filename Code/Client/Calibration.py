# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibration.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_calibration(object):
    def setupUi(self, calibration):
        calibration.setObjectName("calibration")
        calibration.resize(697, 353)
        font = QtGui.QFont()
        font.setFamily("Arial")
        calibration.setFont(font)
        calibration.setStyleSheet("QWidget{\n"
"background:#484848;\n"
"}\n"
"QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #383838);\n"
"}\n"
"QAbstractButton:hover{\n"
"color:#000000;\n"
"background-color:#008aff;\n"
"}\n"
"QAbstractButton:pressed{\n"
"color:#DCDCDC;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 4px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#008aff;\n"
"background-color:#444444;\n"
"}\n"
"\n"
"QLabel{\n"
"color:#DCDCDC;\n"
"\n"
"\n"
"}\n"
"QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"lineedit-password-character:9679;\n"
"}\n"
"")
        self.radioButton_one = QtWidgets.QRadioButton(calibration)
        self.radioButton_one.setGeometry(QtCore.QRect(30, 25, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.radioButton_one.setFont(font)
        self.radioButton_one.setStyleSheet("font: 10pt \"Arial\";")
        self.radioButton_one.setObjectName("radioButton_one")
        self.radioButton_two = QtWidgets.QRadioButton(calibration)
        self.radioButton_two.setGeometry(QtCore.QRect(30, 55, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.radioButton_two.setFont(font)
        self.radioButton_two.setStyleSheet("font: 10pt \"Arial\";")
        self.radioButton_two.setObjectName("radioButton_two")
        self.radioButton_three = QtWidgets.QRadioButton(calibration)
        self.radioButton_three.setGeometry(QtCore.QRect(30, 85, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.radioButton_three.setFont(font)
        self.radioButton_three.setStyleSheet("font: 10pt \"Arial\";")
        self.radioButton_three.setObjectName("radioButton_three")
        self.radioButton_four = QtWidgets.QRadioButton(calibration)
        self.radioButton_four.setGeometry(QtCore.QRect(30, 115, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.radioButton_four.setFont(font)
        self.radioButton_four.setStyleSheet("font: 10pt \"Arial\";")
        self.radioButton_four.setObjectName("radioButton_four")
        self.Button_X1 = QtWidgets.QPushButton(calibration)
        self.Button_X1.setGeometry(QtCore.QRect(230, 235, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.Button_X1.setFont(font)
        self.Button_X1.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_X1.setObjectName("Button_X1")
        self.Button_Z1 = QtWidgets.QPushButton(calibration)
        self.Button_Z1.setGeometry(QtCore.QRect(230, 275, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.Button_Z1.setFont(font)
        self.Button_Z1.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Z1.setObjectName("Button_Z1")
        self.Button_Y2 = QtWidgets.QPushButton(calibration)
        self.Button_Y2.setGeometry(QtCore.QRect(130, 225, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.Button_Y2.setFont(font)
        self.Button_Y2.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Y2.setObjectName("Button_Y2")
        self.Button_Z2 = QtWidgets.QPushButton(calibration)
        self.Button_Z2.setGeometry(QtCore.QRect(30, 275, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.Button_Z2.setFont(font)
        self.Button_Z2.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Z2.setObjectName("Button_Z2")
        self.Button_X2 = QtWidgets.QPushButton(calibration)
        self.Button_X2.setGeometry(QtCore.QRect(30, 235, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.Button_X2.setFont(font)
        self.Button_X2.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_X2.setObjectName("Button_X2")
        self.Button_Y1 = QtWidgets.QPushButton(calibration)
        self.Button_Y1.setGeometry(QtCore.QRect(130, 305, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.Button_Y1.setFont(font)
        self.Button_Y1.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Y1.setObjectName("Button_Y1")
        self.label = QtWidgets.QLabel(calibration)
        self.label.setGeometry(QtCore.QRect(110, 30, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 10pt \"Arial\";")
        self.label.setObjectName("label")
        self.one_x = QtWidgets.QLineEdit(calibration)
        self.one_x.setGeometry(QtCore.QRect(135, 25, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.one_x.setFont(font)
        self.one_x.setStyleSheet("font: 10pt \"Arial\";")
        self.one_x.setAlignment(QtCore.Qt.AlignCenter)
        self.one_x.setObjectName("one_x")
        self.one_y = QtWidgets.QLineEdit(calibration)
        self.one_y.setGeometry(QtCore.QRect(210, 25, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.one_y.setFont(font)
        self.one_y.setStyleSheet("font: 10pt \"Arial\";")
        self.one_y.setAlignment(QtCore.Qt.AlignCenter)
        self.one_y.setObjectName("one_y")
        self.label_2 = QtWidgets.QLabel(calibration)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 10pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.one_z = QtWidgets.QLineEdit(calibration)
        self.one_z.setGeometry(QtCore.QRect(285, 25, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.one_z.setFont(font)
        self.one_z.setStyleSheet("font: 10pt \"Arial\";")
        self.one_z.setAlignment(QtCore.Qt.AlignCenter)
        self.one_z.setObjectName("one_z")
        self.label_3 = QtWidgets.QLabel(calibration)
        self.label_3.setGeometry(QtCore.QRect(265, 30, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 10pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.two_y = QtWidgets.QLineEdit(calibration)
        self.two_y.setGeometry(QtCore.QRect(210, 55, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.two_y.setFont(font)
        self.two_y.setStyleSheet("font: 10pt \"Arial\";")
        self.two_y.setAlignment(QtCore.Qt.AlignCenter)
        self.two_y.setObjectName("two_y")
        self.two_x = QtWidgets.QLineEdit(calibration)
        self.two_x.setGeometry(QtCore.QRect(135, 55, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.two_x.setFont(font)
        self.two_x.setStyleSheet("font: 10pt \"Arial\";")
        self.two_x.setAlignment(QtCore.Qt.AlignCenter)
        self.two_x.setObjectName("two_x")
        self.label_4 = QtWidgets.QLabel(calibration)
        self.label_4.setGeometry(QtCore.QRect(190, 60, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 10pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.two_z = QtWidgets.QLineEdit(calibration)
        self.two_z.setGeometry(QtCore.QRect(285, 55, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.two_z.setFont(font)
        self.two_z.setStyleSheet("font: 10pt \"Arial\";")
        self.two_z.setAlignment(QtCore.Qt.AlignCenter)
        self.two_z.setObjectName("two_z")
        self.label_5 = QtWidgets.QLabel(calibration)
        self.label_5.setGeometry(QtCore.QRect(265, 60, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 10pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(calibration)
        self.label_6.setGeometry(QtCore.QRect(110, 60, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 10pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.three_y = QtWidgets.QLineEdit(calibration)
        self.three_y.setGeometry(QtCore.QRect(210, 85, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.three_y.setFont(font)
        self.three_y.setStyleSheet("font: 10pt \"Arial\";")
        self.three_y.setAlignment(QtCore.Qt.AlignCenter)
        self.three_y.setObjectName("three_y")
        self.three_x = QtWidgets.QLineEdit(calibration)
        self.three_x.setGeometry(QtCore.QRect(135, 85, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.three_x.setFont(font)
        self.three_x.setStyleSheet("font: 10pt \"Arial\";")
        self.three_x.setAlignment(QtCore.Qt.AlignCenter)
        self.three_x.setObjectName("three_x")
        self.label_7 = QtWidgets.QLabel(calibration)
        self.label_7.setGeometry(QtCore.QRect(190, 90, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 10pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.three_z = QtWidgets.QLineEdit(calibration)
        self.three_z.setGeometry(QtCore.QRect(285, 85, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.three_z.setFont(font)
        self.three_z.setStyleSheet("font: 10pt \"Arial\";")
        self.three_z.setAlignment(QtCore.Qt.AlignCenter)
        self.three_z.setObjectName("three_z")
        self.label_8 = QtWidgets.QLabel(calibration)
        self.label_8.setGeometry(QtCore.QRect(265, 90, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 10pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(calibration)
        self.label_9.setGeometry(QtCore.QRect(110, 90, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 10pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.four_y = QtWidgets.QLineEdit(calibration)
        self.four_y.setGeometry(QtCore.QRect(210, 115, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.four_y.setFont(font)
        self.four_y.setStyleSheet("font: 10pt \"Arial\";")
        self.four_y.setAlignment(QtCore.Qt.AlignCenter)
        self.four_y.setObjectName("four_y")
        self.four_x = QtWidgets.QLineEdit(calibration)
        self.four_x.setGeometry(QtCore.QRect(135, 115, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.four_x.setFont(font)
        self.four_x.setStyleSheet("font: 10pt \"Arial\";")
        self.four_x.setAlignment(QtCore.Qt.AlignCenter)
        self.four_x.setObjectName("four_x")
        self.label_10 = QtWidgets.QLabel(calibration)
        self.label_10.setGeometry(QtCore.QRect(190, 120, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 10pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.four_z = QtWidgets.QLineEdit(calibration)
        self.four_z.setGeometry(QtCore.QRect(285, 115, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.four_z.setFont(font)
        self.four_z.setStyleSheet("font: 10pt \"Arial\";")
        self.four_z.setAlignment(QtCore.Qt.AlignCenter)
        self.four_z.setObjectName("four_z")
        self.label_11 = QtWidgets.QLabel(calibration)
        self.label_11.setGeometry(QtCore.QRect(265, 120, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 10pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(calibration)
        self.label_12.setGeometry(QtCore.QRect(110, 120, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font: 10pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.Button_Save = QtWidgets.QPushButton(calibration)
        self.Button_Save.setGeometry(QtCore.QRect(130, 265, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.Button_Save.setFont(font)
        self.Button_Save.setStyleSheet("font: 10pt \"Arial\";")
        self.Button_Save.setObjectName("Button_Save")
        self.label_picture = QtWidgets.QLabel(calibration)
        self.label_picture.setGeometry(QtCore.QRect(355, 20, 320, 320))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_picture.setFont(font)
        self.label_picture.setStyleSheet("font: 10pt \"Arial\";")
        self.label_picture.setText("")
        self.label_picture.setObjectName("label_picture")
        self.five_x = QtWidgets.QLineEdit(calibration)
        self.five_x.setGeometry(QtCore.QRect(135, 145, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.five_x.setFont(font)
        self.five_x.setStyleSheet("font: 10pt \"Arial\";")
        self.five_x.setAlignment(QtCore.Qt.AlignCenter)
        self.five_x.setObjectName("five_x")
        self.five_z = QtWidgets.QLineEdit(calibration)
        self.five_z.setGeometry(QtCore.QRect(285, 145, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.five_z.setFont(font)
        self.five_z.setStyleSheet("font: 10pt \"Arial\";")
        self.five_z.setAlignment(QtCore.Qt.AlignCenter)
        self.five_z.setObjectName("five_z")
        self.radioButton_five = QtWidgets.QRadioButton(calibration)
        self.radioButton_five.setGeometry(QtCore.QRect(30, 145, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.radioButton_five.setFont(font)
        self.radioButton_five.setStyleSheet("font: 10pt \"Arial\";")
        self.radioButton_five.setObjectName("radioButton_five")
        self.six_z = QtWidgets.QLineEdit(calibration)
        self.six_z.setGeometry(QtCore.QRect(285, 175, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.six_z.setFont(font)
        self.six_z.setStyleSheet("font: 10pt \"Arial\";")
        self.six_z.setAlignment(QtCore.Qt.AlignCenter)
        self.six_z.setObjectName("six_z")
        self.six_y = QtWidgets.QLineEdit(calibration)
        self.six_y.setGeometry(QtCore.QRect(210, 175, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.six_y.setFont(font)
        self.six_y.setStyleSheet("font: 10pt \"Arial\";")
        self.six_y.setAlignment(QtCore.Qt.AlignCenter)
        self.six_y.setObjectName("six_y")
        self.label_13 = QtWidgets.QLabel(calibration)
        self.label_13.setGeometry(QtCore.QRect(110, 150, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("font: 10pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(calibration)
        self.label_14.setGeometry(QtCore.QRect(265, 150, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font: 10pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(calibration)
        self.label_15.setGeometry(QtCore.QRect(190, 150, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font: 10pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.radioButton_six = QtWidgets.QRadioButton(calibration)
        self.radioButton_six.setGeometry(QtCore.QRect(30, 175, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.radioButton_six.setFont(font)
        self.radioButton_six.setStyleSheet("font: 10pt \"Arial\";")
        self.radioButton_six.setObjectName("radioButton_six")
        self.label_16 = QtWidgets.QLabel(calibration)
        self.label_16.setGeometry(QtCore.QRect(110, 180, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("font: 10pt \"Arial\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(calibration)
        self.label_17.setGeometry(QtCore.QRect(190, 180, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 10pt \"Arial\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(calibration)
        self.label_18.setGeometry(QtCore.QRect(265, 180, 15, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font: 10pt \"Arial\";")
        self.label_18.setObjectName("label_18")
        self.five_y = QtWidgets.QLineEdit(calibration)
        self.five_y.setGeometry(QtCore.QRect(210, 145, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.five_y.setFont(font)
        self.five_y.setStyleSheet("font: 10pt \"Arial\";")
        self.five_y.setAlignment(QtCore.Qt.AlignCenter)
        self.five_y.setObjectName("five_y")
        self.six_x = QtWidgets.QLineEdit(calibration)
        self.six_x.setGeometry(QtCore.QRect(135, 175, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight.Thin)
        self.six_x.setFont(font)
        self.six_x.setStyleSheet("font: 10pt \"Arial\";")
        self.six_x.setAlignment(QtCore.Qt.AlignCenter)
        self.six_x.setObjectName("six_x")

        self.retranslateUi(calibration)
        QtCore.QMetaObject.connectSlotsByName(calibration)

    def retranslateUi(self, calibration):
        _translate = QtCore.QCoreApplication.translate
        calibration.setWindowTitle(_translate("calibration", "Calibration"))
        self.radioButton_one.setText(_translate("calibration", "One"))
        self.radioButton_two.setText(_translate("calibration", "Two"))
        self.radioButton_three.setText(_translate("calibration", "Three"))
        self.radioButton_four.setText(_translate("calibration", "Four"))
        self.Button_X1.setText(_translate("calibration", "X+"))
        self.Button_Z1.setText(_translate("calibration", "Z+"))
        self.Button_Y2.setText(_translate("calibration", "Y-"))
        self.Button_Z2.setText(_translate("calibration", "Z-"))
        self.Button_X2.setText(_translate("calibration", "X-"))
        self.Button_Y1.setText(_translate("calibration", "Y+"))
        self.label.setText(_translate("calibration", "X:"))
        self.one_x.setText(_translate("calibration", "0"))
        self.one_y.setText(_translate("calibration", "72"))
        self.label_2.setText(_translate("calibration", "Y:"))
        self.one_z.setText(_translate("calibration", "0"))
        self.label_3.setText(_translate("calibration", "Z:"))
        self.two_y.setText(_translate("calibration", "72"))
        self.two_x.setText(_translate("calibration", "0"))
        self.label_4.setText(_translate("calibration", "Y:"))
        self.two_z.setText(_translate("calibration", "0"))
        self.label_5.setText(_translate("calibration", "Z:"))
        self.label_6.setText(_translate("calibration", "X:"))
        self.three_y.setText(_translate("calibration", "72"))
        self.three_x.setText(_translate("calibration", "0"))
        self.label_7.setText(_translate("calibration", "Y:"))
        self.three_z.setText(_translate("calibration", "0"))
        self.label_8.setText(_translate("calibration", "Z:"))
        self.label_9.setText(_translate("calibration", "X:"))
        self.four_y.setText(_translate("calibration", "72"))
        self.four_x.setText(_translate("calibration", "0"))
        self.label_10.setText(_translate("calibration", "Y:"))
        self.four_z.setText(_translate("calibration", "0"))
        self.label_11.setText(_translate("calibration", "Z:"))
        self.label_12.setText(_translate("calibration", "X:"))
        self.Button_Save.setText(_translate("calibration", "Save"))
        self.five_x.setText(_translate("calibration", "0"))
        self.five_z.setText(_translate("calibration", "0"))
        self.radioButton_five.setText(_translate("calibration", "Five"))
        self.six_z.setText(_translate("calibration", "0"))
        self.six_y.setText(_translate("calibration", "72"))
        self.label_13.setText(_translate("calibration", "X:"))
        self.label_14.setText(_translate("calibration", "Z:"))
        self.label_15.setText(_translate("calibration", "Y:"))
        self.radioButton_six.setText(_translate("calibration", "Six"))
        self.label_16.setText(_translate("calibration", "X:"))
        self.label_17.setText(_translate("calibration", "Y:"))
        self.label_18.setText(_translate("calibration", "Z:"))
        self.five_y.setText(_translate("calibration", "72"))
        self.six_x.setText(_translate("calibration", "0"))

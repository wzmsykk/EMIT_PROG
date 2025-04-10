# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(764, 722)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setMaximumSize(QtCore.QSize(99999, 300))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_kinput = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_kinput.setObjectName("lineEdit_kinput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_kinput)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_sigma2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_sigma2.setObjectName("lineEdit_sigma2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sigma2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_energy = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_energy.setObjectName("lineEdit_energy")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_energy)
        self.label_compname = QtWidgets.QLabel(self.groupBox)
        self.label_compname.setObjectName("label_compname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_compname)
        self.lineEdit_l = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_l.setObjectName("lineEdit_l")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_l)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_ld = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ld.setObjectName("lineEdit_ld")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ld)
        self.verticalLayout.addLayout(self.formLayout)
        self.frame_4 = QtWidgets.QFrame(self.groupBox)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_focus = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_focus.setChecked(True)
        self.radioButton_focus.setObjectName("radioButton_focus")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_focus)
        self.gridLayout.addWidget(self.radioButton_focus, 0, 2, 1, 1)
        self.radioButton_solenoid = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_solenoid.setObjectName("radioButton_solenoid")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_solenoid)
        self.gridLayout.addWidget(self.radioButton_solenoid, 1, 0, 1, 1)
        self.radioButton_quadmag = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_quadmag.setChecked(True)
        self.radioButton_quadmag.setObjectName("radioButton_quadmag")
        self.buttonGroup.addButton(self.radioButton_quadmag)
        self.gridLayout.addWidget(self.radioButton_quadmag, 0, 0, 1, 1)
        self.radioButton_defocus = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_defocus.setObjectName("radioButton_defocus")
        self.buttonGroup_2.addButton(self.radioButton_defocus)
        self.gridLayout.addWidget(self.radioButton_defocus, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_img = QtWidgets.QWidget(self.frame)
        self.widget_img.setMinimumSize(QtCore.QSize(200, 200))
        self.widget_img.setObjectName("widget_img")
        self.horizontalLayout.addWidget(self.widget_img)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setMaximumSize(QtCore.QSize(236, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_eps = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_eps.setFont(font)
        self.lineEdit_eps.setObjectName("lineEdit_eps")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_eps)
        self.lineEdit_alpha = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_alpha.setFont(font)
        self.lineEdit_alpha.setObjectName("lineEdit_alpha")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_alpha)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_beta = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_beta.setFont(font)
        self.lineEdit_beta.setObjectName("lineEdit_beta")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_beta)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_y = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_y)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_epsn = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_epsn.setObjectName("lineEdit_epsn")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_epsn)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 49))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pushButton_calc = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_calc.setFont(font)
        self.pushButton_calc.setObjectName("pushButton_calc")
        self.horizontalLayout_3.addWidget(self.pushButton_calc)
        self.verticalLayout_3.addWidget(self.frame_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "束流发射度计算程序"))
        self.groupBox.setTitle(_translate("Dialog", "参数输入"))
        self.label_2.setText(_translate("Dialog", "聚焦参数K"))
        self.label_3.setText(_translate("Dialog", "束斑尺寸σ2 (mm2)"))
        self.label_4.setText(_translate("Dialog", "束流能量E(MeV)"))
        self.label_compname.setText(_translate("Dialog", "透镜(Q铁)有效长度Lq(m)"))
        self.label_11.setText(_translate("Dialog", "漂移段长度(Ld)(m)"))
        self.radioButton_focus.setText(_translate("Dialog", "聚焦"))
        self.radioButton_solenoid.setText(_translate("Dialog", "螺线管"))
        self.radioButton_quadmag.setText(_translate("Dialog", "四极铁"))
        self.radioButton_defocus.setText(_translate("Dialog", "散焦"))
        self.groupBox_2.setTitle(_translate("Dialog", "计算结果"))
        self.label_5.setText(_translate("Dialog", "ε"))
        self.label_6.setText(_translate("Dialog", "α"))
        self.label_7.setText(_translate("Dialog", "β"))
        self.label_8.setText(_translate("Dialog", "Y"))
        self.label_9.setText(_translate("Dialog", "εn"))
        self.pushButton_calc.setText(_translate("Dialog", "计算"))

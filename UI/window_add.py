# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\.source\add.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddRowsWindow(object):
    def setupUi(self, RowsWindow):
        RowsWindow.setObjectName("AddRowsWindow")
        RowsWindow.resize(274, 235)
        self.centralwidget = QtWidgets.QWidget(RowsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.VBox_EditWindow_Index = QtWidgets.QVBoxLayout()
        self.VBox_EditWindow_Index.setSpacing(2)
        self.VBox_EditWindow_Index.setObjectName("VBox_EditWindow_Index")
        self.L_IndexTitle = QtWidgets.QLabel(self.centralwidget)
        self.L_IndexTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.L_IndexTitle.setObjectName("L_IndexTitle")
        self.VBox_EditWindow_Index.addWidget(self.L_IndexTitle)
        self.LE_Index = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Index.setInputMethodHints(QtCore.Qt.ImhNone)
        self.LE_Index.setClearButtonEnabled(False)
        self.LE_Index.setObjectName("LE_Index")
        self.VBox_EditWindow_Index.addWidget(self.LE_Index)
        self.gridLayout.addLayout(self.VBox_EditWindow_Index, 2, 0, 1, 1)
        self.VBox_EditWindow_Customers = QtWidgets.QVBoxLayout()
        self.VBox_EditWindow_Customers.setSpacing(2)
        self.VBox_EditWindow_Customers.setObjectName("VBox_EditWindow_Customers")
        self.L_CustomersTitle = QtWidgets.QLabel(self.centralwidget)
        self.L_CustomersTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.L_CustomersTitle.setObjectName("L_CustomersTitle")
        self.VBox_EditWindow_Customers.addWidget(self.L_CustomersTitle)
        self.LE_Customers = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Customers.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.LE_Customers.setObjectName("LE_Customers")
        self.VBox_EditWindow_Customers.addWidget(self.LE_Customers)
        self.gridLayout.addLayout(self.VBox_EditWindow_Customers, 3, 0, 1, 1)
        self.VBox_EditWindow_CityName = QtWidgets.QVBoxLayout()
        self.VBox_EditWindow_CityName.setSpacing(2)
        self.VBox_EditWindow_CityName.setObjectName("VBox_EditWindow_CityName")
        self.L_CityNameTitle = QtWidgets.QLabel(self.centralwidget)
        self.L_CityNameTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.L_CityNameTitle.setObjectName("L_CityNameTitle")
        self.VBox_EditWindow_CityName.addWidget(self.L_CityNameTitle)
        self.LE_CityName = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_CityName.setObjectName("LE_CityName")
        self.VBox_EditWindow_CityName.addWidget(self.LE_CityName)
        self.gridLayout.addLayout(self.VBox_EditWindow_CityName, 1, 0, 1, 1)
        self.VBox_EditWindow_SubjectName = QtWidgets.QVBoxLayout()
        self.VBox_EditWindow_SubjectName.setSpacing(2)
        self.VBox_EditWindow_SubjectName.setObjectName("VBox_EditWindow_SubjectName")
        self.L_SubjectNameTitle = QtWidgets.QLabel(self.centralwidget)
        self.L_SubjectNameTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.L_SubjectNameTitle.setObjectName("L_SubjectNameTitle")
        self.VBox_EditWindow_SubjectName.addWidget(self.L_SubjectNameTitle)
        self.LE_SubjectName = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_SubjectName.setObjectName("LE_SubjectName")
        self.VBox_EditWindow_SubjectName.addWidget(self.LE_SubjectName)
        self.gridLayout.addLayout(self.VBox_EditWindow_SubjectName, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        RowsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RowsWindow)
        self.statusbar.setObjectName("statusbar")
        RowsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RowsWindow)
        QtCore.QMetaObject.connectSlotsByName(RowsWindow)

    def retranslateUi(self, RowsWindow):
        _translate = QtCore.QCoreApplication.translate
        RowsWindow.setWindowTitle(_translate("AddRowsWindow", "Добавление данных"))
        self.L_IndexTitle.setText(_translate("AddRowsWindow", "Индекс"))
        self.L_CustomersTitle.setText(_translate("AddRowsWindow", "Клиенты отделения"))
        self.L_CityNameTitle.setText(_translate("AddRowsWindow", "Наименование города"))
        self.L_SubjectNameTitle.setText(_translate("AddRowsWindow", "Наименование субъекта РФ"))
        self.pushButton.setText(_translate("AddRowsWindow", "Добавить"))

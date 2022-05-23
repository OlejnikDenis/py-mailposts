# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\.source\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 729)
        MainWindow.setStyleSheet("font: 10pt \"Arial\";")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.VBox_Filters = QtWidgets.QVBoxLayout()
        self.VBox_Filters.setContentsMargins(10, 10, 10, 10)
        self.VBox_Filters.setSpacing(20)
        self.VBox_Filters.setObjectName("VBox_Filters")
        self.VBox_SubjectType = QtWidgets.QVBoxLayout()
        self.VBox_SubjectType.setSpacing(2)
        self.VBox_SubjectType.setObjectName("VBox_SubjectType")
        self.L_SubjectTypeTitle = QtWidgets.QLabel(self.centralwidget)
        self.L_SubjectTypeTitle.setObjectName("L_SubjectTypeTitle")
        self.VBox_SubjectType.addWidget(self.L_SubjectTypeTitle)
        self.checkBox_Type_AutonomousRegion = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Type_AutonomousRegion.setObjectName("checkBox_Type_AutonomousRegion")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_AutonomousRegion)
        self.checkBox_Type_AutonomousDistrict = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Type_AutonomousDistrict.setObjectName("checkBox_Type_AutonomousDistrict")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_AutonomousDistrict)
        self.checkBox_Type_FederalCity = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Type_FederalCity.setObjectName("checkBox_Type_FederalCity")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_FederalCity)
        self.checkBox_Type_Region = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Type_Region.setObjectName("checkBox_Type_Region")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_Region)
        self.checkBox_Type_Area = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Type_Area.setObjectName("checkBox_Type_Area")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_Area)
        self.checkBox_Type_Republic = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Type_Republic.setObjectName("checkBox_Type_Republic")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_Republic)
        self.VBox_Filters.addLayout(self.VBox_SubjectType)
        self.VBox_SubjectName = QtWidgets.QVBoxLayout()
        self.VBox_SubjectName.setSpacing(2)
        self.VBox_SubjectName.setObjectName("VBox_SubjectName")
        self.L_SubjectNameTitle = QtWidgets.QLabel(self.centralwidget)
        self.L_SubjectNameTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.L_SubjectNameTitle.setObjectName("L_SubjectNameTitle")
        self.VBox_SubjectName.addWidget(self.L_SubjectNameTitle)
        self.comboBox_SubjectName = QtWidgets.QLineEdit(self.centralwidget)
        self.comboBox_SubjectName.setObjectName("comboBox_SubjectName")
        self.VBox_SubjectName.addWidget(self.comboBox_SubjectName)
        self.VBox_Filters.addLayout(self.VBox_SubjectName)
        self.VBox_CityName = QtWidgets.QVBoxLayout()
        self.VBox_CityName.setSpacing(2)
        self.VBox_CityName.setObjectName("VBox_CityName")
        self.L_CityNameTitle = QtWidgets.QLabel(self.centralwidget)
        self.L_CityNameTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.L_CityNameTitle.setObjectName("L_CityNameTitle")
        self.VBox_CityName.addWidget(self.L_CityNameTitle)
        self.comboBox_CityName = QtWidgets.QLineEdit(self.centralwidget)
        self.comboBox_CityName.setObjectName("comboBox_CityName")
        self.VBox_CityName.addWidget(self.comboBox_CityName)
        self.VBox_Filters.addLayout(self.VBox_CityName)
        self.VBox_Index = QtWidgets.QVBoxLayout()
        self.VBox_Index.setSpacing(2)
        self.VBox_Index.setObjectName("VBox_Index")
        self.L_IndexTitle = QtWidgets.QLabel(self.centralwidget)
        self.L_IndexTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.L_IndexTitle.setObjectName("L_IndexTitle")
        self.VBox_Index.addWidget(self.L_IndexTitle)
        self.comboBox_Index = QtWidgets.QLineEdit(self.centralwidget)
        self.comboBox_Index.setObjectName("comboBox_Index")
        self.VBox_Index.addWidget(self.comboBox_Index)
        self.VBox_Filters.addLayout(self.VBox_Index)
        self.VBox_SearchButtons = QtWidgets.QVBoxLayout()
        self.VBox_SearchButtons.setObjectName("VBox_SearchButtons")
        self.HBox_Buttons = QtWidgets.QHBoxLayout()
        self.HBox_Buttons.setObjectName("HBox_Buttons")
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.HBox_Buttons.addWidget(self.pushButton_Reset)
        self.pushButton_Find = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Find.setObjectName("pushButton_Find")
        self.HBox_Buttons.addWidget(self.pushButton_Find)
        self.VBox_SearchButtons.addLayout(self.HBox_Buttons)
        self.VBox_Filters.addLayout(self.VBox_SearchButtons)
        self.Horizintal_Line_TOP = QtWidgets.QFrame(self.centralwidget)
        self.Horizintal_Line_TOP.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizintal_Line_TOP.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizintal_Line_TOP.setObjectName("Horizintal_Line_TOP")
        self.VBox_Filters.addWidget(self.Horizintal_Line_TOP)
        self.VBox_EditButtons = QtWidgets.QVBoxLayout()
        self.VBox_EditButtons.setContentsMargins(-1, 0, -1, -1)
        self.VBox_EditButtons.setSpacing(0)
        self.VBox_EditButtons.setObjectName("VBox_EditButtons")
        self.L_EditRow = QtWidgets.QLabel(self.centralwidget)
        self.L_EditRow.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.L_EditRow.setObjectName("L_EditRow")
        self.VBox_EditButtons.addWidget(self.L_EditRow)
        self.HBox_EditButtons = QtWidgets.QHBoxLayout()
        self.HBox_EditButtons.setContentsMargins(-1, 10, -1, -1)
        self.HBox_EditButtons.setObjectName("HBox_EditButtons")
        self.pushButton_RowAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RowAdd.setObjectName("pushButton_RowAdd")
        self.HBox_EditButtons.addWidget(self.pushButton_RowAdd)
        self.pushButton_RowEdit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RowEdit.setObjectName("pushButton_RowEdit")
        self.HBox_EditButtons.addWidget(self.pushButton_RowEdit)
        self.pushButton_RowDel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RowDel.setObjectName("pushButton_RowDel")
        self.HBox_EditButtons.addWidget(self.pushButton_RowDel)
        self.VBox_EditButtons.addLayout(self.HBox_EditButtons)
        self.VBox_Filters.addLayout(self.VBox_EditButtons)
        self.Horizintal_Line_BOTTOM = QtWidgets.QFrame(self.centralwidget)
        self.Horizintal_Line_BOTTOM.setFrameShape(QtWidgets.QFrame.HLine)
        self.Horizintal_Line_BOTTOM.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Horizintal_Line_BOTTOM.setObjectName("Horizintal_Line_BOTTOM")
        self.VBox_Filters.addWidget(self.Horizintal_Line_BOTTOM)
        self.VBox_Stats = QtWidgets.QVBoxLayout()
        self.VBox_Stats.setContentsMargins(0, 0, 0, 0)
        self.VBox_Stats.setSpacing(3)
        self.VBox_Stats.setObjectName("VBox_Stats")
        self.LE_Stats_UniqueSubjects = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Stats_UniqueSubjects.setEnabled(True)
        self.LE_Stats_UniqueSubjects.setFrame(True)
        self.LE_Stats_UniqueSubjects.setReadOnly(True)
        self.LE_Stats_UniqueSubjects.setObjectName("LE_Stats_UniqueSubjects")
        self.VBox_Stats.addWidget(self.LE_Stats_UniqueSubjects)
        self.LE_Stats_Mailposts = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Stats_Mailposts.setEnabled(True)
        self.LE_Stats_Mailposts.setReadOnly(True)
        self.LE_Stats_Mailposts.setObjectName("LE_Stats_Mailposts")
        self.VBox_Stats.addWidget(self.LE_Stats_Mailposts)
        self.LE_Stats_Customers = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Stats_Customers.setEnabled(True)
        self.LE_Stats_Customers.setFrame(True)
        self.LE_Stats_Customers.setReadOnly(True)
        self.LE_Stats_Customers.setObjectName("LE_Stats_Customers")
        self.VBox_Stats.addWidget(self.LE_Stats_Customers)
        self.LE_Stats_Cities = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Stats_Cities.setEnabled(True)
        self.LE_Stats_Cities.setFrame(True)
        self.LE_Stats_Cities.setReadOnly(True)
        self.LE_Stats_Cities.setObjectName("LE_Stats_Cities")
        self.VBox_Stats.addWidget(self.LE_Stats_Cities)
        self.LE_Stats_AvgCustomers = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Stats_AvgCustomers.setEnabled(True)
        self.LE_Stats_AvgCustomers.setFrame(True)
        self.LE_Stats_AvgCustomers.setReadOnly(True)
        self.LE_Stats_AvgCustomers.setObjectName("LE_Stats_AvgCustomers")
        self.VBox_Stats.addWidget(self.LE_Stats_AvgCustomers)
        self.VBox_Filters.addLayout(self.VBox_Stats)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.VBox_Filters.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.VBox_Filters)
        self.Vertical_Line = QtWidgets.QFrame(self.centralwidget)
        self.Vertical_Line.setLineWidth(1)
        self.Vertical_Line.setMidLineWidth(0)
        self.Vertical_Line.setFrameShape(QtWidgets.QFrame.VLine)
        self.Vertical_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Vertical_Line.setObjectName("Vertical_Line")
        self.horizontalLayout.addWidget(self.Vertical_Line)
        self.VBox_Table = QtWidgets.QVBoxLayout()
        self.VBox_Table.setObjectName("VBox_Table")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.VBox_Table.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.VBox_Table)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.MenuBar_Login = QtWidgets.QAction(MainWindow)
        self.MenuBar_Login.setObjectName("MenuBar_Login")
        self.MenuBar_Exit = QtWidgets.QAction(MainWindow)
        self.MenuBar_Exit.setObjectName("MenuBar_Exit")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.MenuBar_Login)
        self.menu.addSeparator()
        self.menu.addAction(self.MenuBar_Exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Почтовые отделения РФ"))
        self.L_SubjectTypeTitle.setText(_translate("MainWindow", "Тип субъекта РФ"))
        self.checkBox_Type_AutonomousRegion.setText(_translate("MainWindow", "Автономная область"))
        self.checkBox_Type_AutonomousDistrict.setText(_translate("MainWindow", "Автономный округ"))
        self.checkBox_Type_FederalCity.setText(_translate("MainWindow", "Город федерального значения"))
        self.checkBox_Type_Region.setText(_translate("MainWindow", "Край"))
        self.checkBox_Type_Area.setText(_translate("MainWindow", "Область"))
        self.checkBox_Type_Republic.setText(_translate("MainWindow", "Республика"))
        self.L_SubjectNameTitle.setText(_translate("MainWindow", "Наименование субъекта РФ"))
        self.L_CityNameTitle.setText(_translate("MainWindow", "Наименование города"))
        self.L_IndexTitle.setText(_translate("MainWindow", "Индекс"))
        self.pushButton_Reset.setText(_translate("MainWindow", "Сбросить"))
        self.pushButton_Find.setText(_translate("MainWindow", "Найти"))
        self.L_EditRow.setText(_translate("MainWindow", "Редактирование данных"))
        self.pushButton_RowAdd.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_RowEdit.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_RowDel.setText(_translate("MainWindow", "Удалить"))
        self.LE_Stats_UniqueSubjects.setText(_translate("MainWindow", "Уникальных субъектов: 3"))
        self.LE_Stats_Mailposts.setText(_translate("MainWindow", "Почтовых отделений: 6"))
        self.LE_Stats_Customers.setText(_translate("MainWindow", "Количество клиентов: 2213"))
        self.LE_Stats_Cities.setText(_translate("MainWindow", "Населённых пунктов: 4"))
        self.LE_Stats_AvgCustomers.setText(_translate("MainWindow", "Ср. количество клиентов: 368"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Субъект"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Населённый пункт"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Индекс"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Количество клиентов"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.MenuBar_Login.setText(_translate("MainWindow", "Вход как администратор"))
        self.MenuBar_Exit.setText(_translate("MainWindow", "Выйти"))
        self.action_3.setText(_translate("MainWindow", "О программе"))

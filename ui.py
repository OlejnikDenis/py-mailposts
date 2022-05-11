from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow


class WindowMain(QMainWindow):
    def __init__(self):
        super(WindowMain, self).__init__()

        self.setWindowTitle("Почтовые отделения РФ")
        self.setGeometry(480, 360, 900, 600)
        self.setStyleSheet("font: 10pt \"Arial\";")

        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(0, 0, 900, 600)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        """ Generates left side: Filters """
        self.VBox_Filters = QtWidgets.QVBoxLayout()
        self.VBox_Filters.setContentsMargins(10, 10, 10, 10)
        self.VBox_Filters.setSpacing(20)

        """ Generates Subject type"""
        self.VBox_SubjectType = QtWidgets.QVBoxLayout()
        self.VBox_SubjectType.setSpacing(2)
        self.L_SubjectNameTitle = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.L_SubjectNameTitle.setText("Тип субъекта РФ")
        self.VBox_SubjectType.addWidget(self.L_SubjectNameTitle)

        self.checkBox_Type_AutonomousRegion = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_Type_AutonomousRegion.setText("Автономная область")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_AutonomousRegion)

        self.checkBox_Type_AutonomousDistrict = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_Type_AutonomousDistrict.setText("Автономный округ")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_AutonomousDistrict)

        self.checkBox_Type_FederalCity = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_Type_FederalCity.setText("Город федерального значения")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_FederalCity)

        self.checkBox_Type_Region = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_Type_Region.setText("Край")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_Region)

        self.checkBox_Type_Area = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_Type_Area.setText("Область")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_Area)

        self.checkBox_Type_Republic = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_Type_Republic.setText("Республика")
        self.VBox_SubjectType.addWidget(self.checkBox_Type_Republic)

        self.VBox_Filters.addLayout(self.VBox_SubjectType)

        """ Generates Subject name"""
        self.VBox_SubjectName = QtWidgets.QVBoxLayout()
        self.VBox_SubjectName.setSpacing(2)

        self.L_SubjectNameTitle = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.L_SubjectNameTitle.setText("Наименование субъекта РФ")
        self.VBox_SubjectName.addWidget(self.L_SubjectNameTitle)

        self.comboBox_SubjectName = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_SubjectName.setEditable(True)
        self.comboBox_SubjectName.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAlphabetically)
        self.VBox_SubjectName.addWidget(self.comboBox_SubjectName)

        self.VBox_Filters.addLayout(self.VBox_SubjectName)

        """ Generates City name"""
        self.VBox_CityName = QtWidgets.QVBoxLayout()
        self.VBox_CityName.setSpacing(2)

        self.L_CityNameTitle = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.L_CityNameTitle.setText("Наименование города")
        self.VBox_CityName.addWidget(self.L_CityNameTitle)

        self.comboBox_CityName = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_CityName.setEditable(True)
        self.comboBox_CityName.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAlphabetically)
        self.VBox_CityName.addWidget(self.comboBox_CityName)

        self.VBox_Filters.addLayout(self.VBox_CityName)

        """ Generates buttons"""
        self.VBox_Buttons = QtWidgets.QVBoxLayout()
        self.VBox_Buttons = QtWidgets.QVBoxLayout()
        self.HBox_Buttons = QtWidgets.QHBoxLayout()

        self.pushButton_Reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Reset.setText("Сбросить")
        self.HBox_Buttons.addWidget(self.pushButton_Reset)

        self.pushButton_Find = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Find.setText("Найти")
        self.HBox_Buttons.addWidget(self.pushButton_Find)

        self.VBox_Buttons.addLayout(self.HBox_Buttons)
        self.VBox_Filters.addLayout(self.VBox_Buttons)

        """ Spacer"""
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.VBox_Filters.addItem(spacerItem)

        self.horizontalLayout.addLayout(self.VBox_Filters)

        """ Vertical line btw filters and table"""
        self.vertilal_line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.vertilal_line.setLineWidth(1)
        self.vertilal_line.setMidLineWidth(0)
        self.vertilal_line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.vertilal_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.horizontalLayout.addWidget(self.vertilal_line)

        """ Data table on right side of app"""
        self.VBox_Table = QtWidgets.QVBoxLayout()
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)

        item = QtWidgets.QTableWidgetItem()
        item.setText("ID")
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Название")
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("...")
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.VBox_Table.addWidget(self.tableWidget)

        self.horizontalLayout.addLayout(self.VBox_Table)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 5)

        """Menu bar"""
        self.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setTitle("Меню")
        self.setMenuBar(self.menubar)

        self.MenuBar_Login = QtGui.QAction(self)
        self.MenuBar_Login.setText("Вход как администратор")

        self.MenuBar_Exit = QtGui.QAction(self)
        self.MenuBar_Exit.setText("Выход")

        self.MenuBar_About = QtGui.QAction(self)
        self.MenuBar_About.setText("О Программе")

        self.menu.addAction(self.MenuBar_Login)
        # self.menu.addAction("self.MenuBar_Login", self.action_clicked)
        self.menu.addSeparator()
        self.menu.addAction(self.MenuBar_Exit)
        self.menubar.addAction(self.menu.menuAction())


class WindowAuth(QMainWindow):
    def __init__(self):
        super(WindowAuth, self).__init__()

        self._WINDOW_SIZE_X: int = 260
        self._WINDOW_SIZE_Y: int = 180
        self._WINDOW_NAME: str = "Авторизация"

        self.resize(self._WINDOW_SIZE_X, self._WINDOW_SIZE_Y)
        self.setStyleSheet("font: 10pt \"Arial\";")
        self.setWindowTitle(self._WINDOW_NAME)

        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0,
                                                             self._WINDOW_SIZE_X,
                                                             self._WINDOW_SIZE_Y))

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)

        self.VB_AuthInputs = QtWidgets.QVBoxLayout()

        self.VB_LoginData = QtWidgets.QVBoxLayout()
        self.VB_LoginData.setSpacing(2)

        self.L_LoginInputTitle = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.L_LoginInputTitle.setText("Логин")

        self.Input_Login = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Input_Login.setPlaceholderText("Login")

        self.VB_LoginData.addWidget(self.L_LoginInputTitle)
        self.VB_LoginData.addWidget(self.Input_Login)

        self.VB_AuthInputs.addLayout(self.VB_LoginData)

        self.VB_PassData = QtWidgets.QVBoxLayout()
        self.VB_PassData.setSpacing(2)

        self.L_PassInputTitle = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.L_PassInputTitle.setText("Пароль")

        self.Input_Pass = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Input_Pass.setPlaceholderText("Password")
        self.Input_Pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.VB_PassData.addWidget(self.L_PassInputTitle)
        self.VB_PassData.addWidget(self.Input_Pass)
        self.VB_AuthInputs.addLayout(self.VB_PassData)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setText("Вход")

        self.VB_AuthInputs.addWidget(self.pushButton)
        self.VB_AuthInputs.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.VB_AuthInputs)
        self.setCentralWidget(self.centralWidget)

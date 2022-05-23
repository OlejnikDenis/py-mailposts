import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from loguru import logger

import UI
import UI.window_edit
from database import Database


# TODO: Реализовать статы для текущей таблицы
# TODO: Реализовать добавление/удаление строк таблицы

# query = """SELECT master_unit.name, cities.name, office_index, customers
#             FROM master_unit,
#             INNER JOIN cities ON master_unit.id = cities.master_id
#             INNER JOIN post_offices ON master_unit.id = post_offices"""
# data = self.database.execute_read_query(query)
#
# def get_subject_fullnames(self):
#     query = """SELECT master_unit.name, subject_types.name
#                 FROM master_unit
#                 INNER JOIN subject_types ON master_unit.type = subject_types.id;"""
#     data = self.database.execute_read_query(query)
#
#     for item, row_data in enumerate(data):
#         data[item] = f"{row_data[0]} {row_data[1]}"
#     return data


class CurrentSession:
    def __init__(self):
        """
        This class is a simplified tokenized session system for authorized users.
        """
        logger.info('User session initialized')
        self.UserName = None
        self.bUserAuthorized = False


class RowsWindow(QtWidgets.QMainWindow, UI.Ui_RowsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class AuthWindow(QtWidgets.QMainWindow, UI.Ui_AuthWindow):
    def __init__(self):
        """
        This class implements the user authorization window in the system.
        """
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.validate_auth_data)


    def validate_auth_data(self):
        login = self.Input_Login.text()
        password = self.Input_Pass.text()

        query = f'SELECT * FROM users WHERE login="{login}" AND password="{password}";'
        data = database.execute_read_query(query)

        if data:
            # If the authorization was successful, store the data in the current session
            logger.info(f'User ({data[0][0]}) is successfully logged on!')

            session.bUserAuthorized = True
            session.UserName = data[0][0]

            self.close()
        else:
            logger.error('User authorization error!')
            session.bUserAuthorized = False

            # TODO: Отобразить сообщение (окно) с ошибкой авторизации

    def keyPressEvent(self, event) -> None:
        """Extending the method for simplified authorization"""
        # modifiers = QtWidgets.QApplication.keyboardModifiers()

        # if modifiers == (QtCore.Qt.KeyboardModifier.ShiftModifier | QtCore.Qt.Key.Key_Return):
        #     logger.info('shift enter')

        if event.key() == QtCore.Qt.Key.Key_Return:
            self.validate_auth_data()
            event.accept()


class MainWindow(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        logger.debug('New window: Main')
        super().__init__()
        self.setupUi(self)

        # Set tableWidget:
        self.tableWidget.setColumnWidth(0, 175)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 75)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setSortingEnabled(True)

        # Bind buttons:
        # auth:
        self.MenuBar_Login.triggered.connect(self.menubar_auth)
        self.MenuBar_Exit.triggered.connect(self.menubar_exit)

        # filters:
        self.checkBox_Type_AutonomousRegion.toggled.connect(self.get_active_filters)
        self.checkBox_Type_AutonomousDistrict.toggled.connect(self.get_active_filters)
        self.checkBox_Type_FederalCity.toggled.connect(self.get_active_filters)
        self.checkBox_Type_Region.toggled.connect(self.get_active_filters)
        self.checkBox_Type_Area.toggled.connect(self.get_active_filters)
        self.checkBox_Type_Republic.toggled.connect(self.get_active_filters)

        self.pushButton_Find.clicked.connect(self.search_by_filters)
        self.pushButton_Reset.clicked.connect(self.search_reset)

        # rows:
        self.pushButton_RowAdd.clicked.connect(self.add_row)
        self.pushButton_RowEdit.clicked.connect(self.edit_row)
        # self.pushButton_RowDel.clicked.connect(self.delete_row)

        # Basic calls:
        self.table_widget_init()

        self.filters = dict()

    def get_active_filters(self) -> dict:
        self.filters['check_AutonomousRegion'] = self.checkBox_Type_AutonomousRegion.isChecked()
        self.filters['check_AutonomousDistrict'] = self.checkBox_Type_AutonomousDistrict.isChecked()
        self.filters['check_FederalCity'] = self.checkBox_Type_FederalCity.isChecked()
        self.filters['check_Region'] = self.checkBox_Type_Region.isChecked()
        self.filters['check_Area'] = self.checkBox_Type_Area.isChecked()
        self.filters['check_Republic'] = self.checkBox_Type_Republic.isChecked()

        # self.filters['SubjectName'] = self.comboBox_SubjectName.currentText()
        self.filters['SubjectName'] = self.comboBox_SubjectName.text()
        self.filters['CityName'] = self.comboBox_CityName.text()
        self.filters['Zipcode'] = self.comboBox_Index.text()

        return self.filters

    def search_by_filters(self):
        # TODO: Исправить баг в логике поиска по БД (если есть и индекс и название города, то находится город)
        # TODO: Исправить баг с поиском по чекбоксам: 'область' находится и в параметре 'автономная 'область'
        # TODO: Исправить баг: если выделить все галки, то TableWidget будет пустым. Ожидались ВСЕ строки.
        #                       Вероятно, необходимо заменить 'and' на 'or' при поиске по чекбоксам

        self.get_active_filters()
        params = list()
        if self.filters['check_AutonomousRegion']:
            params.append(f"instr(subject_name, 'автономная')")

        if self.filters['check_AutonomousDistrict']:
            params.append(f"instr(subject_name, 'округ')")

        if self.filters['check_FederalCity']:
            params.append(f"instr(subject_name, 'федерального')")

        if self.filters['check_Region']:
            params.append(f"instr(subject_name, 'край')")

        if self.filters['check_Area']:
            params.append(f"instr(subject_name, 'область')")

        if self.filters['check_Republic']:
            params.append(f"(instr(subject_name, 'республика') OR instr(subject_name, 'Республика'))")

        if self.filters['SubjectName']:
            params.append(f"instr(subject_name, '{self.filters['SubjectName'].capitalize()}') OR instr(subject_name, '{self.filters['SubjectName'].lower()}')")
        if self.filters['CityName']:
            params.append(f"instr(city_name, '{self.filters['CityName'].capitalize()}') OR instr(city_name, '{self.filters['CityName'].lower()}')")
        if self.filters['Zipcode']:
            params.append(f"instr(zipcode, '{self.filters['Zipcode']}')")

        result = [' AND '] * (len(params) * 2 - 1)
        result[0::2] = params

        query = f"SELECT * FROM mailposts WHERE {''.join(result)};"
        data = database.execute_read_query_dict(query)
        self.table_widget_update(data)

    def search_reset(self):
        self.checkBox_Type_AutonomousRegion.setChecked(False)
        self.checkBox_Type_AutonomousDistrict.setChecked(False)
        self.checkBox_Type_FederalCity.setChecked(False)
        self.checkBox_Type_Region.setChecked(False)
        self.checkBox_Type_Area.setChecked(False)
        self.checkBox_Type_Republic.setChecked(False)

        self.comboBox_SubjectName.setText('')
        self.comboBox_CityName.setText('')
        self.comboBox_Index.setText('')

        self.get_active_filters()
        self.table_widget_init()

    def add_row(self):
        if session.bUserAuthorized:
            logger.debug("New window: RowsWindow")
            self.RowsWindow = RowsWindow()
            self.RowsWindow.show()

        else:
            logger.warning('You are not logged in.')

    def edit_row(self):
        if session.bUserAuthorized:
            logger.debug('edit row')
        else:
            logger.warning('You are not logged in.')

    def menubar_auth(self):
        """Called when 'Login as administrator' is pressed"""
        logger.debug("New window: Authorization")
        self.AuthWindow = AuthWindow()
        self.AuthWindow.show()

    def menubar_exit(self):
        """Called when 'Exit' is pressed"""
        logger.info("'Exit' button triggered!")
        sys.exit()

    def update_stats(self, data):
        _UniqueSubjects = 'Уникальных субъектов: '
        _Mailposts = "Почтовых отделений: "
        _Customers = "Количество клиентов: "
        _Cities = "Населённых пунктов: "
        _AvgCustomers = "Ср. количество клиентов: "

        self._UniqueSubjects_list = list(({item['subject_name']: item for item in data}.values()))
        self._Mailposts_list = list(({item['zipcode']: item for item in data}.values()))
        self._Customers_value = 0
        for row in data:
            self._Customers_value += row['customers']

        self._Cities_list = list(({item['city_name']: item for item in data}.values()))

        self._UniqueSubjects_value = len(self._UniqueSubjects_list)
        self._Mailposts_value = len(self._Mailposts_list)
        self._Cities_value = len(self._Cities_list)
        if self._Mailposts_value:
            self._AvgCustomers_value = self._Customers_value / self._Mailposts_value
        else:
            self._AvgCustomers_value = 0
            
        self.LE_Stats_UniqueSubjects.setText(_UniqueSubjects + str(self._UniqueSubjects_value))
        self.LE_Stats_Mailposts.setText(_Mailposts + str(self._Mailposts_value))
        self.LE_Stats_Customers.setText(_Customers + str(self._Customers_value))
        self.LE_Stats_Cities.setText(_Cities + str(self._Cities_value))
        self.LE_Stats_AvgCustomers.setText(_AvgCustomers + str(int(self._AvgCustomers_value)))

    def table_widget_update(self, data: list):
        self.tableWidget.setRowCount(len(data))

        for row_num, row in enumerate(data):
            item_index = QtWidgets.QTableWidgetItem()
            item_index.setData(Qt.EditRole, int(row['zipcode']))
            item_customers = QtWidgets.QTableWidgetItem()
            item_customers.setData(Qt.EditRole, int(row['customers']))

            self.tableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(row['subject_name']))
            self.tableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(row['city_name']))
            self.tableWidget.setItem(row_num, 2, item_index)
            self.tableWidget.setItem(row_num, 3, item_customers)

        logger.debug('TableWidget updated!')
        self.update_stats(data)

    def table_widget_init(self):
        data = database.execute_read_query_dict('SELECT * FROM mailposts')
        self.table_widget_update(data)

        logger.info('TableWidget is successfully initialized')


if __name__ == '__main__':
    logger.start("log.txt")
    logger.info("Application started!")

    app = QtWidgets.QApplication([])
    session = CurrentSession()
    database = Database()

    StartWindow = MainWindow()
    StartWindow.show()

    sys.exit(app.exec())


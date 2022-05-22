import sys


from database import Database

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
import UI

from loguru import logger


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
            logger.info('enter')
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
        self.pushButton_RowDel.clicked.connect(self.delete_row)

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

        self.filters['SubjectName'] = self.comboBox_SubjectName.currentText()
        self.filters['CityName'] = self.comboBox_CityName.currentText()
        self.filters['Zipcode'] = self.comboBox_Index.currentText()

        return self.filters

    def search_by_filters(self):
        self.get_active_filters()

        query = f"""SELECT * FROM mailposts WHERE zipcode = {self.filters['Zipcode']}"""
        data = database.execute_read_query_dict(query)
        self.table_widget_update(data)

    def search_reset(self):
        self.checkBox_Type_AutonomousRegion.setChecked(False)
        self.checkBox_Type_AutonomousDistrict.setChecked(False)
        self.checkBox_Type_FederalCity.setChecked(False)
        self.checkBox_Type_Region.setChecked(False)
        self.checkBox_Type_Area.setChecked(False)
        self.checkBox_Type_Republic.setChecked(False)

        self.comboBox_SubjectName.setCurrentText('')
        self.comboBox_CityName.setCurrentText('')
        self.comboBox_Index.setCurrentText('')

        self.get_active_filters()
        self.table_widget_init()

    def add_row(self):
        # self.filters.get()
        if session.bUserAuthorized:
            logger.debug('add row')
        else:
            logger.warning('You are not logged in.')

    def edit_row(self):
        if session.bUserAuthorized:
            logger.debug('edit row')
        else:
            logger.warning('You are not logged in.')

    def delete_row(self):
        if session.bUserAuthorized:
            logger.debug('delete row')
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





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


class Filters(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cb_Type_AutonomousRegion = self.checkBox_Type_AutonomousRegion.isChecked()
        self.cb_Type_AutonomousDistrict = self.checkBox_Type_AutonomousDistrict.isChecked()
        self.cb_Type_FederalCity = self.checkBox_Type_FederalCity.isChecked()
        self.cb_Type_Region = self.checkBox_Type_Region.isChecked()
        self.cb_Type_Area = self.checkBox_Type_Area.isChecked()
        self.cb_Type_Republic = self.checkBox_Type_Republic.isChecked()

        self.comboBox_SubjectName = self.comboBox_SubjectName.currentText()


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
        self.filters = Filters()

        # Set tableWidget:
        self.tableWidget.setColumnWidth(0, 175)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 75)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setSortingEnabled(True)

        # Bind buttons:
        self.MenuBar_Login.triggered.connect(self.menubar_auth)
        self.MenuBar_Exit.triggered.connect(self.menubar_exit)
        self.pushButton_RowAdd.clicked.connect(self.add_row)
        self.pushButton_RowEdit.clicked.connect(self.edit_row)
        self.pushButton_RowDel.clicked.connect(self.delete_row)

        # Basic calls:
        self.init_tableWidget()


    def add_row(self):
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

    def get_mailposts_count(self) -> int:
        return int(database.execute_read_query("SELECT COUNT() FROM mailposts")[0][0])

    def init_tableWidget(self):
        self.tableWidget.setRowCount(self.get_mailposts_count())
        data = database.execute_read_query_dict('SELECT * FROM mailposts')

        for row in data:
            item_index = QtWidgets.QTableWidgetItem()
            item_index.setData(Qt.EditRole, int(row['index']))
            item_customers = QtWidgets.QTableWidgetItem()
            item_customers.setData(Qt.EditRole, int(row['customers']))

            self.tableWidget.setItem(row['id']-1, 0, QtWidgets.QTableWidgetItem(row['subject_name']))
            self.tableWidget.setItem(row['id']-1, 1, QtWidgets.QTableWidgetItem(row['city_name']))
            self.tableWidget.setItem(row['id']-1, 2, item_index)
            self.tableWidget.setItem(row['id']-1, 3, item_customers)

        logger.info('TableWidget is successfully loaded')


if __name__ == '__main__':
    logger.start("log.txt")
    logger.info("Application started!")

    app = QtWidgets.QApplication([])
    session = CurrentSession()
    database = Database()

    StartWindow = MainWindow()
    StartWindow.show()

    sys.exit(app.exec())





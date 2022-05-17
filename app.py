import sys

import database
from database import Database

from PyQt5 import QtWidgets
import UI

from loguru import logger


class AuthWindow(QtWidgets.QMainWindow, UI.Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.validate_auth_data)

        self.database = Database()


    def validate_auth_data(self):
        login = self.Input_Login.text()
        password = self.Input_Pass.text()

        query = f'SELECT * FROM users WHERE login="{login}" AND password="{password}";'
        data = self.database.execute_read_query(query)
        if data:
            logger.warning(data)





class MainWindow(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Bind buttons:
        self.MenuBar_Login.triggered.connect(self.menubar_auth)
        self.MenuBar_Exit.triggered.connect(self.menubar_exit)

    def menubar_auth(self):
        logger.info("'Login' button triggered!")
        self.AuthWindow = AuthWindow()
        self.AuthWindow.show()

    def menubar_exit(self):
        logger.info("'Exit' button triggered!")
        sys.exit()



if __name__ == '__main__':
    # start_time = time.time()

    app = QtWidgets.QApplication([])
    StartWindow = MainWindow()
    StartWindow.show()

    # logger.info(f'Program finished in {int(start_time-time.time())} s.')

    sys.exit(app.exec())





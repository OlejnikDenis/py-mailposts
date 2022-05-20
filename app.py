import sys

from database import Database

from PyQt5 import QtWidgets, QtCore
import UI

from loguru import logger


class CurrentSession:

    def __init__(self):
        """
        This class is a simplified tokenized session system for authorized users.
        """
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

        self.database = Database()


    def validate_auth_data(self):
        login = self.Input_Login.text()
        password = self.Input_Pass.text()

        query = f'SELECT * FROM users WHERE login="{login}" AND password="{password}";'
        data = self.database.execute_read_query(query)

        if data:
            # If the authorization was successful, store the data in the current session
            logger.info(f'User ({data[0][0]}) is successfully logged on!')

            session.bUserAuthorized = True
            session.UserName = data[0][0]

            self.close()
        else:
            logger.warning('User authorization error!')
            session.bUserAuthorized = False

            # TODO: Отобразить сообщение (окно) с ошибкой авторизации

    def keyPressEvent(self, event) -> None:
        """Extending the method for simplified authorization"""
        if event.key() == QtCore.Qt.Key.Key_Return:
            self.validate_auth_data()
        event.accept()


class MainWindow(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Bind buttons:
        self.MenuBar_Login.triggered.connect(self.menubar_auth)
        self.MenuBar_Exit.triggered.connect(self.menubar_exit)

    def menubar_auth(self):
        """Called when 'Login as administrator' is pressed"""
        logger.info("'Login' button triggered!")
        self.AuthWindow = AuthWindow()
        self.AuthWindow.show()

    def menubar_exit(self):
        """Called when 'Exit' is pressed"""
        logger.info("'Exit' button triggered!")
        sys.exit()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    session = CurrentSession()

    StartWindow = MainWindow()
    StartWindow.show()

    sys.exit(app.exec())





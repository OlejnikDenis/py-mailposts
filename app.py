import sys

from PyQt5 import QtWidgets
import UI



class AuthWindow(UI.Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def user_auth(self):
        pass


class MainWindow(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Bind buttons:
        self.MenuBar_Login.triggered.connect(self.menubar_auth)
        self.MenuBar_Exit.triggered.connect(self.menubar_exit)

    def menubar_auth(self):
        print('login')

    def menubar_exit(self):
        print('exit')



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    StartWindow = MainWindow()
    StartWindow.show()

    sys.exit(app.exec())



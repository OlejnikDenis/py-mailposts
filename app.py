from PyQt6.QtWidgets import QApplication

from ui import WindowMain, WindowAuth
import sys


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = WindowMain()
        self.window2 = WindowAuth()

        self.window.show()
        self.window2.show()

        sys.exit(self.app.exec())


def main():
    app = Application()


if __name__ == '__main__':
    main()


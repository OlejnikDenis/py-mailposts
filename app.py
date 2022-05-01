import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget,
    QToolBar)
from PyQt6.QtGui import QPalette, QColor, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Mailposts of Russian Federation")
        self.setFixedSize(QSize(800, 600))

        page_layout = QHBoxLayout()
        filters_layout = QVBoxLayout()

        # Creates and add filters layout
        filters_layout.addWidget(Color('yellow'))
        filters_layout.addWidget(Color('black'))
        page_layout.addLayout(filters_layout)
        page_layout.setSpacing(4)
        # page_layout.setContentsMargins(60, 0, 0, 20)

        # Creates and add main page layout
        page_layout.addWidget(Color('Green'))
        page_layout.addLayout(page_layout)

        # Create tabs
        # tabs = QTabWidget()
        # tabs.setTabPosition(QTabWidget.TabPosition.East)
        # tabs.setMovable(True)
        #
        # for n, color in enumerate(["red", "green", "blue", "yellow"]):
        #     tabs.addTab(Color(color), color)
        #
        # self.setCentralWidget(tabs)

        toolbar = QToolBar("My toolbar")
        self.addToolBar(toolbar)
        button_action = QAction("Button 1", self)
        button_action.setStatusTip("This is button 1")
        button_action.triggered.connect(self.clicked_on_toolbar_btn)
        toolbar.addAction(button_action)
        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def clicked_on_toolbar_btn(self, s):
        print("click", s)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
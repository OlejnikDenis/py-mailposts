from PyQt6.QtWidgets import QApplication

from ui import WindowMain, WindowAuth
import sys
import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("mailposts.db")
        self.cursor = self.connection.cursor()

    def execute_read_query(self, query: str) -> list:
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()

            print(f"Request \"{query}\" executed successfully!")
            return data

        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection:
                self.connection.close()




class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.database = Database()
        self.window = WindowMain()

        self.window.show()

        sys.exit(self.app.exec())


def main():
    app = Application()

if __name__ == '__main__':
    main()


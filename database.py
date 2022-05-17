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

    def execute_write_query(self, query: str):
        pass

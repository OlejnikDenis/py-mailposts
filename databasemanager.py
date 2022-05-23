import sqlite3
from loguru import logger


class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect("mailposts.db")
        self.cursor = self.connection.cursor()
        logger.info('Connection to database is established')

    def execute_read_query(self, query: str) -> list:
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data

        except sqlite3.Error as error:
            logger.exception(error)


    def execute_write_query(self, query: str):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as err:
            logger.exception(err)

    def execute_read_query_dict(self, query: str) -> list:
        try:
            self.cursor.execute(query)
            description = self.cursor.description

            column_names = [col[0] for col in description]
            data = [dict(zip(column_names, row)) for row in self.cursor.fetchall()]
            return data
        except sqlite3.Error as err:
            logger.exception(err)
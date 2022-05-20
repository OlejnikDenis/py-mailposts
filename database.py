import sqlite3
from loguru import logger


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("mailposts.db")
        self.cursor = self.connection.cursor()

    def execute_read_query(self, query: str) -> list:
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            logger.debug(f"Request \"{query}\" executed successfully!")
            return data

        except sqlite3.Error as error:
            logger.exception(error)


    def execute_write_query(self, query: str):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            logger.debug(f"Request \"{query}\" executed successfully!")
        except sqlite3.Error as err:
            logger.exception(err)

    # def dict_factory(self, row):
    #     dictionary = dict()
    #
    #     for id, col in enumerate(self.cursor.description):
    #         dictionary[col[0]] = row[id]
    #
    #     return dictionary

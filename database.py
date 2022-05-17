import sqlite3
from loguru import logger


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("mailposts.db")
        self.cursor = self.connection.cursor()

        try:
            pass
            # Create users table:
            # table_users = """
            # CREATE TABLE IF NOT EXISTS users (
            # login VARCHAR(255) NOT NULL PRIMARY KEY,
            # password VARCHAR(255) NOT NULL);
            # """
            # self.connection.execute(table_users)
            # self.connection.commit()

        except sqlite3.Error as err:
            logger.exception(err)

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


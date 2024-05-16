import datetime
import textwrap
from decimal import Decimal

from mysql.connector import connection
from test_suite.src.utilities.logger import Logger
from test_suite.src.Constants.constant import Constant


class MysqlHelper:

    @staticmethod
    def db_connect(self):
        try:
            Logger.log("Connection getting established")
            self.conn = connection.MySQLConnection(
                **Constant.config['db_config'])
            Logger.log("Connection DB established")
            return self.conn.cursor()
        except Exception as e:
            Logger.log("Failed to connection establishment: ", e)

    @staticmethod
    def execute_query(self, query: str) -> list:
        try:
            self.cursor = MysqlHelper.db_connect(self)
            Logger.log(f"Executing DB Query: {query}")
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            column_names = [list(self.cursor.column_names)]
            return MysqlHelper.construct_db_output(column_names, result)
        except Exception as e:
            Logger.log(f"Query Execution Failed: {e}")
        finally:
            self.cursor.close()
            Logger.log("Connection Closed")

    @staticmethod
    def construct_db_output(fieldNames, dbOutput) -> list:
        output = []
        for key, value in zip(fieldNames, dbOutput):
            row = {}
            for k, v in zip(key, value):
                if isinstance(v, Decimal):
                    v = str(v)
                elif isinstance(v, datetime.datetime):
                    v = str(v)
                row.update({k: v})
            output.append(row)
        Logger.log("Output of DB query : ", textwrap.fill(repr(output), width=1000))
        return output

from typing import Optional
import time
import datetime
from test_suite.src.services.mysql_helper import MysqlHelper


class RequestsDatabaseQuery:

    def get_requests_database_results(self, table: str, condition: str = None) -> list:
        query = f"SELECT * from rewards.{table}"
        if condition is not None:
            query = f"{query} where {condition}"
        else:
            query = f"{query} order by id DESC limit 1"
        return MysqlHelper.execute_query(self, query)


    @staticmethod
    def get_users_table_result(self, condition: str = None) -> list:
        return RequestsDatabaseQuery.get_requests_database_results(self, "users", condition)


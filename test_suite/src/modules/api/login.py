import pdb

from test_suite.src.Constants.constant import Constant
from test_suite.src.services.api_helper import ApiHelper


class Login:

    @staticmethod
    def login_payload(payload: dict = None) -> dict:
        tmp_dict = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        if payload is not None:
            tmp_dict.update(payload)
        return tmp_dict

    @staticmethod
    def login(email: str, password: str) -> dict:
        url = f"{Constant.base_url}{Constant.endpoints['login']}"
        return ApiHelper.make_request(url, 'POST', {"email": email, "password": password})

    @staticmethod
    def get_users(self, page_limit: int = 2) -> dict:
        url = f"{Constant.base_url}{Constant.endpoints['users']}?page={page_limit}"
        return ApiHelper.make_request(url , 'GET')



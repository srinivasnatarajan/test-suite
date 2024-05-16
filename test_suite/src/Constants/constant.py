import os
from test_suite.src.Constants.credentials import Credentials
from test_suite.src.Constants.endpoints import APIEndpoints


class Constant(Credentials, APIEndpoints):

    BASE_PATH = os.getcwd()
    TEST_FOLDER = BASE_PATH + '/tests/'
    LOG_FILE = BASE_PATH + '/log'
    REPORT_FOLDER = 'reports'
    config = {}

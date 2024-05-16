import json
import logging
import inspect
import os
from test_suite.src.Constants.constant import Constant


class Logger:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Configure logging to both console and file
    formatter = logging.Formatter("%(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")

    if not os.path.exists(Constant.LOG_FILE):
        os.makedirs(Constant.LOG_FILE)

    fh = logging.FileHandler(Constant.LOG_FILE + "/debug.log")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    @staticmethod
    def configure_logger():
        logger = logging.getLogger("debugLog")
        logger.setLevel(logging.DEBUG)
        _file_path = Constant.LOG_FILE + "/debug.log"
        os.makedirs(os.path.dirname(_file_path), exist_ok=True)  # Create log directory if it doesn't exist
        formatter = logging.Formatter(
            # Format for our loglines
            "%(asctime)s - %(message).6000s", "%Y-%m-%d %H:%M:%S")
        fh = logging.FileHandler(_file_path)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    @staticmethod
    def log(*message):
        stack_info = inspect.stack()[1]
        module = inspect.getmodule(stack_info[0])
        filename = str(module.__name__)
        line_no = str(stack_info[2])
        logging.basicConfig(format="%(asctime)s - %(message)s")
        logger = logging.getLogger('debugLog')
        logger.setLevel(logging.DEBUG)
        tmp = f"{filename}:{stack_info[3]}:{line_no}:  {' '.join(map(str, message))}"  # noqa
        logger.debug(tmp)

    @staticmethod
    def log_request(url, method, data, header, query_param):
        request_data = {
            'request_url': url,
            'request_method': method,
            'request_header': header,
            'request_body': data,
            'request_query': query_param
        }
        Logger.logger.debug("Request:\n%s", json.dumps(request_data, indent=4))

    @staticmethod
    def log_response(response, max_length=1000):
        response_data = {
            'response_url': response.url,
            'response_status_code': response.status_code,
            'response_body': response.text[:max_length] + '...' if len(response.text) > max_length else response.json()
        }
        Logger.logger.debug("Response:\n%s", json.dumps(response_data, indent=4))

    @staticmethod
    def log_error(error, request_data, response):
        Logger.logger.error("Error occurred: %s", error)
        Logger.logger.error("Request:\n%s", json.dumps(request_data, indent=4))
        Logger.logger.error("Response:\n%s", json.dumps(response, indent=4))

    @staticmethod
    def log_stack_trace():
        stack = inspect.stack()
        stack.reverse()
        Logger.logger.debug("Stack Trace:")
        for frame_info in stack[1:]:
            frame = frame_info.frame
            Logger.logger.debug("%s:%d in %s", frame.f_code.co_filename, frame.f_lineno, frame.f_code.co_name)
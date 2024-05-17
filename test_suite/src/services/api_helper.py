import json
import requests

from test_suite.src.utilities.logger import Logger
from jsonschema import validate


class ApiHelper:

    # Method help to construct custom headers
    @staticmethod
    def construct_header(custom_header={}):
        headers = {"Content-Type": "application/json"}
        if custom_header != {}:
            headers.update(custom_header)
        return headers

    @staticmethod
    def make_request(url: str, method: str, data: [dict, None] = None, header: [dict, None] = {}, auth=None,
                     query_param: [dict, None] = None, validate: bool = True, params={'page': 2}) -> dict:
        Logger.log_request(url, method, data, ApiHelper.construct_header(header), query_param)
        response = None
        try:
            if method == 'GET':
                response = requests.get(
                    url=url, params=query_param, headers=ApiHelper.construct_header(header), auth=auth)
            elif method == 'POST':
                response = requests.post(url=url, data=json.dumps(
                    data), headers=ApiHelper.construct_header(header), auth=auth)
            elif method == 'PUT':
                response = requests.put(url=url, data=json.dumps(
                    data), headers=ApiHelper.construct_header(header), auth=auth)
            elif method == 'DELETE':
                response = requests.delete(url=url, params=query_param, headers=ApiHelper.construct_header(header), auth=auth)
            else:
                Logger.logger.error("Invalid Method Requested")
                raise RuntimeError('Invalid Method : ', method)
        except requests.exceptions.HTTPError as errh:
            Logger.log_error(errh, data, response)
            raise
        except requests.exceptions.ConnectionError as errc:
            Logger.log_error(errc, data, response)
            raise
        except requests.exceptions.Timeout as errt:
            Logger.log_error(errt, data, response)
            raise
        except requests.exceptions.RequestException as err:
            Logger.log_error(err, data, response)
            raise
        Logger.log_response(response)
        return {'response_body': response.json(), 'status_code': response.status_code, 'response': response}

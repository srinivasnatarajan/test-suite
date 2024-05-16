from test_suite.src.Constants.constant import Constant
from test_suite.src.utilities.logger import Logger
from icecream import ic


class BaseSetup:

    @staticmethod
    def initialize_base(args):
        ic(args)
        Logger.configure_logger()
        Constant.config['cluster'] = args.c
        Constant.base_url = Constant.app[args.c]['base_url']
        Constant.config.update(Constant.app[args.c])
        Constant.external_api = Constant.api_route['external']
        Constant.internal_api = Constant.api_route['internal']
        Constant.config['api_basic_auth'] = (
            Constant.config['qa_client_key'], Constant.config['qa_client_secret'])
        Constant.config['testFilter'] = args.f
        Constant.config['type'] = args.t
        Logger.log('Setup completed')

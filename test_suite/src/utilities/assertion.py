from test_suite.src.utilities.logger import Logger


class Assertion:

    @staticmethod
    def construct_assertion(assertion_condition, assertion_message):
        if assertion_condition:
            Logger.log("Assertion Passed", assertion_message)
        else:
            Logger.log("Assertion Failed", assertion_message)
            assert assertion_condition, assertion_message

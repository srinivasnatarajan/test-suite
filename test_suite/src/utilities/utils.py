import json
import time

from test_suite.src.utilities.logger import Logger


class Utils:

    @staticmethod
    def remove_keys_from_dict(payload: dict, key: list) -> dict:
        for item in key:
            payload.pop(item)
        return payload

    @staticmethod
    def compare_json_objects(object1, object2, ignore_keys=None) -> bool:
        if ignore_keys is None:
            ignore_keys = []

        def filter_keys(obj):
            return {k: v for k, v in obj.items() if k not in ignore_keys}

        filtered_object1 = filter_keys(object1)
        filtered_object2 = filter_keys(object2)

        if json.dumps(filtered_object1, sort_keys=True) != json.dumps(filtered_object2, sort_keys=True):
            differing_keys = {k: (filtered_object1[k], filtered_object2[k]) for k in filtered_object1 if
                              filtered_object1[k] != filtered_object2[k]}
            # Log the differing key-value pairs
            print(f"Differing key-value pairs: {differing_keys}")
            return False

        return True

    @staticmethod
    def get_current_timestamp() -> str:
        return str(int(round(time.time() * 1000)))

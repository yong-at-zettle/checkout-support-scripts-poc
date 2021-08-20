import json


class IoHelper:
    @staticmethod
    def get_raw_lines(filename: str) -> list[str]:
        with open(filename) as lines:
            return [line.rstrip() for line in lines]

    @staticmethod
    def print_pretty_json(json_str: str):
        print(json.dumps(json_str, indent=4, sort_keys=True))

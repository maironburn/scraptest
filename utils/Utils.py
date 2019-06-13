from os import path
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)


def loadGlobalConfigFromJSON(config_file):
    try:
        json_data = {}
        if path.exists(config_file):
            with open(config_file) as json_config:
                json_data = json.load(json_config, encoding='utf-8')

    except Exception as e:
        print("{}".format(e))

    return json_data


if __name__ == '__main__':
    config_file = "../settings/sites_json"
    data = loadGlobalConfigFromJSON(config_file)
    pass
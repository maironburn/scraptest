from os import path
import json
import pprint

from setuptools.command.setopt import config_file

from settings.sites.sites_json import json_data
pp = pprint.PrettyPrinter(indent=4)


def loadGlobalConfigFromJSON(sites_json):

    json_data = {}
    def load_json(config_file):

        nonlocal json_data
        if path.exists(config_file):
            with open(config_file) as cf:
                return json.load(cf, encoding='utf-8')

        elif isinstance(config_file, str):
            return json.loads(config_file, encoding='utf-8')

    return load_json


if __name__ == '__main__':
    config_file = "../settings/sites_json.py"
    load_data = loadGlobalConfigFromJSON(json_data)
    load_data(json_data)
    print ("")
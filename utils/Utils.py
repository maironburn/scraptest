from os import path
import json
import pprint
import importlib

from setuptools.command.setopt import config_file

from settings.sites.sites_json import json_data
pp = pprint.PrettyPrinter(indent=4)


def loadGlobalConfigFromJSON(config_file):

    if path.exists(config_file):
        with open(config_file) as cf:
            return json.load(cf, encoding='utf-8')

    elif isinstance(config_file, str):
        return json.loads(config_file, encoding='utf-8')

    return None


if __name__ == '__main__':

    loaded_data = loadGlobalConfigFromJSON(json_data)

    if loaded_data:
        divx= loaded_data.get('divx', None)
        pp.pprint(loaded_data)

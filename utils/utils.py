from os import path
import json
import pprint
import os
from settings.sites import json_bank_skel

pp = pprint.PrettyPrinter(indent=4)
from settings.sites.json_bank_skel import *


def load_json_bank_skel(bankname):
    try:
        json_bank = getattr(json_bank_skel, bankname)
        if json_bank_skel:
            return json_bank

    except Exception as e:
        pass

    return None


if __name__ == '__main__':
    pass

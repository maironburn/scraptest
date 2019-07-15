from settings.json_banks import json_bank_skel
from common_config import JSONES
import os
from importlib import import_module

'''
carga el skel del banco correspondiente 
@param bankname : str(nombre del banco)
@return : diccionario de la entidad (definida en el skel)
'''


def load_json_bank_from_skel(bankname):
    try:
        json_file = os.path.join(JSONES, "{}.py".format(bankname))
        module_name = "settings.json_banks.{}".format(bankname)
        if os.path.exists(json_file):
            module = import_module(module_name)
            return getattr(module, bankname)

    except Exception as e:
        pass

    return None


if __name__ == '__main__':
    test = load_json_bank_skel('babucha')

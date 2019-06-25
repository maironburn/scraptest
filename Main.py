# -*- coding: utf-8 -*-

from src.base_xtractor import BaseXtractor

try:
    pass

except Exception as e:
    print("Extension no reconocida{} {}".format("1", "2"))

if __name__ == '__main__':

    kw={'url': 'https://grantorrent.net/categoria/HDRip/'}
    bx = BaseXtractor(**kw)
    pass

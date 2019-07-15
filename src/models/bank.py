# -*- coding: utf-8 -*-

from settings.sites.json_bank_skel import *
from utils.utils import load_json_bank_skel


class Bank(object):
    _driver = None
    _name = None
    _json_data = None

    def __init__(self, kw):
        self._driver = kw.get('driver', None)
        self._name = kw.get('name', None)

        if self.driver and self.name:
            #self.json_data = jso(self.name)
            print("way out of here")
    def load_data(self):
        pass

    @property
    def driver(self):
        return self._driver

    @property
    def name(self):
        return self._name

    @property
    def json_data(self):
        return self._json_data

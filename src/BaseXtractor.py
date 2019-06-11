#! /bin/env/python

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from utils.Logger.AppLogger import AppLogger


class BaseXtractor(object):
    url = None
    _response = None
    logger = None
    _soup = None

    def __init__(self, **kw):

        self.logger = AppLogger.create_rotating_log()
        self.logger.info("Inicializado Logger")
        if kw:
            self.url = kw.get('url', None)
            if self.response:
                self._soup = BeautifulSoup(self.response, "html.parser")

    @property
    def response(self):

        try:
            self._response = requests.get(self.url, allow_redirects=True, verify=False)
            self._response.raise_for_status()

        except requests.exceptions.HTTPError as httpError:
            self.logger.error("Excepcion en getting response: {}".format(httpError))

        except Exception as e:
            self.logger.error("Excepcion en getting: {}".format(e))

        return self._response



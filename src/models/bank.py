# -*- coding: utf-8 -*-
from src.helpers.common_helper import load_json_bank_from_skel
from logger.app_logger import AppLogger
from src.models.cuenta import Cuenta


class Bank(object):
    _name = None
    _json_data = None
    _logger = None
    _cuentas_asociadas = []

    def __init__(self, kw):

        self._name = kw.get('name', None)
        self._logger = kw.get('logger', None)
        if self.name:
            self._json_data = self.load_skel()

    def load_skel(self):

        try:
            self._json_data = load_json_bank_from_skel(self.name)
            self._logger.info('{} -> Loaded skel from : {}'.format(self.__class__.name, self.name))
            return self._json_data

        except Exception as lse:
            self._logger.error("{}-> exception loading skel {} -> {}".format(self.__class__.name, self.name, lse))

        return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value

    @property
    def json_data(self):
        return self._json_data

    @json_data.setter
    def json_data(self, value):
        if value:
            self._json_data = value

    @property
    def cuentas_asociadas(self):
        return self._cuentas_asociadas

    @cuentas_asociadas.setter
    def cuentas_asociadas(self, value):
        if isinstance(value, Cuenta):
            self._cuentas_asociadas = value


class CitiBank(Bank):

    _num_boleto = None
    _cnpj_pagador = None
    _cnpj_beneficiario = None

    def __init__(self, kw):
        super().__init__(kw)

    @property
    def num_boleto(self):
        return self._num_boleto

    @num_boleto.setter
    def num_boleto(self, value):
        if value:
            self._num_boleto = value

    @property
    def cnpj_pagador(self):
        return self._cnpj_pagador

    @cnpj_pagador.setter
    def cnpj_pagador(self, value):
        if value:
            self._cnpj_pagador = value

    @property
    def cnpj_beneficiario(self):
        return self._cnpj_beneficiario

    @cnpj_beneficiario.setter
    def cnpj_beneficiario(self, value):
        if value:
            self._cnpj_beneficiario = value


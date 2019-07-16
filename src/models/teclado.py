# -*- coding: utf-8 -*-

from os import path, listdir
from common_config import DATASET_IMGS, TEMP_IMGS
from src.helpers.automation_helper import capture_screen,move_and_click
from src.helpers.automation_helper import getElementCoords
from src.models.boton import Boton
from logger.app_logger import AppLogger

'''
Clase q mapea el tecladito de la entidad a partir de su dataset de imagenes
Captura la pantalla mediante el capture_screen de automation_helper  y mapea los elementos con getElementCoords
Uso: 
Tratandose de una identificacion de imgs ... solo tiene sentido ser instanciada cuando el tecladito sea visible
durante la inicializacion se captura la pantalla y se mapean los Botones del dataset
(debe ser instanciada mediante el callback del skel correspondiente
'''


class Teclado(object):
    '''carpeta del dataset'''
    _folder = None
    '''dataset diccionario k: str(teclita), value: Boton'''
    _dataset = {}

    def __init__(self, kw):

        bank_name = kw.get('bankname', None)
        self._logger = AppLogger.create_rotating_log() if not kw.get('logger', None) else kw.get('logger')
        if bank_name and self.dataset_exist(bank_name):
            capture_screen(name=bank_name)
            self.map_them_all(bank_name)

    def dataset_exist(self, bank_name):
        self.folder = path.join(DATASET_IMGS, bank_name)
        return path.exists(self.folder) and path.isdir(self.folder)

    def map_them_all(self, bank_name):

        haystack = path.join(TEMP_IMGS, "{}{}".format(bank_name, '.png'))
        for element in [x for x in listdir(self.folder)]:
            key = self.get_name_from_filename(element)
            x, y = getElementCoords(haystack, path.join(self.folder, element))
            kw = {'name': key, 'image': element, 'x': x, 'y': y}
            value = Boton(kw)
            self._logger.info("mapeado Boton: {}, coords x: {} , y: {}".format(key, x, y))
            self._dataset.update({key: value})

        print("all mapped")

    def add_boton(self, boton):
        if isinstance(boton, Boton):
            self._dataset.update({boton.name: boton})

    def write(self, text, case_sensitive=False):
        if not case_sensitive:
            text=text.lower()
        for i in text:
            if i in self.dataset.keys():
                move_and_click(self.dataset.get(i))

    def get_name_from_filename(self, filename):
        '''nombre de la teclita '''
        # @todo or not to do ! ... caracteres utf8...
        return filename.split('.')[0]

    @property
    def folder(self):
        return self._folder

    @folder.setter
    def folder(self, value):
        if path.exists(value):
            self._folder = value

    @property
    def dataset(self):
        return self._dataset


if __name__ == '__main__':
    teclado = Teclado({'bankname': 'unicaja'})
    pass

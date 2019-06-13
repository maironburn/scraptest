#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Pelicula(object):
    _nombre = ""
    _genero = ""
    _ano = ""
    _director = []
    _actores = []
    _formato = ""
    _duracion = ""
    _tamano = ""
    _sinopsis = ""

    def __init__(self, **kw):

        self._nombre = kw.get('nombre', None)
        self._genero = kw.get('genero', None)
        self._ano = kw.get('ano', None)
        self._director = kw.get('director', [])
        self._actores = kw.get('actores', [])
        self._formato = kw.get('formato', None)
        self._duracion = kw.get('duracion', None)
        self._tamano = kw.get('tamano', None)
        self._sinopsis = kw.get('sinopsis', None)
        self._img = kw.get('img', None)


    # <editor-fold desc="Getter y Setters">
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if value:
            self._nombre = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        if value:
            self._genero = value

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        if value:
            self._ano = value

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        if value:
            self._director = value

    @property
    def actores(self):
        return self._actores

    @actores.setter
    def actores(self, value):
        if value:
            self._actores = value

    @property
    def formato(self):
        return self._formato

    @formato.setter
    def formato(self, value):
        if value:
            self._formato = value

    @property
    def duracion(self):
        return self._formato

    @duracion.setter
    def duracion(self, value):
        if value:
            self._duracion = value

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, value):
        if value:
            self._tamano = value

    @property
    def sinopsis(self):
        return self._sinopsis

    @sinopsis.setter
    def sinopsis(self, value):
        if value:
            self._sinopsis = value

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        if value:
            self._img = value
    # </editor-fold>


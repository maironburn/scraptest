import os

class Boton(object):
    _name = ''
    _image = ''
    _x = 0.0
    _y = 0.0

    def __init__(self, kw):

        self._name = kw.get('name')
        self._image = kw.get('image')
        self._x = kw.get('x')
        self._y = kw.get('y')

    # <editor-fold desc="Getter y Setters">

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):

        if value:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value:
            self._y = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        if value:
            self._image = value



    # </editor-fold>


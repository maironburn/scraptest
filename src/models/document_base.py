# -*- coding: utf-8 -*-

import requests
import hashlib
import mimetypes
from logger.AppLogger import AppLogger


class DocumentBase(object):
    _url = None
    _content_type = None
    _response = None
    _md5 = None
    logger = None
    _filename = None
    _file_full_path = None

    def __init__(self, url=""):

        self.logger = AppLogger.create_rotating_log()
        self.logger.info("Log inicializado")

        self._url = ""

        self.url = url
        self._response = self.get_response()
        self._filename = self.url.split('/')[-1]
        self.logger.info("Nombre del documento: %s" % (self._filename,))
        self._file_full_path = "DOC_TEMP_DIR" + self._filename
        self.logger.info("file_full_path: %s" % (self._file_full_path,))
        if self._response:
            self._content_type = self.get_content_type()
            self.logger.info("content_type: %s" % (self._content_type,))
            self.create_temporalfile_from_content()
            self._md5 = self.calculate_md5sum()

    ''' guarda el contenido remoto en fichero temporal en modo raw'''
    def create_temporalfile_from_content(self):
        try:
            with open(self._file_full_path, 'wb') as f:
                f.write(self._response.content)

        except Exception as e:
            print ("Excepcion al guardar el documento, createTempFileFromContent : %s" .format(e))

    def get_response(self):

        r = None
        try:
            r = requests.get(self.url, allow_redirects=True, verify=False)
            r.raise_for_status()

        except requests.exceptions.HTTPError as httpError:
            self.logger.error("Excepcion en get_response: %s" % (format(httpError),))

        except Exception as e:
            self.logger.error("Excepcion en get_response: %s" % (format(e),))

        return r

    ''' obtiene el tipo mime ap del response / content-type '''
    def get_content_type(self):

        if self._response:
            return mimetypes.guess_extension(self._response.headers['content-type'])[1:]

        return None

    @property
    def content_type(self):
        return self._content_type


if __name__ == "__main__":
    pass

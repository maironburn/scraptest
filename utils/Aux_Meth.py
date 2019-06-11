from settings.settings import *
import importlib

def getLibForProcessing(extension=None):

    if extension and extension in DOCUMENTS_TYPES_PARSER.keys():
        try:

            print "Libreria a importar %s" % (DOCUMENTS_TYPES_PARSER[extension])
            importlib.import_module(DOCUMENTS_TYPES_PARSER[extension])
            print "libreria %s importada con exito" % (DOCUMENTS_TYPES_PARSER[extension])

            reader = getattr(DOCUMENTS_TYPES_PARSER[extension], READER_WRITER_DICT [extension]['reader'])
            writer = getattr(DOCUMENTS_TYPES_PARSER[extension], READER_WRITER_DICT [extension]['writer'])

            return reader, writer

        except Exception as e:
            print "excepcion: %e" % (format(e))

import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGGER_NAME = "Bank_RPA"
LOG_FILE = "{}{}{}{}{}".format(ROOT_DIR, os.path.sep, 'logger', os.path.sep, LOGGER_NAME)
SETTINGS = os.path.join(ROOT_DIR, 'settings')
# por si selenium
SELENIUM_DRIVER_PATH = os.path.join(ROOT_DIR, '{}{}{}'.format('chromedriver_win32', os.path.sep, 'chromedriver.exe'))

''''
Seguramente se requiera la lectura del user para leer las cookies del User_Data \ prodile
'''

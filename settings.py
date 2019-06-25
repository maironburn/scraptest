import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGGER_NAME = "BanKScrapy"
LOG_FILE = "{}{}{}{}{}".format(ROOT_DIR, os.path.sep, 'logger', os.path.sep, LOGGER_NAME)
SETTINGS = os.path.join(ROOT_DIR, 'settings')

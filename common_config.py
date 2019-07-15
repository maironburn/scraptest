import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

LOGGER_NAME = "B4nk_Sr4py"
LOG_FILE = os.path.join(ROOT_DIR, "logger{}{}".format(os.path.sep, LOGGER_NAME))
SETTINGS = os.path.join(ROOT_DIR, 'settings')
JSONES = os.path.join(SETTINGS, 'json_banks')

# keep_foregorund
APP_NAME = ""
TIME_SLEEP = 10

# selenium stuff
SELENIUM_DRIVER_PATH = os.path.join(ROOT_DIR, '{}{}{}'.format('chromedriver_win32', os.path.sep, 'chromedriver.exe'))

# imagenes
IMG_DIRS = os.path.join(ROOT_DIR, 'img')
TEMP_IMGS = os.path.join(IMG_DIRS, 'temps_imgs')
DATASET_IMGS = os.path.join(IMG_DIRS, 'datasets')

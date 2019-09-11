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
IE_DRIVER_PATH = os.path.join(ROOT_DIR, '{}{}{}'.format('IEDriver', os.path.sep, 'IEDriverServer.exe'))

# imagenes
IMG_DIRS = os.path.join(ROOT_DIR, 'img')
TEMP_IMGS = os.path.join(IMG_DIRS, 'temps_imgs')
DATASET_IMGS = os.path.join(IMG_DIRS, 'datasets')

#Folder to store after generate public /private RSA keys
RSA_KEYS = os.path.join(ROOT_DIR, "crypto{}{}".format(os.path.sep, "rsa_keys"))
FICHERO_CREDENCIALES=os.path.join(SETTINGS, "credentials{}{}".format(os.path.sep, "credentials.py"))

COOKIE_FILE= os.path.join(ROOT_DIR, "src{}controllers{}TestCookies.pkl".format(os.path.sep, os.path.sep))
CHROME_DIR='C:\\Users\\mario.diaz.rodriguez\\AppData\\Local\\Google\\Chrome\\User Data'

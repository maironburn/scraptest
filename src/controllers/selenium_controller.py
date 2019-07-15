from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from src.models.teclado import Teclado
from common_config import SELENIUM_DRIVER_PATH

'''
incializa el driver 

@start_opc... si requiere parametros adicionales, ni lo considero ahora mismo
options for session_id ?
headless como opcion en skell? 
probablemente -> user-data-dir; 
    string: path to user data directory that Chrome is using
    option_set.add_argument('disable-notifications')

interesante:  Enable popup blocking with chromedriver
https://bugs.chromium.org/p/chromedriver/issues/detail?id=1291
'''


def start(start_opc=None):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(SELENIUM_DRIVER_PATH, chrome_options=options)

    if driver:
        return driver
    return None


'''
login estandar
    Se entiende un formulario de login simple
    usuario, pwd y [algun otro dato adicional]
'''


def standard_login(driver, dict_bank):
    if driver:
        driver.get(dict_bank.get('login_url'))
        credentials = dict_bank.get('credentials')
        login_form = dict_bank.get('login_form')

    try:

        for k, v in login_form.items():
            if k in credentials.keys():
                elem = driver.find_element_by_xpath(v)
                elem.send_keys(credentials[k])

        submit = driver.find_element_by_xpath(login_form.get('submit'))
        submit.click()

        return driver

    except NoSuchElementException as nse:
        print("no enconcontrado")

    return False


'''
login precioso de reconocimiento de imagenes
'''


def login_bello(driver, dict_bank):
    if driver:
        driver.get(dict_bank.get('login_url'))
        credentials = dict_bank.get('credentials')
        login_form = dict_bank.get('login_form')

    try:

        # for k, v in login_form.items():
        #     if k in credentials.keys():
        #         elem = driver.find_element_by_id(v)
        #         elem.send_keys(credentials[k])

        element = driver.find_element_by_xpath(login_form.get('user'))
        element.clear()
        element.send_keys(credentials.get('user'))
        sleep(2)
        element = driver.find_element_by_xpath(login_form.get('pin'))
        element.send_keys('%')
        sleep(10)
        teclado = Teclado({'bankname': 'kutxabank'})
        # element = driver.find_element_by_xpath(login_form.get('user'))
        teclado.write(credentials.get('pin'))
        submit = driver.find_element_by_xpath(login_form.get('submit'))
        submit.click()

        return driver

    except NoSuchElementException as nse:
        print("no enconcontrado")

    return False


'''
@todo : tu debes desaparecer (caso bankia: ahora en post_login_actions -> refactor
'''


def check_dnd(driver, dict_bank):
    if driver:
        dnd = dict_bank.get('dnd', None)
        if dnd:
            for k, v in dnd.items():
                try:
                    if driver.find_element_by_class_name(k):
                        driver.find_element_by_xpath(v).click()
                except Exception as e:
                    print("buscando condicion dnd: {} -> xpath: {}".format(k, v))


'''
ejecuta secuencialmente el workflow definido en el skel
'''


# @todo; considerar el callback para el reconocimiento de imgs...buen comodin
def do_workflow(driver, list_workflow):
    try:
        dict_search_method = {'xpath': driver.find_element_by_xpath,
                              'class': driver.find_element_by_class_name,
                              'id': driver.find_element_by_id,
                              'link_text' : driver.find_element_by_link_text,
                              'partial_link_text' : driver.find_element_by_partial_link_text

                              }
        for w in list_workflow:
            # tipo de busqueda para localizar al elemento
            tipo = w.get('tipo')
            element = dict_search_method.get(tipo)(w.get('target'))

            sleep(2)
            if w.get('mode') == 'click':
                element.click()

            if w.get('mode') == 'fill':
                # previamente a send_keys se requiere un clear
                element.clear()
                element.send_keys(w.get('data'))

            if w.get('expect_cond'):
                wait = WebDriverWait(driver, 10)
                wait.until(ec.element_to_be_clickable((By.XPATH, w.get('expect_cond'))))
            else:
                sleep(1)
    except Exception:
        print("oooo ooooooooo")

    driver_close(driver)


def driver_close(driver):
    if driver:
        driver.closer()

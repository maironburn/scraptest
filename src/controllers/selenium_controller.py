from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from src.models.teclado import Teclado
from common_config import SELENIUM_DRIVER_PATH
from logger.app_logger import AppLogger
from slugify import slugify

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


class SeleniumController(object):
    _driver = None
    _bank = None
    _logger = None
    _dict_navigated_elements = []
    _current_window = None
    find_method = None

    def __init__(self, kw):

        self._logger = AppLogger.create_rotating_log() if kw.get('logger', None) is None else kw.get('logger')
        if kw.get('bank', None):
            self.bank = kw.get('bank')
            self.start() if kw.get('selenium_opts', None) is None else self.start(kw.get('selenium_opts'))
            self.find_method = self.load_find_method_references()
            self.finds_method = self.load_finds_method_references()

    def do_the_process(self):

        try:
            # independientemente de que halla acciones prelogin ...lo primero es abrir la url de la web
            self.driver.get(self.bank.get('login_url'))
            # comprobamos si son necesarias llevar a cabo acciones antes de iniciar el proceso de logado
            if self.bank.get('pre_login_actions'):
                self._logger.debug("Se requieren acciones previas al logado")
                self.pre_post_login_actions(self.bank.get('pre_login_actions'), stage="pre")

            auth_meth = self.bank.get('login_method')
            self.loggin_dict_meth = {'standard_login': self.standard_login,
                                     'login_bello': self.login_bello
                                     }

            self.loggin_dict_meth[auth_meth]()

            # comprobamos si son necesarias llevar a cabo acciones posteriores al logado
            if self.bank.get('post_login_actions'):
                self._logger.debug("Se requieren acciones posteriores al logado")
                self.pre_post_login_actions(self.bank.get('post_login_actions'), stage="post")

            self.do_workflow()

        except Exception as ex:

            print("peto")

    '''
    @:param, lista de opciones con las que inicializar el driver de selenium
    '''
    def start(self, default_opc=["--start-maximized"]):

        options = webdriver.ChromeOptions()
        for opc in default_opc:
            options.add_argument(opc)

        self._driver = webdriver.Chrome(SELENIUM_DRIVER_PATH, chrome_options=options)

        if self._driver:
            self.load_find_method_references()
            return self._driver

        return None

    def load_find_method_references(self):

        return {
            'name': self.driver.find_element_by_name,
            'xpath': self.driver.find_element_by_xpath,
            'class': self.driver.find_element_by_class_name,
            'id': self.driver.find_element_by_id,
            'link_text': self.driver.find_element_by_link_text,
            'partial_link_text': self.driver.find_element_by_partial_link_text,
            'css_selector': self.driver.find_element_by_css_selector
        }

    def load_finds_method_references(self):

        return {
            'name': self.driver.find_elements_by_name,
            'xpath': self.driver.find_elements_by_xpath,
            'class': self.driver.find_elements_by_class_name,
            'id': self.driver.find_elements_by_id,
            'link_text': self.driver.find_elements_by_link_text,
            'partial_link_text': self.driver.find_elements_by_partial_link_text,
            'css_selector': self.driver.find_elements_by_css_selector
        }

    '''
    login estandar
        Se entiende un formulario de login simple
        usuario, pwd y [algun otro dato adicional]
    '''

    '''
    
        apertura de nuevo tab
        @:param, element_that_cause_the_swapping (elemento que causa el swap)
        
    '''

    def swap_window(self, element_that_cause_the_swapping=None):

        current = self.driver.window_handles[0]
        if element_that_cause_the_swapping:
            element_that_cause_the_swapping.click()

            WebDriverWait(self.driver, 20).until(ec.number_of_windows_to_be(2))
            new_windows = [window for window in self.driver.window_handles if window != current][0]
            self.driver.switch_to.window(new_windows)
            sleep(5)

    def standard_login(self):
        if self.driver:

            self.current_windows = self.driver.window_handles[0]
            credentials = self.bank.get('credentials')
            login_form = self.bank.get('login_form')

        try:
            self._logger.debug("Inciando proceso standard de logado")
            for k, v in login_form.items():
                if k in credentials.keys():
                    # verificamos existencia del elemento target
                    tipo = login_form.get(k)['tipo']
                    target = login_form.get(k)['target']
                    self._logger.info("Buscando por {} -> {}".format(tipo, target))
                    if len(self.finds_method[tipo](target)):
                        self._logger.info("Elemento encontrado: {}".format(k))
                        elem = self.find_method[tipo](target)
                        elem.send_keys(credentials[k])

            e_submit = login_form.get('submit')
            submit = self.find_method[e_submit['tipo']](e_submit['target'])
            submit.click()

            return self.driver

        except NoSuchElementException as nse:
            self._logger.error("Elemento no encontrado: {}".format(k))
            pass

        return False

    '''
    login precioso de reconocimiento de imagenes
    '''

    def login_bello(self):
        if self.driver:

            credentials = self.bank.get('credentials')
            login_form = self.bank.get('login_form')

        try:
            self._logger.debug("Inciando proceso de logado Beeello")

            tipo = login_form.get('user')['tipo']
            target = login_form.get('user')['target']
            element = self.find_method[tipo](target)
            element.clear()
            element.send_keys(credentials.get('user'))
            sleep(1)
            # pin y carga del teclado
            tipo = login_form.get('pin')['tipo']
            target = login_form.get('pin')['target']
            element = self.find_method[tipo](target)

            element.send_keys('%')
            sleep(2)

            teclado = Teclado({'bankname': self.bank.get('bankname')})
            teclado.write(credentials.get('pin'))

            tipo = login_form.get('submit')['tipo']
            target = login_form.get('submit')['target']
            submit = self.find_method[tipo](target)
            submit.click()

            # driver.get('https://www.kutxabank.es/NASApp/BesaideNet2/Gestor?PRESTACION=login&FUNCION=login&ACCION=preseleccion')

            return self.driver

        except NoSuchElementException as nse:
            print("no enconcontrado")

        return False

    '''
        acciones post login o post login, la mecanica es igual
        @:param, lista de acciones (pre o post acciones)
    '''

    def pre_post_login_actions(self, lista_acciones=None, stage=""):

        if self.driver and len(lista_acciones):
            self._logger.info("Evaluando acciones {} login".format(stage))
            for actions in lista_acciones:

                try:
                    tipo = actions.get('tipo')
                    target = actions.get('target')
                    desc = actions.get('description')
                    mode = actions.get('mode')
                    self._logger.info(
                        "{} -> tipo busqueda: {} , expresion: {} , mode: {}".format(desc, tipo, target, mode))


                    if len(self.finds_method[tipo](target)):
                        self._logger.info("matched condition {} !! ".format(desc))
                        elem = self.find_method[tipo](target)
                        if mode == 'click':
                            elem.click()

                        if mode == 'swap_window':
                            self.swap_window(elem)
                        sleep(2)
                except Exception as e:
                    pass
                    # print("buscando condicion dnd: {} -> xpath: {}".format(k, v))

    def do_workflow(self):
        try:

            for action in self.bank.get('workflow'):
                # tipo de busqueda para localizar al elemento
                tipo = action.get('tipo')
                target = action.get('target')
                desc = action.get('description', None)
                mode = action.get('mode')

                self._logger.info(
                    "{} -> tipo busqueda: {} , expresion: {} , mode: {}".format(desc, tipo, target, mode))

                if len(self.finds_method[tipo](target)):
                    self._logger.info("matched condition {} !! ".format(desc))
                    element = self.find_method[tipo](target)
                    sleep(2)
                    if mode == 'click':
                        element.click()

                    if mode == 'fill':
                        # previamente a send_keys se requiere un clear
                        element.clear()
                        element.send_keys(action.get('data'))

                    if action.get('expect_cond'):
                        wait = WebDriverWait(self.driver, 10)
                        wait.until(ec.element_to_be_clickable((By.XPATH, action.get('expect_cond'))))
                    else:
                        sleep(1)

                    self.navigated_elements.append({slugify(target): element})

        except Exception:
            self._logger.error("Error duante el workflow")

        self.driver_close()

    def driver_close(self):
        if self.driver:
            self.driver.close()

    # <editor-fold desc="getters /setters">
    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, value):
        if value:
            return self._driver

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value):
        if isinstance(value, dict):
            self._bank = value

    @property
    def navigated_elements(self):
        return self._navigated_elements

    @navigated_elements.setter
    def navigated_elements(self, value):
        if isinstance(value, list):
            self._navigated_elements = value

    @property
    def current_windows(self):
        return self._current_window

    # </editor-fold>

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys
def doLogin(driver, dict_bank):
    if driver:
        driver.get(dict_bank.get('login_url'))
        credentials = dict_bank.get('credentials')
        login_form = dict_bank.get('login_form')

    try:

        for k, v in login_form.items():
            if k in credentials.keys():
                elem = driver.find_element_by_id(v)
                elem.send_keys(credentials[k])

        submit = driver.find_element_by_xpath(login_form.get('submit'))
        submit.click()

        return driver

    except NoSuchElementException as nse:
        print("no enconcontrado")

    return False


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


def do_workflow(driver, list_workflow):

    try:
        for w in list_workflow:
            xpath = w.get('xpath')
            element = driver.find_element_by_xpath(xpath)
            sleep(2)
            if w.get('mode') == 'click':
                element.click()

            if w.get('mode') == 'fill':
                element.clear()

                element.send_keys(w.get('data'))

            if w.get('expect_cond'):
                wait = WebDriverWait(driver, 10)
                element = wait.until(ec.element_to_be_clickable((By.XPATH, w.get('expect_cond'))))
            else:
                sleep(1)
    except Exception:
        print("oooo ooooooooo")

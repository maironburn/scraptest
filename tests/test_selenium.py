from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from common_config import SELENIUM_DRIVER_PATH
from src.selenium_loader import start
from src.models.bank import *
from utils.utils import load_json_bank_skel
from bs4 import BeautifulSoup
from src.controllers.helper import doLogin, check_dnd, do_workflow
from time import sleep
from selenium.webdriver.common.by import By

print("{}".format(SELENIUM_DRIVER_PATH))
driver = start()
# add options ? for session_id, headless ?
# kw = {'driver': driver, 'name': 'bankia'}
bankia = load_json_bank_skel('bankia')
page = doLogin(driver, bankia)
sleep(10)
check_dnd(driver, bankia)
do_workflow(driver, bankia.get('workflow'))

# bank = Bank(kw)

#
# driver.find_element_by_xpath("//td[(@scope='row')]/a").click()
# if link:
#     url= bankia.get('base') + link
#     driver.get(url)

# target= sopa_preciosa.find("input", {"id": "id-search-field"})
# target.attrs.update({'class': 'target_class'})
# new_tag = sopa_preciosa.new_tag('target_element', id='target_element')
# target.append(new_tag)
#
# driver.execute_script()
#
# elem = driver.find_element_by_class_name("target_class")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

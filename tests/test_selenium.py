from common_config import SELENIUM_DRIVER_PATH
from src.controllers.selenium_controller import start
from src.helpers.common_helper import load_json_bank_from_skel
# from bs4 import BeautifulSoup < -- sopa preciosa aun no te he necesitado :( !!
from src.controllers.selenium_controller import standard_login,login_bello, check_dnd, do_workflow
from time import sleep

print("{}".format(SELENIUM_DRIVER_PATH))
driver = start()
# kw = {'driver': driver, 'name': 'bankia'}
# bankia = load_json_bank_from_skel('bankia')
babucha = load_json_bank_from_skel('babucha')
auth_method = babucha.get('login_method')
page = auth_method(driver, babucha)
sleep(10)
check_dnd(driver, babucha)
do_workflow(driver, babucha.get('workflow'))
driver.close()
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

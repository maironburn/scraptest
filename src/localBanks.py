# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:15:54 2019

@author: julieta.bogado
"""

import warnings; warnings.filterwarnings("ignore")
from selenium import webdriver
import os
from os import environ
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By 
from datetime import datetime, timedelta, date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import glob
from pyautogui import alert


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def rename_excel_file(user, bank_name,account, date_Today):
    list_of_files = glob.glob('C:\\Users\\'+user+'\\Downloads\\*.xls')
    latest_file = max(list_of_files, key = os.path.getctime)
    file_path_name = 'C:\\Users\\'+user+'\\Documents\\Bancos\\Descarga_movimientos\\'+ bank_name + account +'-'+ dateFile + '.xls'
    #check if file exists:
    if not os.path.exists(file_path_name):
        os.rename(latest_file, file_path_name)
    else:
        pass

def waitElement(webId):
    while browser.find_elements_by_id(webId) == []:
        time.sleep(1)

def waitXpathElement(webXpath):
    while browser.find_elements_by_xpath(webXpath)== []:
            time.sleep(1)
    
def bankia(us, empresa, pin):
    try:
        account = ['ES7620380445386000034900','ES7420380445326000034648']
        if date.today().weekday() == 0:
            date1 = datetime.strftime(datetime.now() - timedelta(11), '%d/%m/%Y')
            dateS = date1.split('/')
        else:
            date1 = datetime.strftime(datetime.now() - timedelta(7), '%d/%m/%Y')
            dateS = date1.split('/')
        url = 'https://oficinaempresas.bankia.es/es/login.html'
        index = 1
        ind=0
        for i in range(2):
            browser.get(url)
            waitElement('tab2')
            browser.find_element_by_id('tab2').click()
            time.sleep(1)
            browser.find_element_by_id('nUsuario').send_keys(str(us[index]))
            browser.find_element_by_id('nContrato').send_keys(str(empresa[index]))
            browser.find_element_by_xpath('//*[@id="pass2"]/div/input[1]').send_keys(pin[index])
            browser.find_element_by_xpath('//*[@id="panel-1"]/form/div[5]/input').click()
            time.sleep(5)
            try:
                WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="accounts-table"]/tbody/tr/td[4]/a')))
                browser.find_element_by_xpath('//*[@id="accounts-table"]/tbody/tr/td[4]/a').click()
            except:
                browser.switch_to_active_element().find_element_by_class_name('bki-close').click()
                browser.switch_to_default_content()
                while browser.find_elements_by_xpath('//*[@id="accounts-table"]/tbody/tr/td[4]/a') == []:
                    time.sleep(1)
                browser.find_element_by_xpath('//*[@id="accounts-table"]/tbody/tr/td[4]/a').click()
            waitXpathElement('//*[@id="oie2-layout-content"]/section[1]/header/div[2]/button[3]')
            browser.find_element_by_xpath('//*[@id="oie2-layout-content"]/section[1]/header/div[2]/button[3]').click()
            try:
                browser.find_element_by_id('daysimpleDateFrom').clear()
                browser.find_element_by_id('monthsimpleDateFrom').clear()
                browser.find_element_by_id('yearsimpleDateFrom').clear()
                time.sleep(1)
                browser.find_element_by_id('daysimpleDateFrom').send_keys(dateS[0])
                browser.find_element_by_id('monthsimpleDateFrom').send_keys(dateS[1])
                browser.find_element_by_id('yearsimpleDateFrom').send_keys(dateS[2])
                browser.find_element_by_id('daysimpleDateTo').clear()
                browser.find_element_by_id('monthsimpleDateTo').clear()
                browser.find_element_by_id('yearsimpleDateTo').clear()
                time.sleep(1)
                browser.find_element_by_id('daysimpleDateTo').send_keys(dateTodayS[0])
                browser.find_element_by_id('monthsimpleDateTo').send_keys(dateTodayS[1])
                browser.find_element_by_id('yearsimpleDateTo').send_keys(dateTodayS[2])
                time.sleep(1)
                browser.find_element_by_xpath('//*[@id="oie2-layout-content"]/section[1]/article/div/fieldset/ul/li/button').click()
                waitElement('content')
                browser.find_element_by_id('deviceBody').find_elements_by_id('content')[2]
                browser.find_element_by_class_name('ng-scope').find_elements_by_tag_name('section')[1]
                browser.find_element_by_class_name('oie2-main-grid').find_elements_by_tag_name('div')[1]
                button = browser.find_element_by_class_name('oie2-icon-btn')
                time.sleep(2)
                browser.execute_script("window.scrollBy(0, -150);", button)
                time.sleep(1)
                button.click()
                time.sleep(1)
                browser.find_element_by_xpath('//*[@id="oie2-layout-content"]/section[1]/header/div[2]/ul/li[1]/a').click()
                time.sleep(5)
                browser.find_element_by_xpath('//*[@id="header-container"]/button').click()
                time.sleep(5)
                rename_excel_file(user,'bankia',account[ind],dateFile)
                index += 1
                ind += 1
            except:
                print('Error en Bankia')
    except:
        print('Error on Bankia')

def bbva(us, empresa, pin):
    try:
        if date.today().weekday() == 0 or date.today().weekday() == 1 or date.today().weekday() == 2:
            date1 = datetime.strftime(datetime.now() - timedelta(5), '%d/%m/%Y')
            dateS = date1.split('/')
        elif date.today().weekday() == 3 or date.today().weekday() == 4:
            date1 = datetime.strftime(datetime.now() - timedelta(4), '%d/%m/%Y')
            dateS = date1.split('/')
        account =['ES7601824572460201520783','ES2601824572410010063134']
        ind = 0
        url = 'https://www.bbvanetcash.com'
        index = 7
        for i in range(2):
            browser.get(url)
            try:
                browser.find_element_by_xpath('//*[@id="modal_redirect_content"]/div[1]/div').click()
            except:
                pass
            try:
                #input cod empresa
                browser.find_element_by_id('cod_emp').send_keys(us[index])
                #input user
                browser.find_element_by_id('cod_usu').send_keys(empresa[index])
                #input contraseña
                browser.find_element_by_id('eai_password').send_keys(pin[index])
                #click entrar
                browser.find_element_by_xpath('//*[@id="cuerpo_izquierda_top"]/button').click()
                time.sleep(15)
            except:
                browser.find_element_by_id('changeLabel').click()
                #input cod empresa
                browser.find_element_by_id('cod_emp').send_keys(us[index])
                #input user
                browser.find_element_by_id('cod_usu').send_keys(empresa[index])
                #input contraseña
                browser.find_element_by_id('eai_password').send_keys(pin[index])
                #click entrar
                browser.find_element_by_xpath('//*[@id="cuerpo_izquierda_top"]/button').click()
                time.sleep(15)
            #informacion de cuentas
            
            browser.find_element_by_id('kyop-menuOption-200300000B-menuLeft').click()
            children = browser.find_element_by_id('kyop-div-children-container-200300000B-menuLeft')
            for c in children.find_elements_by_tag_name('a'):
                if c.text == 'Saldos y movimientos':
                    c.click()
            time.sleep(3)
            browser.switch_to_frame(browser.find_element_by_id('kyop-central-load-area'))
            browser.find_element_by_id('kyos_cabeceraPpal')
            c =browser.find_elements_by_tag_name('th')
            #click on checkbox saldos y movimientos
            browser.find_element_by_id('kyos_seleccionarTodasCuentasPC').click()
            time.sleep(2)
            #click on button movimientos
            browser.find_element_by_id('kyos_botonConsultarMovimientosPC').click()
            time.sleep(2)
            #input yesterday date
            browser.find_element_by_id('kyos_fechaDesdePC').send_keys(dateS)
            time.sleep(1)
            #input today date
            browser.find_element_by_id('kyos_fechaHastaPC').send_keys(dateTodayS)
            time.sleep(1)
            try:
                #click on button consultar
                browser.find_element_by_xpath('//*[@id="kyos_consultarMovimientosTooltip"]/div[14]/div/button').click()
            except:
                browser.switch_to_default_content()
                browser.find_element_by_xpath('//*[@id="9807951"]/div[1]').click()
                browser.switch_to_frame(browser.find_element_by_id('kyop-central-load-area'))
                #click on button consultar
                browser.find_element_by_xpath('//*[@id="kyos_consultarMovimientosTooltip"]/div[14]/div/button').click()
            #click on download button
            time.sleep(3)
            try:
                browser.find_element_by_id('kyos_descargar_resultadoMovSpan_0').click()
                #click XLS format
                browser.find_element_by_id('kyos_XLSDescargar_0').click()
                time.sleep(2)
                #click on download button
                browser.find_element_by_xpath('//*[@id="kyos_descargarPosicionCuentasTooltip_0"]/div[7]/div').click()
                time.sleep(4)
                rename_excel_file(user,'BBVA',account[ind],dateFile)
            except:
                print('BBVA: NO HAY MOVIMIENTOS EN EL PERÍODO INGRESADO')
            index += 1
            ind += 1
    except:
        print('Error on Bbva Bank')

def ibercaja(us, pin):
    try:
        account = 'ES4120858058920330024055'
        if date.today().weekday() == 0:
            date1 = datetime.strftime(datetime.now() - timedelta(28), '%d/%m/%Y')
            dateS = date1.split('/')
        else:
            date1 = datetime.strftime(datetime.now() - timedelta(28), '%d/%m/%Y')
            dateS = date1.split('/')
        url = "https://www.ibercaja.es/"
        browser.get(url)
        time.sleep(3)
        try:
            browser.find_element_by_xpath('/html/body/div[1]/div/a/span').click()
        except:
            pass
        waitXpathElement('//*[@id="login"]/a[1]')
        browser.find_element_by_xpath('//*[@id="login"]/a[1]').click()
        time.sleep(2)
        browser.find_element_by_id('codeibd').send_keys(us[11])
        browser.find_element_by_id('claveibd').send_keys(pin[11])
        browser.find_element_by_id('entraribd').click()
        browser.find_element_by_id('menu_vertical')
        browser.switch_to_frame(browser.find_element_by_id('menu_vertical'))
        browser.find_element_by_id('li2a').click()
        time.sleep(2)
        #fecha desde
        browser.switch_to_default_content()
        browser.find_element_by_id('operativas')
        browser.switch_to_frame(browser.find_element_by_id('operativas'))
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[2]/td[2]/input[1]').clear()
        time.sleep(0.5)
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[2]/td[2]/input[1]').send_keys(dateS[0])
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[2]/td[2]/input[2]').clear()
        time.sleep(0.5)
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[2]/td[2]/input[2]').send_keys(dateS[1])
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[2]/td[2]/input[3]').clear()
        time.sleep(0.5)
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[2]/td[2]/input[3]').send_keys(dateS[2])
        time.sleep(1)
        #fecha hasta
        browser.switch_to_default_content()
        browser.find_element_by_id('operativas')
        browser.switch_to_frame(browser.find_element_by_id('operativas'))
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]')
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[2]/td[4]/input[1]').send_keys(dateTodayS[0])
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[2]/td[4]/input[2]').send_keys(dateTodayS[1])
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[2]/td[4]/input[3]').send_keys(dateTodayS[2])
        #click aceptar
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[3]/tbody/tr/td[2]/input').click()
    except:
        print('Error en IberCaja.')
    try:
        browser.find_element_by_xpath('//*[@id="Formulario"]/table[3]/tbody/tr/td/a').click()
        time.sleep(4)
        rename_excel_file(user,'Ibercaja',account,dateFile)
    except:
        print('IberCaja: No hay movimientos en la fecha ingresada')

def morabanc(us,pin):
    try:
        account = 'AD2800040019000027042019'
        if date.today().weekday() == 0:
            date1 = datetime.strftime(datetime.now() - timedelta(11), '%d/%m/%Y')
        else:
            date1 = datetime.strftime(datetime.now() - timedelta(11), '%d/%m/%Y')
        url= 'https://www.morabanc.ad/onlinebanking/GeneralServlet'
        browser.get(url)
        waitXpathElement('//*[@id="user"]')
        browser.find_element_by_xpath('//*[@id="user"]').send_keys(us[9])
        waitXpathElement('//*[@id="write"]')
        browser.find_element_by_xpath('//*[@id="write"]').send_keys(pin[9])
        time.sleep(1)
        browser.find_element_by_id('GA_login_acceder_privada').click()
        waitXpathElement('//*[@id="listacuentas"]/div/div[1]/div[1]/h4/a')
        cuentaCorriente = browser.find_element_by_xpath('//*[@id="listacuentas"]/div/div[1]/div[1]/h4/a')
        time.sleep(2)
        cuentaCorriente.location_once_scrolled_into_view
        cuentaCorriente.click()
        time.sleep(10)
        #click on buton search
        browser.find_element_by_id('botonsubmit').click()
        #click on filters
        browser.find_element_by_xpath('//*[@id="masmovimientos"]/div[4]/div/p/i[1]').click()
        #input yesterday date
        browser.find_element_by_id('search-start-date').send_keys(date1)
        #input today date
        time.sleep(1)
        #click on search button
        browser.find_element_by_id('submit-advanced-search').click()
        #click on download
        a = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="listMovV"]/div[1]/i[3]'))) 
        a.click()
        try:
            browser.find_element_by_xpath('//*[@id="listMovV"]/div[2]/div[1]/div/p[3]').click()
            time.sleep(4)
            rename_excel_file(user,'Morabanc',account,dateFile)
        except:
            print('no se encuentran fechas')
        time.sleep(4)
    except:
        print('Error en banco MoraBank')


def bancsabadellAndorra(us, pin):
    try:
        account = 'AD5100080090341200031339'
        if date.today().weekday() == 0:
            date1 = datetime.strftime(datetime.now() - timedelta(28), '%d/%m/%Y')
            dateS = date1.split('/')
        else:
            date1 = datetime.strftime(datetime.now() - timedelta(28), '%d/%m/%Y')
            dateS = date1.split('/')
        url = 'https://www.bsandorra.com/'
        browser.get(url)
        waitXpathElement('//*[@id="mainMenu"]/li[2]/a')
        browser.find_element_by_xpath('//*[@id="mainMenu"]/li[2]/a').click()
        waitXpathElement('//*[@id="formLoginTbl"]/tbody/tr[1]/td[2]/input')
        browser.find_element_by_xpath('//*[@id="formLoginTbl"]/tbody/tr[3]/td[1]/div/a').click()
        waitXpathElement('//*[@id="accessForms"]/div[2]/form/ul/li[4]/h2')
        browser.find_element_by_xpath('//*[@id="accessForms"]/div[2]/form/ul/li[4]/h2').click()
        #send usuario
        browser.find_element_by_name('userDNI4').send_keys(us[12])
        browser.find_element_by_name('pinNif4').send_keys(pin[12])
        browser.find_elements_by_id('button1')[3].click()
        browser.switch_to_default_content()
        browser.find_element_by_xpath('//*[@id="leftZone"]/ul/li[2]/a').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="sm_full_NETi_container"]/left/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[15]/td[2]/input[2]').click()
        time.sleep(1)
        #cambiar fechas
        browser.find_element_by_xpath('//*[@id="sm_full_NETi_container"]/left/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[9]/td/input[2]').clear()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sm_full_NETi_container"]/left/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[9]/td/input[2]').send_keys(dateS[0])
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sm_full_NETi_container"]/left/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[9]/td/input[3]').clear()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sm_full_NETi_container"]/left/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[9]/td/input[3]').send_keys(dateS[1])
        time.sleep(2)
        #descargar
        browser.find_element_by_name('enviar').click()
        # descargar excel
        time.sleep(4)
        rename_excel_file(user,'Sabadell_Andorra',account,dateFile)
    except:
        print('Error en banco Sabadell de Andorra')

def clickCuenta(index):
    browser.find_element_by_class_name('sel_empresa').click()
    browser.find_elements_by_class_name('link_empresa')[index].click()

def dateExportBack():
    if date.today().weekday() == 0 or date.today().weekday() == 1 or date.today().weekday() == 2 or date.today().weekday() == 3:
        date1 = datetime.strftime(datetime.now() - timedelta(6), '%d/%m/%Y')
        dateS = date1.split('/')
    elif date.today().weekday() == 4:
        date1 = datetime.strftime(datetime.now() - timedelta(4), '%d/%m/%Y')
        dateS = date1.split('/')
    browser.find_element_by_id('dia').send_keys(dateS[0])
    browser.find_element_by_id('mes').send_keys(dateS[1])
    browser.find_element_by_id('year').send_keys(dateS[2])
    browser.find_element_by_id('diaH').send_keys(dateTodayS[0])
    browser.find_element_by_id('mesH').send_keys(dateTodayS[1])
    browser.find_element_by_id('yearH').send_keys(dateTodayS[2])
    browser.find_element_by_xpath('//*[@id="frmPageBusq"]/div[2]/button').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="descarga"]/span').click()
    time.sleep(4)
    browser.find_element_by_class_name('bna_pestselec_01').click()
    time.sleep(3)
    
def bankinter(us,pin):
    try:
        account = ['-6000-Accenture_SL','-6001-Tecnilógica_Ecosistemas_SAU','-6002-Aos_SA','-6025-Energuia_Web','-6024-Customerwork','-6040-Holdings','-6008-Avanade_Spain-SAU','-6012-Itbs','-6020-Informatica_Euskadi']
        url = r'https://empresas.bankinter.com/www/es-es/cgi/empresas+cuentas+integral'
        browser.get(url)
        #lista de cuentas con indices
        lista_cuentas = [0,1,2,4,5,6,7,8,9]
        #input user
        waitElement('lg_username')
        browser.find_element_by_id('lg_username').send_keys(str(us[3]))
        #input password
        browser.find_element_by_id('lg_password').send_keys(str(pin[3]))
        #click on button go
        browser.find_element_by_xpath('//*[@id="frmLogin"]/div/div/div[2]/div[4]/div/input').click()
        time.sleep(3)
        index=0
        #Rest of the accounts
        for i in lista_cuentas:
            #delete javascript pop-up
#            browser.execute_script("document.getElementById('notificacion_push').remove(); document.getElementById('notificacion_push').remove()")
            try:
                browser.switch_to_active_element().find_element_by_xpath('//*[@id="notificacion_push"]/div/div/div/div/div/div/div/div/center/div/table/tbody/tr[2]/td/table/tbody/tr/td/p[4]/a/font').click()
            except:
                pass                
            clickCuenta(lista_cuentas[index])
            time.sleep(4)
            if len(browser.find_elements_by_id('empresaCVI')) == 1:
                if True:
                    try:
                        browser.switch_to_active_element().find_element_by_xpath('//*[@id="notificacion_push"]/div/div/div/div/div/div/div/div/center/div/table/tbody/tr[2]/td/table/tbody/tr/td/p[4]/a').click()
                    except:
                        pass
                    browser.find_element_by_id('empresaCVI').click()
                    time.sleep(3)
                    #click en cuenta
                    if len(browser.find_elements_by_id('cta_1_0'))==1:
                        browser.find_element_by_id('cta_1_0').click()
                    elif len(browser.find_elements_by_id('cta0'))==1:
                        browser.find_element_by_id('cta0').click()
                    time.sleep(3)
                    dateExportBack()
                    time.sleep(4)
                    rename_excel_file(user,'Bankinter',account[index],dateFile)
                else:
                    time.sleep(4)
                    browser.switch_to_active_element().find_element_by_xpath('//*[@id="notificacion_push"]/div/div/div/div/div/div/div/div/center/div/table/tbody/tr[2]/td/table/tbody/tr/td/p[4]/a').click()
                    clickCuenta(lista_cuentas[index])
                    time.sleep(5)
                    browser.find_element_by_id('empresaCVI').click()
                    time.sleep(3)
                    #click en cuenta
                    if len(browser.find_elements_by_id('cta_1_0'))==1:
                        browser.find_element_by_id('cta_1_0').click()
                    elif len(browser.find_elements_by_id('cta0'))==1:
                        browser.find_element_by_id('cta0').click()
                    time.sleep(3)
                    dateExportBack()
                    time.sleep(4)
                    rename_excel_file(user,'Bankinter',account[index],dateFile)
            elif len(browser.find_elements_by_id('cta_1_0')) == 1:
                if True:
                    try:
                        browser.switch_to_active_element().find_element_by_xpath('//*[@id="notificacion_push"]/div/div/div/div/div/div/div/div/center/div/table/tbody/tr[2]/td/table/tbody/tr/td/p[4]/a').click()
                    except:
                        pass
                    browser.find_element_by_id('cta_1_0').click()
                    clickCuenta(lista_cuentas[index])
                    time.sleep(3)
                    if len(browser.find_elements_by_id('cta_1_0'))==1:
                        browser.find_element_by_id('cta_1_0').click()
                    elif len(browser.find_elements_by_id('cta0'))==1:
                        browser.find_element_by_id('cta0').click()
                    dateExportBack()
                    time.sleep(4)
                    rename_excel_file(user,'Bankinter',account[index],dateFile)
                else:
                    time.sleep(4)
                    browser.switch_to_active_element().find_element_by_xpath('//*[@id="notificacion_push"]/div/div/div/div/div/div/div/div/center/div/table/tbody/tr[2]/td/table/tbody/tr/td/p[4]/a').click()
                    clickCuenta(4)
                    time.sleep(3)
                    if len(browser.find_elements_by_id('cta_1_0'))==1:
                        browser.find_element_by_id('cta_1_0').click()
                    elif len(browser.find_elements_by_id('cta0'))==1:
                        browser.find_element_by_id('cta0').click()
                    dateExportBack()
                    time.sleep(4)
                    rename_excel_file(user,'Bankinter',account[index],dateFile)
            index += 1
    except:
        print('Error en Bankinter Bank')

def boa(us, empresa, pin):
    try:
        url = 'https://cashproonline.bankofamerica.com/AuthenticationFrameworkWeb/cpo/login/public/loginMain.faces'
        index = 0
        account = 'Spain'
        lista = [1,2]
        browser.get(url)
        waitElement('loginRight:login_form:companyId')
        browser.find_element_by_id('loginRight:login_form:companyId').send_keys(us[10])
        browser.find_element_by_id('loginRight:login_form:userId').send_keys(empresa[10])
        browser.find_element_by_id('password').send_keys(pin[10])
        browser.find_element_by_id('loginRight:login_form:loginButton').click()
        #click reporting
        waitElement('reportingId-span')
        browser.find_element_by_id('reportingId-span').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="irReportsPDRId-span"]/span[1]').click()
        waitElement('iframe2theme')
        browser.find_element_by_id('iframe2theme')
        browser.switch_to_frame(browser.find_element_by_id('iframe2theme'))
        browser.find_element_by_id('irFrame')
        browser.switch_to_frame(browser.find_element_by_id('irFrame'))
        browser.find_element_by_id('irCustomStepOne').find_element_by_id('irCustomStepOne:favpage_body').find_element_by_id('irCustomStepOne:reportsPanel')
        browser.find_element_by_id('irCustomStepOne:headerDataTableId:tbtn').find_element_by_id('irCustomStepOne:headerDataTableId:tbn')
        browser.find_element_by_id('irCustomStepOne:headerDataTableId:21:rowChkBox').click()
        #select excel & pdf
        for i in lista:
            browser.find_element_by_xpath('//*[@id="irCustomStepOne:headerDataTableId:tbn"]/tr[23]/td[3]').click()
            selection = Select(browser.find_element_by_id('irCustomStepOne:headerDataTableId:21:hiddenStatusId9'))
            time.sleep(2)
            selection.select_by_index(lista[index])
            selection.select_by_index(lista[index])
            time.sleep(4)
            #download
            browser.find_element_by_id('irCustomStepOne:exportbtn').click()
            time.sleep(5)
            index += 1
        rename_excel_file(user,'BankOfAmerica-',account,dateFile)
    except:
        print('Error on Bank of America')

def santanderBank(us, pin):
#    try:
        account = ['ES9400491811312910359607','ES1100492036302814098352','ES6100301518010870009271']
        url ="https://www.bancosantander.es/es/empresas#"
        browser.get(url)
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="_W054_Menu_Cabecera_WAR_W054_Menu_Cabeceraportlet__VIEW"]/div/header/div[1]/div[2]/div[4]/div/nav/ul/li[3]/div/div/a')))
        browser.find_element_by_xpath('//*[@id="_W054_Menu_Cabecera_WAR_W054_Menu_Cabeceraportlet__VIEW"]/div/header/div[1]/div[2]/div[4]/div/nav/ul/li[3]/div/div/a').click()
        time.sleep(2)
        browser.find_element_by_id("iFrameNorm")
        browser.switch_to_frame(browser.find_element_by_id("iFrameNorm"))
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'usuarioForm')))
        browser.find_element_by_id('usuarioForm').send_keys(us[6])
        browser.find_element_by_id('passwordForm').send_keys(pin[6])
        browser.find_element_by_id('login-button2').click()
        index = 0
        ind= 3
        for i in range(3):
            if ind == 4:
                date1 = datetime.strftime(datetime.now() - timedelta(28), '%d/%m/%Y')
                dateS = date1.split('/')
            elif date.today().weekday() == 0 or date.today().weekday() == 1 or date.today().weekday() == 2 or date.today().weekday() == 3:
                date1 = datetime.strftime(datetime.now() - timedelta(6), '%d/%m/%Y')
                dateS = date1.split('/')
            elif date.today().weekday() == 4:
                date1 = datetime.strftime(datetime.now() - timedelta(4), '%d/%m/%Y')
                dateS = date1.split('/')
            browser.window_handles
            time.sleep(2)
            browser.switch_to.window(browser.window_handles[1])
            time.sleep(7)
            try:
                browser.switch_to_active_element()
                time.sleep(3)
                browser.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div/span/i').click()
                time.sleep(3)
            except:
                pass
            while browser.find_elements_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[2]/a') == []:
                time.sleep(1)
            browser.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[2]/a').click()
            while browser.find_elements_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[2]/ul/li/div/div/ul[2]/li[2]/a') == []:
                time.sleep(1)
            browser.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[2]/ul/li/div/div/ul[2]/li[2]/a').click()
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'SEP')))
            browser.find_element_by_id('SEP')
            browser.switch_to_frame(browser.find_element_by_id('SEP'))
            time.sleep(3)
            browser.find_element_by_xpath('//*[@id="contenedorPrincipal"]/div[1]/div[3]').find_element_by_id('bodytable')
            browser.find_elements_by_tag_name('tr')[2].find_elements_by_tag_name('td')[4]
            time.sleep(3)
            #click en desplegable de numero de cuenta
            browser.find_element_by_xpath('//*[@id="bodytable"]/tbody[1]/tr['+str(ind)+']/td[5]/drop-down-box/div/button').click()
            time.sleep(2)
            #click en movimientos
            browser.find_element_by_xpath('//*[@id="bodytable"]/tbody[1]/tr['+str(ind)+']/td[5]/drop-down-box/div/ul/li[2]').click()
            time.sleep(3)
            #click fechadesde
            browser.find_element_by_xpath('//*[@id="fecha_desde"]/div/div/div').click()
            #MES ANTERIOR
            time.sleep(0.5)
            if dateS[1] != dateTodayS[1]:
                browser.find_element_by_xpath('//*[@id="fecha_desde"]/div/div/div/datepicker/div/div[1]/div[1]/a').click()
            else:
                pass
            time.sleep(2)
            browser.find_element_by_class_name('_720kb-datepicker-calendar-body')
            num = browser.find_elements_by_tag_name('a')
            for n in num:
                if n.text == dateS[0]:
                    n.click()
                    break
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="fecha_hasta"]/div/div/div/datepicker').click()
            browser.find_element_by_xpath('//*[@id="fecha_hasta"]/div/div/div/datepicker/div/div[3]')
            num2 = browser.find_elements_by_tag_name('a')
            for n in num2:
                if n.text == dateTodayS[0]:
                    n.click()
                    break
            time.sleep(2)
            browser.find_element_by_id('boton_filtros_2').click()
            time.sleep(5)
            selection = Select(browser.find_element_by_xpath('//*[@id="printableSection"]/div[2]/div[1]/div[1]/div/div[1]/select'))
            selection.select_by_index(2)
            time.sleep(4)
            try:
                browser.switch_to.window(browser.window_handles[2])
                browser.find_element_by_id('boton_cerrar_ventana').click()
                browser.switch_to.window(browser.window_handles[1])
            except:
                rename_excel_file(user,'SantanderBank-',account[index],dateFile)
            ind +=1
            index+=1
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
#    except:
#        print('Error en Santander Bank')
#        browser.switch_to.window(browser.window_handles[2])
#        browser.find_element_by_id('boton_cerrar_ventana').click()
#        browser.switch_to.window(browser.window_handles[1])

def Sabadell(us,pin):
    try:
        account = ['ES4000810300680001189320','ES1300815029170001669775']
        if date.today().weekday() == 0:
            date1 = datetime.strftime(datetime.now() - timedelta(28), '%d/%m/%Y')
        else:
            date1 = datetime.strftime(datetime.now() - timedelta(28), '%d/%m/%Y')
        url = 'https://www.bancsabadell.com/txempbs/default.bs'
        browser.get(url)
        while browser.find_elements_by_class_name('sbd-textfield-DNI') == None:
            time.sleep(1)
        #input user
        browser.find_element_by_class_name('sbd-textfield-DNI').send_keys(us[5])
        browser.find_element_by_xpath('//*[@id="accessKey"]/input').send_keys(pin[5])
        browser.find_element_by_xpath('//*[@id="On"]/span[2]').click()
        waitXpathElement('//*[@id="leftZone"]/ul/li[3]/a')
        #saldo y movimientos
        cont = 0
        for i in range(2):
            browser.find_element_by_xpath('//*[@id="leftZone"]/ul/li[3]/a').click()
            time.sleep(5)
            #CLICK ON FILTER
            browser.find_element_by_id('externalDIV_inputComponentsForm:orderAccount').click()
            if cont == 0:
                browser.find_element_by_link_text('ES40 0081 0300 6800 0118 9320 | ACCENTURE,S.L.').click()
            elif cont == 1:
                browser.find_element_by_link_text('ES13 0081 5029 1700 0166 9775 | AVANADE SPAIN S.L.').click()
            #input date yesterday
            browser.find_element_by_id('dateMovFrom2').send_keys(date1)
            #input date today
            browser.find_element_by_id('dateMovTo2').send_keys(dateToday)
            time.sleep(3)
            #click on button buscar
            browser.find_element_by_xpath('//*[@id="bs-busqueda-concreta"]/div/div/div/div[10]/button/span').click()
            time.sleep(3)
            #download excel file
            try:
                browser.find_element_by_xpath('//*[@id="menuleft"]/li[2]/a').click()
                time.sleep(4)
                rename_excel_file(user,'Sabadell-',account[cont],dateFile)
            except:
                print('Sabadell Bank: El periodo de fechas que usted ha seleccionado no contiene movimientos.')
            cont += 1
    except:
        print('Error en banco Sabadell')

def bancoPop(us, pin):
    try:
        account = ['Accenture', 'Avanade']
        if date.today().weekday() == 0 or date.today().weekday() == 1 :
            date1 = datetime.strftime(datetime.now() - timedelta(11), '%d/%m/%Y')
        elif date.today().weekday() == 2 or date.today().weekday() == 3 or date.today().weekday() == 4:
            date1 = datetime.strftime(datetime.now() - timedelta(9), '%d/%m/%Y')
        url = 'https://www4.bancopopular.es/eai_logon/GbpInternetLogonEAI/gbplogon?tipo_btt=em'
        browser.get(url)
        time.sleep(3)
        browser.find_element_by_id('username').send_keys(us[0])
        a = pin[0]
        pinLista=[]
        pinLista = list(str(a))
        index = 0
        ind = 0
        for i in pinLista:
            browser.find_element_by_name(pinLista[ind]).click()
            ind+=1
        time.sleep(1)
        browser.find_element_by_id("boton").click()
        time.sleep(3)
        tabla = browser.find_element_by_class_name('dojoxGridScrollbox')
        time.sleep(3)
        tabla.find_elements_by_tag_name('td')
        listacuentas = []
        for t in tabla.find_elements_by_tag_name('a'):
            listacuentas.append(t.text)
        for l in listacuentas:
            c=browser.find_element_by_link_text(l)
            c.click()
            waitElement('CUE9001C_PosicionIntegral3_linkCta_0_label')
            browser.find_element_by_id('CUE9001C_PosicionIntegral3_linkCta_0_label').click()
            time.sleep(8)
            d = browser.find_element_by_id('CUE0014C_Busq_MisCuentas_RelMov_fOpDesde')
            d.send_keys(date1)
            h = browser.find_element_by_id('CUE0014C_Busq_MisCuentas_RelMov_fOpHasta')
            h.send_keys(dateTodayS)
            browser.find_element_by_id('CUE0014C_Busq_MisCuentas_RelMov_btBusq').click()
            time.sleep(5)
            browser.find_element_by_id('mainContainer').find_element_by_id('cuerpo')
            browser.find_element_by_id('pagina').find_element_by_class_name('odb').find_element_by_id('odb_title')
            browser.find_elements_by_id('odb_sec_exp')
            lista = browser.find_element_by_tag_name('div')
            for i in lista.find_elements_by_tag_name('a'):
                if i.text == 'Excel':
                    i.click()
            browser.switch_to_default_content()
            time.sleep(5)
            browser.find_element_by_id('mainContainer').find_element_by_class_name('header_top')
            browser.find_element_by_id('launchSelContratos').click()
            time.sleep(4)
            rename_excel_file(user,'BancoPopular-',account[index],dateFile)
            index += 1
    except:
        print('Error on Banco Popular')

def bbk():
    account = ['ES6920950462413830261066','ES9720950461109100168147']
    url = 'https://bbk.kutxabank.es/cs/Satellite/kb/es/negocios_y_empresas'
    browser.get(url)
    alert(text='Click ok after you ve logued in.', title='Kutxabank', button='OK')
    current = browser.window_handles[0]
    WebDriverWait(browser, 20).until(EC.number_of_windows_to_be(2))
    newWindow = [window for window in browser.window_handles if window != current][0]
    browser.switch_to.window(newWindow)
    browser.find_element_by_id('divEntrar').click()
    waitElement('formPAS:j_id134:0:data1:0:j_id140:0:j_id144')
    browser.find_element_by_id('formPAS:j_id134:0:data1:0:j_id140:0:j_id144').click()
    time.sleep(4)
    browser.find_element_by_id('formCriterios:criteriosMovimientos:_1').click()
    time.sleep(5)
    try:
        browser.find_element_by_id('formListado:resourceExcel').click()
        rename_excel_file(user,'Kutxsabank-',account[0])
    except:
        print('BBK: No hay movimientos en el periodo ingresado.')
    time.sleep(6)
    #cambio de cuenta
    browser.find_element_by_id('formMenuSuperior:PanelSuperior:2:itemMenuSuperior').click()
    waitElement('formPAS:j_id97:0:data1:1:j_id103:0:j_id108')
    browser.find_element_by_id('formPAS:j_id97:0:data1:1:j_id103:0:j_id108').click()
    time.sleep(5)
    try:
        browser.find_element_by_id('formListado:resourceExcel').click()
        rename_excel_file(user,'Kutxsabank-',account[1],dateFile)
    except:
        print('BBK: No hay movimientos en el periodo ingresado.')
    time.sleep(6)
    browser.close()
    browser.switch_to_window(current)

def unicaja():
    if date.today().weekday() == 0:
        date1 = datetime.strftime(datetime.now() - timedelta(28), '%d/%m/%Y')
        dateS = date1.split('/')
    else:
        date1 = datetime.strftime(datetime.now() - timedelta(28), '%d/%m/%Y')
        dateS = date1.split('/')

    account = 'ES0621032811300032034812'
    url = "https://www.unicajabanco.es/es/empresas-y-autonomos"
    browser.get(url)
    browser.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/div/ul/li[2]/a').click()
    alert(text='Click ok after you ve logued in.', title='UniCaja', button='OK')
    time.sleep(5)
    current = browser.window_handles[0]
    WebDriverWait(browser, 20).until(EC.number_of_windows_to_be(2))
    newWindow = [window for window in browser.window_handles if window != current][0]
    browser.switch_to.window(newWindow)
    browser.find_element_by_xpath('//*[@id="menu3nivel"]/ul[1]/li/ul/li[5]/a').click()
    time.sleep(5)
    #fecha desde
    browser.find_element_by_xpath('//*[@id="diaDesde"]').send_keys(dateS[0])
    browser.find_element_by_xpath('//*[@id="mesDesde"]').send_keys(dateS[1])
    browser.find_element_by_xpath('//*[@id="anoDesde"]').send_keys(dateS[2])
    #fecha hasta
    browser.find_element_by_xpath('//*[@id="diaHasta"]').send_keys(dateTodayS[0])
    browser.find_element_by_xpath('//*[@id="mesHasta"]').send_keys(dateTodayS[1])
    browser.find_element_by_xpath('//*[@id="anoHasta"]').send_keys(dateTodayS[2])
    browser.find_element_by_xpath('//*[@id="univia"]/form/table/tbody/tr[9]/td/input').click()
    time.sleep(3)
    try:
        a =browser.find_element_by_xpath('//*[@id="mainContent"]/table/tbody/tr[2]/td/h2')
        if a.text == 'No existen movimientos para listar':
            print('Caja España: No existen movimientos durante el período de tiempo ingresado.')
    except:
        rename_excel_file(user,'Unicaja-',account,dateFile)
    time.sleep(4)
    browser.close()
    browser.switch_to_window(current)

def liberbank():
    date2 = datetime.strftime(datetime.now() - timedelta(28), '%d/%b/%Y')
    dateS = date2.split('/')
    dateBefore = [s.lstrip("0") for s in dateS]
    url = "https://www.cajaextremadura.es/particulares/"
    browser.get(url)
    alert(text='Click ok after you ve logued in.', title='Liberbank', button='OK')
    lista_cuentas = ['20480120440000363400015772','20480120440000373400015673']
    index = 0
    for i in lista_cuentas:
        try:
            browser.find_element_by_xpath('/html/frameset')
            browser.find_element_by_name('resultados')
            browser.switch_to_frame(browser.find_element_by_name('resultados'))
            browser.find_element_by_id('central')
            browser.find_element_by_id('TB_iframeContent')
            browser.switch_to_frame(browser.find_element_by_id('TB_iframeContent'))
            browser.find_element_by_id('central').find_element_by_class_name('link-flecha').click()
            browser.switch_to_default_content()
        except:
            browser.switch_to_default_content()
        browser.find_element_by_xpath('/html/frameset')
        browser.find_element_by_name('resultados')
        browser.switch_to_frame(browser.find_element_by_name('resultados'))
        time.sleep(3)
        browser.find_element_by_id('menuLI_cuentas').click()
        browser.find_element_by_xpath('//*[@id="'+str(lista_cuentas[index])+'"]')
        time.sleep(3)
        browser.switch_to_default_content()
        browser.find_element_by_name('resultados')
        browser.switch_to_frame(browser.find_element_by_name('resultados'))
        time.sleep(3)
        browser.find_element_by_xpath('/html').find_element_by_id('central').find_element_by_id('all')
        browser.find_element_by_id('datosContenidoSin').find_element_by_class_name('wrapper-generico').find_element_by_class_name('cuentas-content')
        browser.find_element_by_id('resumenCuentas').find_element_by_id('listadoCuentasInicio')
        browser.find_element_by_id(lista_cuentas[index]).click()
        time.sleep(2)
        #click mas movimientos
        browser.find_element_by_id('movimientosCuentaPrin').find_element_by_id('iframemovimientosCuentaPrin')
        browser.find_element_by_id('contenido')
        if index == 1:
            click_help = browser.find_element_by_id('contenido')
            click_help.click()
            actions = ActionChains(browser)
            for j in range(5):
                actions = actions.send_keys(Keys.TAB)
            actions = actions.send_keys(Keys.ENTER)
            actions.perform()
        elif index == 0:
            click_help = browser.find_element_by_id('20480120440000363400015772')
            click_help.click()
            actions = ActionChains(browser)
            actions = actions.send_keys(Keys.TAB)
            actions = actions.send_keys(Keys.ENTER)
            actions.perform()
        time.sleep(5)
        #click en calendar
        ul_help = browser.find_element_by_id('ul_opcionesminiDashboard')
        ul_help.click()
        actions = ActionChains(browser)
        for i in range(4):
            actions = actions.send_keys(Keys.TAB)
        actions = actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)
        browser.find_element_by_id('select_fecha_desde').click()
        browser.find_element_by_id('ui-datepicker-div').find_element_by_class_name('ui-datepicker-calendar').find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody')
        #tomo el mes
        mes_text = browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/span[1]')
        mes = mes_text.text
        #click mes
        while not mes.startswith((dateBefore[1]).upper()):
            next_month = browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/a[2]')
            next_month.click()
            #actualizo el mes dentro del loop
            mes_text = browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/span[1]')
            mes = mes_text.text
            time.sleep(1)
        time.sleep(2)
        table = browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody')
        table_tr = table.find_elements_by_tag_name('tr')
        #click  día
        for tr in table_tr:
            tr_td = tr.find_elements_by_tag_name('td')
            for td in tr_td:
                if td.text == str(dateBefore[0]):
                    td.click()
                    break
        #CLICK ACTUALIZAR
        browser.find_element_by_class_name('botonActualizar').click()
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="paginacion"]/ul/li[1]/div[1]/a').click()
        time.sleep(4)
        rename_excel_file(user,'Liberbank-',lista_cuentas[index],dateFile)
        #CLICK INICIO
        browser.find_element_by_id('menuLI_inicio').click()
        index += 1
        time.sleep(4)

user = environ.get('USERNAME')
options = webdriver.ChromeOptions()
prefs = {}
options.add_argument("--start-maximized")
driverPath = 'C:\\Users\\'+user+'\\Documents\\Bancos\\chromedriver_win32\\chromedriver.exe_old_one'
options.add_argument('user-data-dir=C:\\Users\\'+ user +'\\AppData\Local\\Google\\Chrome\\User Data')
browser = webdriver.Chrome(driverPath, chrome_options = options)
browser.execute_script("document.body.style.zoom='100 %'")
createFolder('C:\\Users\\'+user+'\\Documents\\Bancos\\Descarga_movimientos')
excelPath = r'C:\\Users\\'+ user +'\\Documents\\Bancos\\contraseñas.xlsx'
workbook = pd.ExcelFile(excelPath)
df=workbook.parse('Sheet1')
us , empresa, pin = df['Usuario'], df['Empresa'], df['Clave/Pin']
dateToday = datetime.today().strftime('%d/%m/%Y')
dateTodayS = dateToday.split('/')
dateFile = dateToday.replace('/','-')


bankia(us, empresa, pin)
time.sleep(3)
bbva(us, empresa, pin)
time.sleep(3)
ibercaja(us, pin)
time.sleep(3)
morabanc(us,pin) 
time.sleep(3)
bancsabadellAndorra(us, pin)
time.sleep(3)
bankinter(us, pin) 
time.sleep(3)
santanderBank(us, pin) 
time.sleep(3)
Sabadell(us, pin)
time.sleep(3)
bancoPop(us, pin)
time.sleep(3)
boa(us, empresa, pin)
time.sleep(3)
bbk()
time.sleep(3)
unicaja()
time.sleep(3)
liberbank()

browser.close()
alert(text='Descargas completadas.', title='Local Banks', button='OK')
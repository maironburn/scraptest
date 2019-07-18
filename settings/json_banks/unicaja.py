from src.controllers.selenium_controller import SeleniumController as sc

unicaja = {
    'bankname': "unicaja",
    'url_base': 'https://www.unicajabanco.es/es/empresas-y-autonomos',

    'login_url': 'https://www.unicajabanco.es/es/empresas-y-autonomos',
    # metodo de logado (standar, reconocimiento de imgs...whatever)
    'headless': False,

    'login_method': 'login_bello',
    # acciones a realizar antes de poder hacer login (deshacerse de popups, clicks sobre botones...)
    'pre_login_actions': [
        # boton acceso al area de clientes
        # <a target="_self" class="link-button btn-bg-red aceptarCookies" title="ACEPTAR Y SEGUIR NAVEGANDO">
        #                     ACEPTAR Y SEGUIR NAVEGANDO
        #                   </a>
        {'tipo': 'xpath',
         'target': "//div[@class='content']//div[@class='blockFaldon']//div[@class='botton-faldon']//div//a[@class='link-button btn-bg-red aceptarCookies'][contains(text(),'ACEPTAR Y SEGUIR NAVEGANDO')]",
         'mode': 'click',
         'description': 'ventana configuracion de cookies'}
        ,
        {'tipo': 'xpath', 'target': "//a[@id='/content/unicaja/es/es_header_composer_button1']", 'mode': 'swap_window',
         'description': 'click en Acceso al area de clientes', 'ec': {'tipo': 'xpath', 'target': "//input[@id='user']"}}

    ],

    # acciones a realizar despues del login (q no forman parte del workflow)
    'post_login_actions': [],

    # credenciales para la autenticacion
    'credentials': {
        'user': '',
        'pin': ''
    }
    ,
    # identificacion de los elmentos del formulario de login
    'login_form': {
        'user': {'tipo': 'xpath', 'target': "//input[@id='user']"},
        'pin': {'tipo': 'xpath', 'target': "//input[@id='clave']"},
        'submit': {'tipo': 'xpath', 'target': "//div[6]//input[1]"}
    }
    ,
    # periodicidad de las consultas ( @TBD )
    'checking_time': ''
    ,
    # elemento sobre el q interactuar / condicion posterior de espera para continuar el wf
    '''
        @param: tipo, determina el modo a captura del elemento

        en el metodo que lanza el workflow hay un diccionario con las posibles opciones de captura:
                dict_search_method = {'xpath': driver.find_element_by_xpath,
                                      'class': driver.find_element_by_class_name,
                                      'id': driver.find_element_by_id,
                                      'link_text' : driver.find_element_by_link_text,
                                      'partial_link_text' : driver.find_element_by_partial_link_text
                              }

        @param: target, expresion del elemento a capturar
        @param: expect_cond: condicion de espera (xpath del elemento que debe estar visible y clickable
                       de momento solo he tenido esta casuistica (ec.element_to_be_clickable)
        @param: mode : fill (para los textinput) | click (botones y enlace)
              Si el modo es fill llevara un campo de datos asociados...hardcodeado ahora mismo
              ya veremos como lo enchufo dp

            Dejo muestra, uno de cada tipo definido hasta el momento

        @param: callback: por si se requieren acciones adicionales en algun paso del workflow
    '''

    'workflow': [
        # click con condiciones de espera
        {'xpath': '//*[@id="menu3nivel"]/ul[1]/li/ul/li[5]/strong/a', 'mode': 'click'},

        # click sobre la lupa (sin condiciones de espera)

        {'xpath': '//*[@id="diaDesde"]', 'mode': 'fill', 'data': '01'},

        {'xpath': '//*[@id="mesDesde"]', 'mode': 'fill', 'data': '01'},
        {'xpath': '//*[@id="anoDesde"]',
         'mode': 'fill', 'data': '01'},

        {'xpath': '//*[@id="diaHasta"]',
         'mode': 'fill', 'data': '01'},

        {'xpath': '//*[@id="mesHasta"]',
         'mode': 'fill', 'data': '01'},

        {'xpath': '//*[@id="anoHasta"]',
         'mode': 'fill', 'data': '01'},

        {'xpath': '//*[@id="univia"]/form/table/tbody/tr[9]/td/input', 'mode': 'click'}

    ]

}

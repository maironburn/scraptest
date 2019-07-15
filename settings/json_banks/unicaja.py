from src.controllers.selenium_controller import login_bello

unicaja = {

    'url_base': 'https://www.unicajabanco.es/es/empresas-y-autonomos',

    'login_url': 'https://www.unicajabanco.es/es/empresas-y-autonomos',
    # metodo de logado (standar, reconocimiento de imgs...whatever)
    'headless': False,

    'login_method': login_bello,
    # acciones a realizar antes de poder hacer login (deshacerse de popups, clicks sobre botones...)
    'pre_login_actions': [
        # aceptar cookies
        {'tipo': 'xpath', 'target': "//a[(@target='_self')]"},
        # area de clientes
        {'tipo': 'xpath', 'target': "//a[(@title=' Ir a Acceso clientes ')]"}
    ],

    # acciones a realizar despues del login (q no forman parte del workflow)
    'post_login_actions': [],

    # credenciales para la autenticacion
    'credentials': {
        'user': '05238978S',
        'enterprise_id': '',
        'pin': 'JAZMIN10'
    }
    ,
    # identificacion de los elmentos del formulario de login
    'login_form': {
        # Xpath
        'user': "//input[(@id='clave')]",
        'enterprise_id': '',
        'pin': '',
        'submit': ""
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
        {'xpath': "//td[(@scope='row')]/a", 'expect_cond': "//button[(@ng-click='showSearch = !showSearch')]",
         'mode': 'click'},

        # click sobre la lupa (sin condiciones de espera)

        {'xpath': "//button[(@ng-click='showSearch = !showSearch')]",
         'mode': 'click'},
        # el fill de un text input
        {'xpath': "//input[(@name='daysimpleDateFrom')]", 'mode': 'fill', 'data': '06'},

    ]

}

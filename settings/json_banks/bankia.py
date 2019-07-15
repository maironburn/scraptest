from src.controllers.selenium_controller import standard_login

bankia = {

    # por si se requiere construir url a partir de otros params o url relativas
    'url_base': 'https://oficinaempresas.bankia.es/bole/es/',
    'headless': False,  # @todo

    # url de para el login
    'login_url': 'https://oficinaempresas.bankia.es/es/login.html',

    # metodo de logado (standar, reconocimiento de imgs...whatever)
    'login_method': standard_login,

    # acciones a realizar antes de poder hacer login (deshacerse de popups, clicks sobre botones...)
    'pre_login_actions': [],

    # acciones a realizar despues del login (q ,conceptualmente, no formen parte del workflow)
    # en este caso cierra un popup de bienvenida
    'post_login_actions': [{'modal-dialog': "//button[(@title='Cerrar')]"}],

    # credenciales para la autenticacion
    # @todo hay que determinar la fuente de credenciales
    'credentials': {
        'user': '',
        'enterprise_id': '',
        'pin': ''
    }
    ,
    # identificacion de los elmentos del formulario de login
    'login_form': {

        'user': "//input[(@ng-model='login.userId')]",
        'enterprise_id': "//input[(@ng-model=='login.contract')]",
        'pin': "//input[(@ng-model=login.password')]",
        'submit': "//input[(@value='Entrar')]"
    }
    ,
    # periodicidad de las consultas ( @TBD )
    'checking_time': ''
    ,
    # elemento sobre el q interactuar / condicion posterior de espera para continuar el wf
    # @todo ,  to think about (key adicional para invocar un callback o metodo ?... )
    'workflow': [{'tipo': 'xpath', 'target': "//td[(@scope='row')]/a",
                  'expect_cond': "//button[(@ng-click='showSearch = !showSearch')]",
                  'mode': 'click'},
                 # click sobre la lupa
                    {'tipo': 'xpath', 'target': "//button[(@ng-click='showSearch = !showSearch')]",
                   'mode': 'click'},
                    # formulario de busqueda
                    # desde
                    {'tipo': 'xpath', 'target': "//input[(@name='daysimpleDateFrom')]", 'mode': 'fill', 'data': '06'},
                    {'tipo': 'xpath', 'target': "//input[(@name='monthsimpleDateFrom')]", 'mode': 'fill', 'data': '06'},
                    {'tipo': 'xpath', 'target': "//input[(@name='yearsimpleDateFrom')]", 'mode': 'fill',
                      'data': '2019'},
                    # hasta
                    {'tipo': 'xpath', 'target': "//input[(@name='daysimpleDateTo')]", 'mode': 'fill', 'data': '15'},
                    {'tipo': 'xpath', 'target': "//input[(@name='monthsimpleDateTo')]", 'mode': 'fill', 'data': '06'},
                    {'tipo': 'xpath', 'target': "//input[(@name='yearsimpleDateTo')]", 'mode': 'fill','data': '2019'},
                    # boton buscar
                    {'tipo': 'xpath', 'target': "//button[(@class='oie2-btn btn-green bk-button')]", 'mode': 'click'},
                    # descargar
                    {'tipo': 'xpath', 'target': "//button[(@ng-click='showDropdown = !showDropdown')]", 'mode': 'click'},
                    # link descargar en excel
                    {'tipo': 'xpath', 'target': "//a[(@title='Exportar a Excel')]",'mode': 'click'}

                 ]
}

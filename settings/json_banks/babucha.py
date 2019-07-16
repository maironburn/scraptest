from src.controllers.selenium_controller import login_bello

babucha = {

    'bankname': 'kutxabank',

    'url_base': 'https://portal.kutxabank.es/cs/Satellite/kb/es/negocios_y_empresas',

    'login_url': 'https://portal.kutxabank.es/cs/Satellite/kb/es/negocios_y_empresas',

    'login_method': 'login_bello',

    'pre_login_actions': [],

    'post_login_actions': [],

    'credentials': {
        'user': '',
        'enterprise_id': '',
        'pin': ''
    }
    ,
    'login_form': {

        'user': {'tipo': 'xpath', 'target': "//input[(@name='usuario')]"},
        'pin': {'tipo': 'xpath', 'target': "//input[(@name='password_PAS')]"},
        'submit': {'tipo': 'xpath', 'target': "//input[(@name='enviar')]"}
    }
    ,
    # periodicidad de las consultas ( @TBD )
    'checking_time': ''
    ,

    'workflow': [
        # click con condiciones de espera
        {'tipo': 'class', 'target': "//td[(@scope='row')]/a",
         'expect_cond': "//button[(@ng-click='showSearch = !showSearch')]",
         'mode': 'click', 'description': ''},

        # click sobre la lupa (sin condiciones de espera)

        {'tipo': 'xpath', 'target': "//button[(@ng-click='showSearch = !showSearch')]",
         'mode': 'click', 'description': ''},
        # el fill de un text input
        {'tipo': 'xpath', 'target': "//input[(@name='daysimpleDateFrom')]", 'mode': 'fill', 'data': '06',
         'description': ''},

    ]

}

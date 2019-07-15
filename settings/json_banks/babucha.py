from src.controllers.selenium_controller import login_bello

babucha = {

    'url_base': 'https://portal.kutxabank.es/cs/Satellite/kb/es/negocios_y_empresas',

    'login_url': 'https://portal.kutxabank.es/cs/Satellite/kb/es/negocios_y_empresas',

    'login_method': login_bello,

    'pre_login_actions': [],

    'post_login_actions': [],


    'credentials': {
        'user': '3924804',
        'enterprise_id': '',
        'pin': '282235'
    }
    ,

    'login_form': {

        'user': "//input[(@name='usuario')]",
        'enterprise_id': '',
        'pin': "//input[(@name='password_PAS')]",
        'submit': "//input[(@name='enviar')]"
    }
    ,
    #periodicidad de las consultas ( @TBD )
    'checking_time': ''
    ,

    'workflow': [
                 # click con condiciones de espera
                 {'tipo': 'class', 'target': "//td[(@scope='row')]/a", 'expect_cond': "//button[(@ng-click='showSearch = !showSearch')]",
                  'mode': 'click'},

                 # click sobre la lupa (sin condiciones de espera)

                 {'xpath': "//button[(@ng-click='showSearch = !showSearch')]",
                  'mode': 'click'},
                 #el fill de un text input
                 {'xpath': "//input[(@name='daysimpleDateFrom')]", 'mode': 'fill', 'data': '06'},

                 ]

}
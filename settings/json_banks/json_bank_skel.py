bankia = {

    'url_base': 'https://oficinaempresas.bankia.es/bole/es/',

    'login_url': 'https://oficinaempresas.bankia.es/es/login.html',

    #add login_method
    'credentials': {
        'user': '',
        'enterprise_id': '',
        'pin': ''
    }
    ,
    'login_form': {
        # son ids, cambiar por xpath
        'user': 'nUsuario',
        'enterprise_id': 'nContrato',
        'pin': 'pass2',
        'submit': "//input[(@value='Entrar')]"
    }
    ,
    # posibles ventanas molestas...tipo aceotar cookies
    # el orden de los dnd varía seun entidad, aparecen antes / dp del login !
    'dnd': {'modal-dialog': "//button[(@title='Cerrar')]"}
    ,
    'checking_time': ''
    ,
    # elemento sobre el q interactuar / condicion posterior de espera para continuar el wf
    'workflow': [{'xpath': "//td[(@scope='row')]/a", 'expect_cond': "//button[(@ng-click='showSearch = !showSearch')]",
                  'mode': 'click'},
                 # click sobre la lupa
                 {'xpath': "//button[(@ng-click='showSearch = !showSearch')]",
                  'mode': 'click'},
                 # formulario de busqueda
                 # desde
                 {'xpath': "//input[(@name='daysimpleDateFrom')]", 'mode': 'fill', 'data': '06'},
                 {'xpath': "//input[(@name='monthsimpleDateFrom')]", 'mode': 'fill', 'data': '06'},
                 {'xpath': "//input[(@name='yearsimpleDateFrom')]", 'mode': 'fill', 'data': '2019'},
                 # hasta
                 {'xpath': "//input[(@name='daysimpleDateTo')]", 'mode': 'fill', 'data': '15'},
                 {'xpath': "//input[(@name='monthsimpleDateTo')]", 'mode': 'fill', 'data': '06'},
                 {'xpath': "//input[(@name='yearsimpleDateTo')]", 'mode': 'fill', 'data': '2019'},
                 #boton buscar
                 {'xpath': "//button[(@class='oie2-btn btn-green bk-button')]",
                  'mode': 'click'},
                 # descargar
                 {'xpath':"//button[(@ng-click='showDropdown = !showDropdown')]",
                                  'mode': 'click'},

                 #link descargar en excel
                 {'xpath': "//a[(@title='Exportar a Excel')]",
                  'mode': 'click'}

                 ]

}

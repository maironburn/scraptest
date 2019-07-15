import requests
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1


class Authenticator(object):
    _auth_entry_point = ''
    _user = None
    _pwd = None
    _status_code = None
    _response = None


    def __init__(self, **kw):
        self._auth_entry_point = kw.get("entry_point")
        self._user = kw.get("user")
        self._pwd = kw.get("pwd")

        self.auth_types = {'basic_auth': HTTPBasicAuth(self._user, self._pwd),
                           'digest_auth': HTTPDigestAuth(self._user, self._pwd),
                           ''' pip install requests-oauthlib '''
                           'oauth_auth': OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                                                'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
                           }

    def do_the_auth(self, auth_mode):
        if auth_mode and auth_mode in self.auth_types:
            self._response = requests.get(self._auth_entry_point, auth=self.auth_types[auth_mode])
            self._status_code = self._response.status_code

    # <editor-fold desc="Getter / Setters ">

    @property
    def entry_point(self):
        return self._auth_entry_point

    @entry_point.setter
    def entry_point(self, value):
        if value:
            self._auth_entry_point = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if value:
            self._user = value

    @property
    def pwd(self):
        return self._pwd

    @pwd.setter
    def pwd(self, value):
        if value:
            self._pwd = value

    @property
    def response(self):
        return self.response

    @response.setter
    def response(self, value):
        if value:
            self._response = value

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        if value:
            self._status_code = value

    # </editor-fold>

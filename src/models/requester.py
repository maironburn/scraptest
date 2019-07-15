



class Requester(object):


    _payload={}

    def __init__(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        self._payload = ''


    def query_get(self, payload= None):

        r = requests.get("http://httpbin.org/get", params=payload)
class TagStruct(object):
    _item_list = []
    _bs = None
    _root_info = None
    _handler_class = None

    def __init__(self, **kw):

        if 'bs' in kw.keys() and kw.get('bs'):
            self._bs = kw.get('bs')
            self.load_root(kw.get('load_root'))

    def load_root(self, root):
        self._root_info = self._bs.findAll("div", {"class": "imagen-post"})

    @property
    def plain_name_items(self):
        self._item_list = self._bs.findAll("div", {"class": "bloque-inferior"})

    def fill_info(self):
        for i in self._root:
            self._handler_class.href = i.find('a').get('href')


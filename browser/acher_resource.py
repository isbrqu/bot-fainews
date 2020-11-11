from models import TypeResource

types_resource = TypeResource.sort().get()

class Resource:
    
    def __init__(self, a):
        self.tag = a
        self.__name = None
        self.__url = None
        self.__type_resource = None

    @property
    def name(self):
        if not self.__name:
            self.__name = self.tag.get_text()
        return self.__name

    @property
    def url(self):
        if not self.__url:
            self.__url = self.tag['href']
        return self.__url

    @property
    def type_resource(self):
        if not self.__type_resource:
            self.__type_resource = self.__identifiy_type_of_resource(self.url)
        return self.__type_resource

    def __identifiy_type_of_resource(self, url):
        for tr in types_resource:
            if tr.identificador:
                for iden in tr.identificador.split():
                    if iden in url:
                        return tr.idTipoRecurso
            else:
                return tr.idTipoRecurso


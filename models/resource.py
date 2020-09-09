from orator import Model
# from orator.orm import scope

class Resource(Model):

    __table__ = 'recurso'
    __timestamps__ = False
    __primary_key__ = 'idRecurso'

    @classmethod
    def not_loaded(cls, mod):
        return cls().new_query_without_scopes()\
            .select('idTipoRecurso')\
            .where('url', mod['url'])\
            .where('idMateria', mod['idMateria'])\
            .where('idTipoRecurso', mod['idTipoRecurso'])\
            .first() == None


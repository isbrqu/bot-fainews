from orator import Model
from orator.orm import scope

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

    @scope
    def joinCourse(self, query):
        return query.join('materia',
            'recurso.idMateria', '=', 'materia.idMateria')

    @scope
    def joinTypeResource(self, query):
        return query.join('tipoRecurso',
            'recurso.idTipoRecurso', '=', 'tipoRecurso.idTipoRecurso')

    @scope
    def not_sent(self, query):
        return query.where('enviado', False)

    @scope
    def sort(self, query):
        return query\
            .order_by('recurso.idMateria')\
            .order_by('recurso.idTipoRecurso')


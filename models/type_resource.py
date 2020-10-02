from orator import Model
from orator.orm import scope

class TypeResource(Model):

    __table__ = 'tipoRecurso'
    __timestamps__ = False
    __primary_key__ = 'idTipoRecurso'

    @scope
    def sort(self, query):
        return query\
            .order_by('idTipoRecurso')


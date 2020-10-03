from decouple import config
from orator.orm import Model, accessor

URL_COURSE = config('URL_BASE') + 'course/view.php?id=%d'

class Course(Model):

    __table__ = 'materia'
    __timestamps__ = False
    __primary_key__ = 'idMateria'

    @accessor
    def url(self):
        return URL_COURSE % self.get_raw_attribute('numeroUrl')

    @accessor
    def name(self):
        return self.get_raw_attribute('nombre')

    @classmethod
    def everyone_in_the_period(cls, period):
        return cls().new_query_without_scopes()\
            .where('cuatrimestre', period)\
            .or_where('esRecursable', True)\
            .get()


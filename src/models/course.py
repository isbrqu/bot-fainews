import config
from orator.orm import Model, accessor

class Course(Model):

    __table__ = 'courses'
    __timestamps__ = False
    __primary_key__ = 'id'

    @accessor
    def url(self):
        return config.telegram.url_course % self.get_raw_attribute('numeroUrl')

    @classmethod
    def first_period(cls):
        return cls().new_query_without_scopes()\
            .where('cuatrimestre', 1)\
            .or_where('esRecursable', True)\
            .get()

    @classmethod
    def second_period(cls):
        return cls().new_query_without_scopes()\
            .where('cuatrimestre', 2)\
            .or_where('esRecursable', True)\
            .get()


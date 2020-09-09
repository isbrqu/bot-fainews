from orator.orm import Model, accessor

URL_BASE = 'https://pedco.uncoma.edu.ar/'
URL_COURSE = URL_BASE + 'course/view.php?id=%d'

class Course(Model):

    __table__ = 'materia'
    __timestamps__ = False
    __primary_key__ = 'idMateria'

    @accessor
    def url(self):
        return URL_COURSE % self.get_raw_attribute('numeroUrl')


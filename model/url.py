from orator import Model
from orator.orm import scope

class Url(Model):

    __table__ = 'urls'
    __timestamps__ = False

    @scope
    def of_subject(self, query, subject):
        return query.where('subject_id', subject.id)

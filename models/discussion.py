from orator import Model
from orator.orm import scope

class Discussion(Model):

    __table__ = 'discusion'
    __timestamps__ = False

    @scope
    def last(self, query):
        return query.order_by('id', 'desc').first()

    @scope
    def of_subject(self, query, subject):
        return query.where('subject_id', subject.id)

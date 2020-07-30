from orator import Model

class Subject(Model):

    __table__ = 'subjects'
    __timestamps__ = False

    # TODO: crea método para completar la url para acceder a al board
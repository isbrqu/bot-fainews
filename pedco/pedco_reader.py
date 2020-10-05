from models import Resource, Discussion

class PedcoReader:

    def __init__(self):
        pass

    @property
    def discussions_not_sent(self):
        return Discussion.select(
            'discusion.idDiscusion',
            'discusion.nombre as name',
            'discusion.autor',
            'materia.nombre as course',
        ).joinForum()\
        .joinCourse()\
        .not_sent()\
        .sort()\
        .get()

    @property
    def resources_not_sent(self):
        return Resource.select(
            'recurso.idRecurso',
            'recurso.nombre as name',
            'recurso.url',
            'materia.nombre as course',
            'tipoRecurso.nombre as typer',
            'tipoRecurso.mensaje as msg'
        ).joinCourse()\
        .joinTypeResource()\
        .not_sent()\
        .sort()\
        .get()


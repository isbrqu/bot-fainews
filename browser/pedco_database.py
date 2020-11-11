from models import Resource, Discussion
from models import Course, Forum

class PedcoDatabase:

    def __init__(self):
        self.courses1 = Course.everyone_in_the_period(1)
        self.courses2 = Course.everyone_in_the_period(2)

    @property
    def courses(self):
        return (self.courses1 if self.period == 1 else self.courses2)

    @property
    def forums(self):
        return Forum.everyone_in_the_period(self.period)

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

    def save_discussion(self, forum, tr):
        new = HDiscussion(tr)
        old = Discussion.with_url_id(new.url_id).first()
        if not old:
            Discussion.insert({
                'nombre': new.name,
                'numeroUrl': new.url_id,
                'enviado': False,
                'rutaFoto': '',
                'autor': new.author,
                'creado': new.created,
                'actualizado': new.updated,
                'idForo': forum.idForo
            })
        elif old.actualizado != new.updated:
            old.actualizado = new.updated
            old.enviado = False
            old.save()

    def save_resource(self, course, a):
        resource = HDiscussion(a)
        mod = {
            'nombre': resource.name,
            'url': resource.url,
            'enviado': False,
            'idMateria': course.idMateria,
            'idTipoRecurso': resource.type_resource
        }
        if Resource.not_loaded(mod):
            Resource.insert(mod)


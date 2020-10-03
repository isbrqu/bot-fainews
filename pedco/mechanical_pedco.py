from datetime import datetime
from models import Course
from models import Resource
from models import TypeResource
from models import Forum
from models import Discussion
from .mechanical_moodle import MechanicalMoodle
from .hdiscussion import HDiscussion

class MechanicalPedco(MechanicalMoodle):

    def __init__(self):
        super().__init__()
        self.courses1 = Course.everyone_in_the_period(1)
        self.courses2 = Course.everyone_in_the_period(2)
        self.types_resource = TypeResource.sort().get()

    # COURSE

    @property
    def courses(self):
        return (self.courses1 if self.period == 1 else self.courses2)

    def update_resources(self):
        for course in self.courses:
            self.open_with_session(course.url)
            print(f'course: {course.name}')
            for a in self.page.select('#region-main a[href]'):
                url = a['href']
                mod = {
                    'nombre': a.get_text(),
                    'url': url,
                    'enviado': False,
                    'idMateria': course.idMateria,
                    'idTipoRecurso': self.__identifiy_type_of_resource(url)
                }
                if Resource.not_loaded(mod):
                    Resource.insert(mod)

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

    # DISCUSSION

    @property
    def forums(self):
        return Forum.everyone_in_the_period(self.period)

    def update_discussions(self):
        for forum in self.forums:
            self.open_with_session(forum.url)
            print(f'forum: {forum.name}')
            for tr in self.page.select('tr.discussion'):
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

    def __identifiy_type_of_resource(self, url):
        for tr in self.types_resource:
            if tr.identificador:
                for iden in tr.identificador.split():
                    if iden in url:
                        return tr.idTipoRecurso
            else:
                return tr.idTipoRecurso


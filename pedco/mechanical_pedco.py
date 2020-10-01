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
        self.courses1 = Course.first_period()
        self.courses2 = Course.second_period()
        self.types_resource = TypeResource.order_by('idTipoRecurso').get()

    @property
    def new_resources(self):
        return Resource.select(
            'recurso.idRecurso',
            'recurso.nombre as name',
            'recurso.url',
            'materia.nombre as course',
            'tipoRecurso.nombre as typer',
            'tipoRecurso.mensaje as msg'
        ).join('materia', 'recurso.idMateria', '=', 'materia.idMateria')\
        .join('tipoRecurso', 'recurso.idTipoRecurso', '=', 'tipoRecurso.idTipoRecurso')\
        .where('enviado', False)\
        .order_by('recurso.idMateria')\
        .order_by('recurso.idTipoRecurso')\
        .get()

    @property
    def current_courses(self):
        if datetime.now().month < 6:
            return self.courses1
        else:
            return self.courses2

    @property
    def forums(self):
        if datetime.now().month < 6:
            return Forum.first_period()
        else:
            return Forum.second_period()

    def update_resources(self):
        for course in self.current_courses:
            self.open_with_session(course.url)
            for a in self.page.select('#region-main a[href]'):
                url = a['href']
                mod = {
                    'nombre': a.get_text(),
                    'url': url,
                    'enviado': False,
                    'idMateria': course.idMateria,
                    'idTipoRecurso': self._identifiy_type_of_resource(url)
                }
                if Resource.not_loaded(mod):
                    Resource.insert(mod)
            print(f'OK - {course.idMateria} -> {course.nombre}')

    def update_discussions(self):
        for forum in self.forums:
            self.open_with_session(forum.url)
            print(f'abriendo: {forum.nombre}, {forum.url}, {forum.activo}, {forum.materia}')
            for tr in self.page.select('tr.discussion'):
                new = HDiscussion(tr)
                old = Discussion.where('numeroUrl', new.url_id).first()
                if not old:
                    Discussion.insert({
                        'nombre': new.name,
                        'numeroUrl': new.url_id,
                        'enviado': False,
                        'autor': new.author,
                        'creado': new.created,
                        'actualizado': new.updated,
                        'idForo': forum.idForo
                    })
                elif old.actualizado != new.updated:
                    old.actualizado = new.updated
                    old.enviado = False
                    old.save()

    def _identifiy_type_of_resource(self, url):
        for tr in self.types_resource:
            if tr.identificador:
                for iden in tr.identificador.split():
                    if iden in url:
                        return tr.idTipoRecurso
            else:
                return tr.idTipoRecurso


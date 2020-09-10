from mechanicalsoup import StatefulBrowser
from datetime import datetime
import time

from models import Course
from models import Resource
from models import TypeResource

URL_BASE = 'https://pedco.uncoma.edu.ar/'
URL_LOGIN = URL_BASE + 'login/index.php'
URL_HOME = URL_BASE + 'my/'
URL_COURSE = URL_BASE + 'course/view.php?id=%d'
URL_FORUM = URL_BASE + 'mod/forum/view.php?id=%d'
TITLE_LOGIN = 'PEDCO: Entrar al sitio'

class Mechanical(StatefulBrowser):

    def __init__(self, subjects=[]):
        super().__init__()
        self.courses1 = Course.first_period()
        self.courses2 = Course.second_period()
        self.types_resource = TypeResource.order_by('idTipoRecurso').get()

    @property
    def page(self):
        return super().get_current_page()

    @property
    def url(self):
        return self.get_url()

    @property
    def title(self):
        return self.page.title.text

    @property
    def in_login(self):
        return (self.url == URL_LOGIN)

    @property
    def logged_in(self):
        return not self.in_login

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

    def open(self, url):
        success = False
        while not success:
            try:
                super().open(url, timeout=5)
                success = True
            except Exception as e:
                print(e)
                time.sleep(2)
        return success

    def open_with_session(self, url):
        success = False
        while not success:
            if self.in_login:
                print('se ha cerrado la sesión')
                self.loginenv()
            else:
                success = True
                self.open(url)
        return success

    def login(self, username, password):
        self.open(URL_LOGIN)
        if self.page.find('h4'):
            self.select_form(nr=1)
        else:
            self.select_form()
            self['username'] = username
            self['password'] = password
        self.submit_selected()
        success = self.logged_in
        return success

    @property
    def current_courses(self):
        if datetime.now().month < 6:
            return self.courses1
        else:
            return self.courses2

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

    def _identifiy_type_of_resource(self, url):
        for tr in self.types_resource:
            if tr.identificador:
                for iden in tr.identificador.split():
                    if iden in url:
                        return tr.idTipoRecurso
            else:
                return tr.idTipoRecurso


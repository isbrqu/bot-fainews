from models import Resource, Discussion 
from .hdiscussion import HDiscussion
from .hressource import HResource

class PedcoWriter:
    
    def __init__(self):

    def resource(self, course, a):
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

    def discussion(self, forum, tr):
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


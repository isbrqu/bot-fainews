from orator.seeds import Seeder


class TypeResourceTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('tipoRecurso').insert([
            {
                'nombre': 'data',
                'descripcion': 'Base de datos',
                'mensaje': 'Se ha subido una base de datos',
                'identificador': '/mod/data/view',
            },
            {
                'nombre': 'bigbluebuttonbn',
                'descripcion': 'BigBlueButtonBN',
                'mensaje': 'Se ha creado una BigBlueButtonBN',
                'identificador': '/mod/bigbluebuttonbn/view',
            },
            {
                'nombre': 'chat',
                'descripcion': 'Chat',
                'mensaje': 'Se habilitó un chat',
                'identificador': '/mod/chat/view',
            },
            {
                'nombre': 'choice',
                'descripcion': 'Consulta',
                'mensaje': 'Se creo un modulo de consulta',
                'identificador': '/mod/choice/view',
            },
            {
                'nombre': 'quiz',
                'descripcion': 'Cuestionario',
                'mensaje': 'Se habilitó un cuestionario para realizar',
                'identificador': '/mod/quiz/view',
            },
            {
                'nombre': 'journal',
                'descripcion': 'Diario',
                'mensaje': 'Se a creado un diario',
                'identificador': '/mod/journal/view',
            },
            {
                'nombre': 'feedback',
                'descripcion': 'Encuesta',
                'mensaje': 'Se habilitó una encuesta',
                'identificador': '/mod/feedback/view',
            },
            {
                'nombre': 'survey',
                'descripcion': 'Encuestas predefinidas',
                'mensaje': 'Se habilitó una encuesta predefinida',
                'identificador': '/mod/survey/view',
            },
            {
                'nombre': 'forum',
                'descripcion': 'Foro',
                'mensaje': 'Se creó un nuevo foro',
                'identificador': '/mod/forum/view',
            },
            {
                'nombre': 'glossary',
                'descripcion': 'Glosario',
                'mensaje': 'Se habilitó un glosario',
                'identificador': '/mod/glossary/view',
            },
            {
                'nombre': 'lti',
                'descripcion': 'Herramienta Externa',
                'mensaje': 'Se subió una herramienta externa',
                'identificador': '/mod/lti/view',
            },
            {
                'nombre': 'hotpot',
                'descripcion': 'HotPot',
                'mensaje': 'Se creo un nuevo HotPot',
                'identificador': '/mod/hotpot/view',
            },
            {
                'nombre': 'jitsi',
                'descripcion': 'Jitsi',
                'mensaje': 'Se habilitó un Jitsi',
                'identificador': '/mod/jitsi/view',
            },
            {
                'nombre': 'lesson',
                'descripcion': 'Lección',
                'mensaje': 'Se ha creado una lección',
                'identificador': '/mod/lesson/view',
            },
            {
                'nombre': 'scorm',
                'descripcion': 'Paquete SCROM',
                'mensaje': 'Se ha creado un paquete SCROM',
                'identificador': '/mod/scorm/view',
            },
            {
                'nombre': 'workshop',
                'descripcion': 'Taller',
                'mensaje': 'Se habilitó un Taller',
                'identificador': '/mod/workshop/view',
            },
            {
                'nombre': 'assign',
                'descripcion': 'Tarea',
                'mensaje': 'Se a creado una tarea para entregar',
                'identificador': '/mod/assign/view',
            },
            {
                'nombre': 'wiki',
                'descripcion': 'Wiki',
                'mensaje': 'Se habilitó una wiki',
                'identificador': '/mod/wiki/view',
            },
            {
                'nombre': 'resource',
                'descripcion': 'Archivo',
                'mensaje': 'Se ha subidó un nuevo archivo',
                'identificador': '/mod/resource/view /pluginfile.php/',
            },
            {
                'nombre': 'folder',
                'descripcion': 'Carpeta',
                'mensaje': 'Se ha creado una carpeta',
                'identificador': '/mod/folder/view',
            },
            {
                'nombre': 'label',
                'descripcion': 'Etiqueta',
                'mensaje': 'Se ha creado una etiqueta',
                'identificador': '/mod/label/view',
            },
            {
                'nombre': 'book',
                'descripcion': 'Libro',
                'mensaje': 'Se habilitó un nuevo libro',
                'identificador': '/mod/book/view',
            },
            {
                'nombre': 'page',
                'descripcion': 'Página',
                'mensaje': 'Se a creado una página',
                'identificador': '/mod/page/view',
            },
            {
                'nombre': 'imscp',
                'descripcion': 'Paquete de conenido IMS',
                'mensaje': 'Se ha subido un paquete de conenido IMS',
                'identificador': '/mod/imscp/view',
            },
            {
                'nombre': 'url',
                'descripcion': 'URL',
                'mensaje': 'Se ha proporcionado una URL',
                'identificador': '/mod/url/view',
            },
            {
                'nombre': 'youtube',
                'descripcion': 'YouTube',
                'mensaje': 'Se ha subido un video de YouTube',
                'identificador': 'youtu.be youtube.com',
            },
            {
                'nombre': 'meet',
                'descripcion': 'Google Meet',
                'mensaje': 'Se a proporcionado un enlace meet',
                'identificador': 'meet.google.com',
            },
            {
                'nombre': 'unknow',
                'descripcion': 'Desconocido',
                'mensaje': 'Se a proporcionado un recurso no identificado',
                'identificador': '',
            },
        ])


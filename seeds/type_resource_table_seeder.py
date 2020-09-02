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
            },
            {
                'nombre': 'bigbluebuttonbn',
                'descripcion': 'BigBlueButtonBN',
                'mensaje': 'Se ha creado una BigBlueButtonBN',
            },
            {
                'nombre': 'chat',
                'descripcion': 'Chat',
                'mensaje': 'Se habilitó un chat',
            },
            {
                'nombre': 'choice',
                'descripcion': 'Consulta',
                'mensaje': 'Se creo un modulo de consulta',
            },
            {
                'nombre': 'quiz',
                'descripcion': 'Cuestionario',
                'mensaje': 'Se habilitó un cuestionario para realizar',
            },
            {
                'nombre': 'journal',
                'descripcion': 'Diario',
                'mensaje': 'Se a creado un diario',
            },
            {
                'nombre': 'feedback',
                'descripcion': 'Encuesta',
                'mensaje': 'Se habilitó una encuesta',
            },
            {
                'nombre': 'survey',
                'descripcion': 'Encuestas predefinidas',
                'mensaje': 'Se habilitó una encuesta predefinida',
            },
            {
                'nombre': 'forum',
                'descripcion': 'Foro',
                'mensaje': 'Se creó un nuevo foro',
            },
            {
                'nombre': 'glossary',
                'descripcion': 'Glosario',
                'mensaje': 'Se habilitó un glosario',
            },
            {
                'nombre': 'lti',
                'descripcion': 'Herramienta Externa',
                'mensaje': 'Se subió una herramienta externa',
            },
            {
                'nombre': 'hotpot',
                'descripcion': 'HotPot',
                'mensaje': 'Se creo un nuevo HotPot',
            },
            {
                'nombre': 'jitsi',
                'descripcion': 'Jitsi',
                'mensaje': 'Se habilitó un Jitsi',
            },
            {
                'nombre': 'lesson',
                'descripcion': 'Lección',
                'mensaje': 'Se ha creado una lección',
            },
            {
                'nombre': 'scorm',
                'descripcion': 'Paquete SCROM',
                'mensaje': 'Se ha creado un paquete SCROM',
            },
            {
                'nombre': 'workshop',
                'descripcion': 'Taller',
                'mensaje': 'Se habilitó un Taller',
            },
            {
                'nombre': 'assign',
                'descripcion': 'Tarea',
                'mensaje': 'Se a creado una tarea para entregar',
            },
            {
                'nombre': 'wiki',
                'descripcion': 'Wiki',
                'mensaje': 'Se habilitó una wiki',
            },
            {
                'nombre': 'resource',
                'descripcion': 'Archivo',
                'mensaje': 'Se ha subidó un nuevo archivo',
            },
            {
                'nombre': 'folder',
                'descripcion': 'Carpeta',
                'mensaje': 'Se ha creado una carpeta',
            },
            {
                'nombre': 'label',
                'descripcion': 'Etiqueta',
                'mensaje': 'Se ha creado una etiqueta',
            },
            {
                'nombre': 'book',
                'descripcion': 'Libro',
                'mensaje': 'Se habilitó un nuevo libro',
            },
            {
                'nombre': 'page',
                'descripcion': 'Página',
                'mensaje': 'Se a creado una página',
            },
            {
                'nombre': 'imscp',
                'descripcion': 'Paquete de conenido IMS',
                'mensaje': 'Se ha subido un paquete de conenido IMS',
            },
            {
                'nombre': 'url',
                'descripcion': 'URL',
                'mensaje': 'Se ha proporcionado una URL',
            },
            {
                'nombre': 'youtube',
                'descripcion': 'YouTube',
                'mensaje': 'Se ha subido un video de YouTube',
            },
            {
                'nombre': 'meet',
                'descripcion': 'Google Meet',
                'mensaje': 'Se a proporcionado un enlace meet',
            },
            {
                'nombre': 'unknow',
                'descripcion': 'Desconocido',
                'mensaje': 'Se a proporcionado un recurso no identificado',
            },
        ])


from orator.seeds import Seeder


class CourseTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('materia').insert([
            {
                'nombre': 'Cálculo Diferencial e Integral',
                'ano': 2,
                'cuatrimestre': 1,
                'alias': 'calculo-diferencial-e-integral',
                'numeroUrl': 1891,
                'esRecursable': False,
            },
            {
                'nombre': 'Estructuras de Datos',
                'ano': 2,
                'cuatrimestre': 1,
                'alias': 'estructuras-de-datos',
                'numeroUrl': 241,
                'esRecursable': False,
            },
            {
                'nombre': 'Inglés Técnico 1',
                'ano': 2,
                'cuatrimestre': 1,
                'alias': 'ingles-tecnico-1',
                'numeroUrl': 665,
                'esRecursable': False,
            },
            {
                'nombre': 'Teoría de la Computación 1',
                'ano': 2,
                'cuatrimestre': 1,
                'alias': 'teoria-de-la-computacion-1',
                'numeroUrl': 1865,
                'esRecursable': False,
            },
            {
                'nombre': 'Programación Orientada a Objetos',
                'ano': 2,
                'cuatrimestre': 1,
                'alias': 'programacion-orientada-a-objetos',
                'numeroUrl': 246,
                'esRecursable': False,
            },
            {
                'nombre': 'Ingeniería de Requerimientos',
                'ano': 2,
                'cuatrimestre': 2,
                'alias': 'ingenieria-de-requerimientos',
                'numeroUrl': 2006,
                'esRecursable': False,
            },
            {
                'nombre': 'Métodos Computacionales para el Cálculo',
                'ano': 2,
                'cuatrimestre': 2,
                'alias': 'métodos-computacionales-para-el-cálculo',
                'numeroUrl': 2036,
                'esRecursable': False,
            },
            {
                'nombre': 'Teoría de la Computación 2',
                'ano': 2,
                'cuatrimestre': 2,
                'alias': 'teoría-de-la-computación-2',
                'numeroUrl': 2013,
                'esRecursable': False,
            },
            {
                'nombre': 'Arquitecturas y Organización de Computadoras 1',
                'ano': 2,
                'cuatrimestre': 2,
                'alias': 'arquitecturas-y-organización-de-computadoras-1',
                'numeroUrl': 2052,
                'esRecursable': False,
            },
            {
                'nombre': 'Programación Concurrente',
                'ano': 2,
                'cuatrimestre': 2,
                'alias': 'programación-concurrente',
                'numeroUrl': 2059,
                'esRecursable': False,
            }
        ])


from orator.migrations import Migration


class CreateCoursesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('materia') as table:
            table.increments('idMateria')
            table.string('nombre', 250)
            table.integer('ano').unsigned()
            table.integer('cuatrimestre').unsigned()
            table.string('alias', 100).unique()
            table.integer('numeroUrl').unsigned()
            table.boolean('esRecursable')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('materia')

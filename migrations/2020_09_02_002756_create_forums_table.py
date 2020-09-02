from orator.migrations import Migration


class CreateForumsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('foro') as table:
            table.increments('idForo')
            table.string('nombre', 100)
            table.integer('numeroUrl')
            table.boolean('activo')
            table.integer('idMateria').unsigned()
            table.foreign('idMateria')\
                .references('idMateria').on('materia')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('foro')

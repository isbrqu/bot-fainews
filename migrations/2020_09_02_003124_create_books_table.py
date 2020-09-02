from orator.migrations import Migration


class CreateBooksTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('libro') as table:
            table.increments('idLibro')
            table.string('nombre', 250)
            table.integer('numeroUrl').unsigned().unique()
            table.boolean('activo')
            table.integer('idMateria').unsigned()
            table.foreign('idMateria')\
                .references('idMateria').on('materia')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('libro')

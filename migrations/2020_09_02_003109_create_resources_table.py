from orator.migrations import Migration


class CreateResourcesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('recurso') as table:
            table.increments('idRecurso')
            table.string('nombre', 250)
            table.string('url', 250)
            table.boolean('enviado')
            table.integer('idMateria').unsigned()
            table.foreign('idMateria')\
                .references('idMateria').on('materia')\
                .on_delete('cascade')
            table.integer('idTipoRecurso').unsigned()
            table.foreign('idTipoRecurso')\
                .references('idTipoRecurso').on('tipoRecurso')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('recurso')

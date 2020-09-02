from orator.migrations import Migration


class CreateTypeResourcesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tipoRecurso') as table:
            table.increments('idTipoRecurso')
            table.string('nombre', 250).unique()
            table.string('descripcion', 250)
            table.string('mensaje', 250)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tipoRecurso')

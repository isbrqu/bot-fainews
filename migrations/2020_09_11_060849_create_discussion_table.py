from orator.migrations import Migration


class CreateDiscussionTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('discusion') as table:
            table.increments('idDiscusion')
            table.string('nombre', 250)
            table.integer('numeroUrl').unsigned()
            table.boolean('enviado')
            table.string('rutaFoto', 250)
            table.string('autor', 100)
            table.string('creado', 50)
            table.string('actualizado', 50)
            table.integer('idForo').unsigned()
            table.foreign('idForo')\
                .references('idForo').on('foro')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('discusion')

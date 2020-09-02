from orator.migrations import Migration


class CreateChaptersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('capitulo') as table:
            table.increments('idCapitulo')
            table.string('nombre', 250)
            table.integer('numeroUrl').unsigned()
            table.boolean('enviado')
            table.integer('idLibro').unsigned()
            table.foreign('idLibro')\
                .references('idLibro').on('libro')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('capitulo')

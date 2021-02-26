from orator.migrations import Migration


class CreatePagesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('pages') as table:
            table.increments('id')
            table.string('name')
            table.timestamp('created_at')
            table.integer('book_id').unsigned()
            table.foreign('book_id')\
                .references('id').on('books')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('pages')

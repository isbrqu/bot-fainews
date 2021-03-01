from orator.migrations import Migration


class CreateChaptersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('chapters') as table:
            table.primary('id')
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

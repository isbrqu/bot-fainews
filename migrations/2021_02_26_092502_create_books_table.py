from orator.migrations import Migration


class CreateBooksTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('books') as table:
            table.integer('id').unsigned()
            table.primary('id')
            table.string('name')
            table.timestamps()
            table.integer('course_id').unsigned()
            table.foreign('course_id')\
                .references('id').on('courses')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('books')

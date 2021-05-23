from orator.migrations import Migration


class CreateCoursesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('courses') as table:
            table.increments('id')
            table.string('name')
            table.string('alias')
            table.integer('category_id').unsigned()
            table.foreign('category_id')\
                .references('id').on('categories')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('courses')

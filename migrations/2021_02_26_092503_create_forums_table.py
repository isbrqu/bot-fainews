from orator.migrations import Migration


class CreateForumsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('forums') as table:
            table.increments('id')
            table.string('name')
            table.timestamps()
            table.integer('user_id').unsigned()
            table.foreign('user_id')\
                .references('id').on('users')\
                .on_delete('cascade')
            table.integer('course_id').unsigned()
            table.foreign('course_id')\
                .references('id').on('courses')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('forums')

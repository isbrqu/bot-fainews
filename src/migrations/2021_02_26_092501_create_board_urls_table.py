from orator.migrations import Migration


class CreateBoardUrlsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('board_urls') as table:
            table.increments('id')
            table.string('name')
            table.string('url')
            table.timestamp('created_at')
            table.integer('course_id').unsigned()
            table.foreign('course_id')\
                .references('id').on('courses')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('board_urls')

from orator.migrations import Migration


class CreateDiscussionsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('discussions') as table:
            table.primary('id')
            table.string('name')
            table.timestamps()
            table.integer('forum_id').unsigned()
            table.foreign('forum_id')\
                .references('id').on('forums')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('discussions')

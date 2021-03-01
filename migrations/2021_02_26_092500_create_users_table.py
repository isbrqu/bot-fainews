from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.integer('id').unsigned()
            table.primary('id')
            table.string('name')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')

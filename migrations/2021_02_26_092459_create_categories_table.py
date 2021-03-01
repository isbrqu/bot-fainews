from orator.migrations import Migration


class CreateCategoriesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('categories') as table:
            table.integer('id').unsigned()
            table.primary('id')
            table.string('name')
            table.integer('category_id').unsigned()
            table.foreign('category_id')\
                .references('id').on('categories')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('categories')

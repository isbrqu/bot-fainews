class Subject(object):
	"""docstring for Subject"""
	def __init__(self, name, course, alias, forum):
		self.name = name
		self.alias = alias
		self.course = 'https://pedco.uncoma.edu.ar/course/view.php?id=' + course
		self.forum = 'https://pedco.uncoma.edu.ar/mod/forum/view.php?id=' + forum

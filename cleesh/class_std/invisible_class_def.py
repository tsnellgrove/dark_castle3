# program: dark castle
# author: Tom Snellgrove
# module description: Invisible class deffinition module


### classes
class Invisible(object):
	def __init__(self, name):
		self._name = name # text str of each obj's canonical name; should be unique and immutable
		""" Invisible is the root object class. There are no instantiated objects of class Invisible 
		but all objects in the game inherit the name attribute and their obj print capabilities from Invisible. 
		"""

	# *** getters & setters ***
	@property
	def name(self):
		return self._name

	# *** abstract identity methods needed for room.get_mach_lst() ***
	def is_timer(self):
		return False

	def is_mach(self):
		return False

	# *** obj representation def ***
	def __repr__(self):
		return f"Object {self.name} is of class {type(self).__name__}"
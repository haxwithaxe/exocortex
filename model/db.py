class Record:
	""" Database Record model"""
	default_values = {}

	def __init__(self, **values):
		self.values = values or {}

	def get(self):
		""" Get the contents of the record """
		self._load_defaults()
		return self.values

	def _load_defaults(self):
		"""Load the default values so we don't pass any empty fields we don't want to be empty to the database backend"""
		# shallow copy the default values so we don't mangle it too much
		defaults = self.default_values.copy()
		# load the given values over the defaults
		defaults.update(self.values)
		# set values to be the updated dictionary
		self.values = defaults


class DB:
	""" Database model """
	
	def __init__(self, source):
		""" Set the database source """
		pass

	def open(self):
		""" Open and/or load the database object. """
		pass

	def get(self, **criteria):
		""" Find and return the Records that match the criteria. """
		pass

	def set(self, **records):
		""" Set the values for the matching Records or create one if there is no match. """
		pass

	def close(self):
		""" Close the DB object if required """
		pass

	def compact(self):
		"""For every database in database_directory, instantiate a copy of Compactor() and compact the database to free up disk space and make searches more efficient."""
		pass

	def _file_exists(self):
		""" Does the database file exist? """
		pass

	def exists(self):
		""" Does the database file and/or table exist """
		pass

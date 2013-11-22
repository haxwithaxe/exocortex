"""
This is the back-end that provides the information data for the UI by gathering collating findings.
"""

class MissingDB(Exception):
	pass

# Define Classes
class UDBI:
	"""Unified database interface"""
	def __init__(self):
		self.db_list = []
		pass

	def find(self, sources*, **criteria):
		""" Find database entries from all sources `sources` (if specified otherwise find from any source) with the key-value style criteria specified by `criteria` otherwise find all entries from the specified source.
		@param	sources		arguments specifying sources to query.
		@param	criteria	keyword arguments giving criteria for the query
		@return				dict of results [empty dict if no results]"""
		pass

	def _db_exist(self, source):
		"""	See if a required databases exist.
			@throws		MissingDB exception if a required db is not found
			@returns	bool
		"""
		pass

	def _open_all(self):
		"""For every directory in database_directory ...
		model.db.open directory"""
		# for each source db, append it to self.db_list and open it
		for db in self.sources:
			db = DB(db)
			if db.exists():
				db.open()
				self.db_list.append(db)

	def _end_search(self):
		""" Close the search connections to the databases. """
		pass

	def _clean_up(self):
		""" Clean up after ourselves. """
		pass

	def close(self):
		""" Close the databases. """
		pass


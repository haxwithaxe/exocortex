"""
URL Control (MVC)
"""

__authors__ = ["haxwithaxe <me at haxwithaxe dot net>"]

__license__ = "GPLv3"


class URL:
	def __init__(self, target):
		""" config is a model.Config object already loaded
			@param	target	a string or urllib2.Request object
		"""
		self.target = target
		self.validate_target()	#die hard if we don't have what we need

	def validate_target(self):
		""" Fail early ... Fail often ... Fail before production
			@throws		ValueError if self.target is not a string or urllib2.Request
		"""
		if not self.target or not isinstance(self.target, str) or not isinstance(self.target, urllib2.Request):
			raise ValueError("target must be a URI string or a urllib2.Request object.")

	def get(self, ignore_bad_cert=False):
		""" Get page from target.
		@param	ignore_bad_cert	bool, if true don't throw erros when ssl cert is invalid/selfsigned
		@return					the page retrieved or None if not found.
		"""
		pass

	def clean(self):
		""" Clean up files and open sockets or objects. """
		pass

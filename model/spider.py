"""
Web Spider model
"""

__authors__ = ["haxwithaxe <me at haxwithaxe dot net>"]

__license__ = "GPLv3"

from bot import *
from  actor_utils import *

TARGET_KEY = "target"

class WebSpider(Bot):
	def __init__(self, target, config):
		""" config is a model.Config object already loaded"""
		super.__init__(self, config)
		self.target = target

	def on_stop(self):
		""" Hook for doing any cleanup that should be done after the actor has processed the last message, and before the actor stops. """
		self.disconnect()
		self.clean()

	def on_receive(self, message):
		""" When a message is recieved decide what to do with it
			@param	message	(picklable dict) – the message to handle
			@return			anything that should be sent as a reply to the sender
		"""
		if TARGET_KEY in message:
			self.target = message[TARGET_KEY]
		else:
			super.on_receive(self, message)

	def clean(self):
		""" Clean up files and open sockets or objects. """
		pass

	def parse(self, page):
		""" Do stuff to parse the page for data and return that data """
		pass

	def dump(self, data):
		""" stick the data someplace """
		pass

	def download(self, path):
		""" download the uri made of self.target+path """
		pass


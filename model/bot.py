"""
Bot model
"""

__authors__ = ["haxwithaxe <me at haxwithaxe dot net>"]

__license__ = "GPLv3"

import pykka
from  ..util.actor import *

CONNECT = Action("connect")
DISCONNECT = Action("disconnect")

class Bot(pykka.ThreadingActor):
	def __init__(self, config):
		""" config is a model.Config object already loaded"""
		super(Bot, self).__init__()
		self.conf = conf

	def on_start(self):
		""" Hook for doing any setup that should be done after the actor is started, but before it starts processing messages. AKA the main loop """
		pass

	def on_stop(self):
		""" Hook for doing any cleanup that should be done after the actor has processed the last message, and before the actor stops. """
		self.disconnect()
		self.clean()
		pass

	def on_failure(self, exception_type, exception_value, traceback):
		""" Hook for doing any cleanup after an unhandled exception is raised, and before the actor stops. """
		logging.error(exception_type, exception_value, traceback)
		pass

	def on_receive(self, message):
		""" When a message is recieved decide what to do with it
			@param	message	(picklable dict) – the message to handle
			@return			anything that should be sent as a reply to the sender
		"""
		if message == DISCONNECT:
			self.disconnect()
		elif message == CONNECT:
			self.connect()
		elif message == CLEAN:
		else:
			return self._

	def connect(self):
		""" Connect to target. """
		pass

	def disconnect(self):
		""" Disconnect from target. """
		pass

	def clean(self):
		""" Clean up files and open sockets or objects. """
		pass

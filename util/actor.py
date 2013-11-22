"""
Actor Class Utilities
"""

__authors__ = ["haxwithaxe <me at haxwithaxe dot net>"]

__license__ = "GPLv3"

import pykka

class Message:
	key = 'message'
	def __init__(self, *args, **values):
		self.value = values
		self.value.update({key: ' '.join(str(args))})

class Action(Message):
	key = 'action'


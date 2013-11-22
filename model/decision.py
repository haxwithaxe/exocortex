"""
Decision making code interface
"""

class Decision:
	default_init_kwargs = {}
	def __init__(self, **kwargs):
		args_helper.handle_kwargs(kwargs, default_init_kwargs)
		self.certianty = kwargs['certianty']
		self.input = 
		self.result = 

class Decider:
	def __init__(self, *args, **kwars):
		pass

	def ask(self, *args, **kwargs):
		pass

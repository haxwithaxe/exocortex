"""
functions to help handle *args and **kwargs
"""

def handle_kwargs(kwargs, defaults):
	""" make sure that kwargs has all the values we need so we don't need to check as we go """
	defaults_copy = defaults.copy()
	defaults_copy.update(kwargs)
	return defaults_copy


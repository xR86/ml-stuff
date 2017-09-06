"""Summary
Utility package for data science tasks.
"""


# Boolean functions

def is_variable(var):
	"""Checks if the variable is saved in either local or global variables."""
	return ( var in locals() or var in globals() )

def is_saved(file_str):
	"""Checks if the file is saved locally"""
	from pathlib import Path
	return Path(file_str).is_file()


# Serializing functions - json

import json

def json_serialize(file_str, file_obj):
	"""Serializes object(prefferably dict) to json"""
	with open(file_str + '.json', 'w') as f:
		f.write(json.dumps(file_obj))

def json_deserialize(file_str):
	"""Deserialize file to dict"""
	if not is_saved(file_str + '.json'):
		raise('File does not exist !')
	with open(file_str + '.json', 'r') as f:
		return json.loads(f.read())


# Serializing functions - pickle

import pickle

def pickle_serialize(file_str, file_obj):
	"""Serializes/pickle object(prefferably list) to pkl"""
	with open(file_str + '.pkl', 'wb') as f:
		pickle.dump(file_obj, f)

def pickle_deserialize(file_str):
	"""Deserialize/unpickle file to list (maybe ?)"""
	if not is_saved(file_str + '.txt'):
		raise('File does not exist !')
	with open(file_str + '.pkl', 'rb') as f:
		return pickle.load(f)


import sys
import inspect

if __name__ == '__main__':
	functions, modules = [], []
	#modules = []
	for name, obj in inspect.getmembers(sys.modules[__name__]):
		if inspect.isfunction(obj):
			functions.append(name)
			help(obj) # alternate syntax: my_func.__doc__
		elif inspect.ismodule(obj):
			modules.append(name)
	
	print('functions: %s' % functions)
	print('modules: %s' % modules)

"""Summary
Utility package for data science tasks.

>> python utils.py -v # to see verbose output of tests

"""


# Boolean functions

def is_variable(var):
	"""Checks if the variable is saved in either local or global variables.

	# uncomment to test
	>>> is_variable('__doc__')
	True

	"""
	return ( var in locals() or var in globals() )

def is_saved(file_str):
	"""Checks if the file is saved locally.

	>>> is_saved('README.md')
	True

	"""
	from pathlib import Path
	return Path(file_str).is_file()


# Serializing functions - json

import json

def json_serialize(file_str, file_obj):
	"""Serializes object(prefferably dict) to json.

	>>> json_serialize('temp', {'test': 2})
	>>> is_saved('temp.json')
	True
	>>> from os import remove; remove('temp.json') # teardown

	"""
	with open(file_str + '.json', 'w') as f:
		f.write(json.dumps(file_obj))

def json_deserialize(file_str):
	"""Deserialize file to dict.

	>>> json_serialize('temp', {'test': 2}) # set-up
	>>> json_deserialize('temp')
	{'test': 2}

	"""
	if not is_saved(file_str + '.json'):
		raise('File does not exist !')
	with open(file_str + '.json', 'r') as f:
		return json.loads(f.read())


# Serializing functions - pickle

import pickle

def pickle_serialize(file_str, file_obj):
	"""Serializes/pickle object(prefferably list) to pkl.

	>>> pickle_serialize('temp', [1, 2, 3])
	>>> is_saved('temp.pkl')
	True
	>>> from os import remove; remove('temp.pkl') # teardown

	"""
	with open(file_str + '.pkl', 'wb') as f:
		pickle.dump(file_obj, f)

def pickle_deserialize(file_str):
	"""Deserialize/unpickle file to str.

	>>> pickle_serialize('temp', [1, 2, 3]) # set-up
	>>> pickle_deserialize('temp')
	[1, 2, 3]
	>>> from os import remove; remove('temp.pkl') # teardown

	"""
	if not is_saved(file_str + '.pkl'):
		raise('File does not exist !')
	with open(file_str + '.pkl', 'rb') as f:
		return pickle.load(f)

# Serializing functions - yaml

import yaml

def yaml_serialize(file_str, file_obj):
	"""Serialize yaml file.

	>>> yaml_serialize('temp', {'a': 2})
	>>> is_saved('temp.yaml')
	True
	>>> from os import remove; remove('temp.yaml') # teardown

	"""
	with open(file_str + '.yaml', 'w') as f:
		yaml.dump(file_obj, f, default_flow_style=False)

def yaml_deserialize(file_str):
	"""Deserialize yaml file.

	>>> yaml_serialize('temp', {'a': 2}) # set-up
	>>> yaml_deserialize('temp')
	{'a': '2'}
	>>> from os import remove; remove('temp.yaml') # teardown

	"""
	if not is_saved(file_str + '.yaml'):
		raise('File does not exist !')
	with open(file_str + '.yaml', 'r') as stream:
		try:
			# using BaseLoader to prevent value conversion
			loaded = yaml.load(stream, Loader=yaml.BaseLoader)
		except yaml.YAMLError as exc:
			print(exc)
		# print(json.dumps(dict(loaded), sort_keys=True, indent=4, separators=(',', ': ')))
		return loaded


import sys
import inspect

if __name__ == '__main__':
	functions, modules = [], []
	# modules = []
	for name, obj in inspect.getmembers(sys.modules[__name__]):
		if inspect.isfunction(obj):
			functions.append(name)
			# help(obj) # alternate syntax: my_func.__doc__
		elif inspect.ismodule(obj):
			modules.append(name)
		# print('%s = %s' % (name, is_variable(name)))
	
	print('\nfunctions: %s' % functions)
	print('\nmodules: %s\n\n' % modules)

	import doctest
	doctest.testmod()
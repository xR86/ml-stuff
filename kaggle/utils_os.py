import os


def filter_prefix(root='./', prefix='.'):
	root, dirs, files = os.walk(root).__next__()
	# print(root, end='\n---\n')
	# print(dirs, end='\n---\n')
	# print(files, end='\n---\n')
	lst = list(filter(None, map(lambda x: x if x.startswith(prefix) else None, files)))
	return lst


if __name__ == "__main__":
	print('If ran from ml-stuff/')
	print('Should be `.gitignore`: %s' % filter_prefix())

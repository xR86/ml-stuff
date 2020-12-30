import json
import os


def filter_prefix(root='./', prefix='.'):
	root, dirs, files = os.walk(root).__next__()
	# print(root, end='\n---\n')
	# print(dirs, end='\n---\n')
	# print(files, end='\n---\n')
	lst = list(filter(None, map(lambda x: x if x.startswith(prefix) else None, files)))
	return lst

def file_listing(search_path):
	notes = open('./file_list.txt', 'w')
	notes_structured = open('./file_list.json', 'w')

	payload = {}
	for root, dirs, files in os.walk(search_path):
		notes.write(root + '\n')
		notes.write('\n'.join(files))
		notes.write('\n')
		payload[root] = files

	json.dump(payload, notes_structured, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == "__main__":
	print('If ran from ml-stuff/')
	print('Should be `.gitignore`: %s' % filter_prefix())

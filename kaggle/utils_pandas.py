
keep_this = """
Feature 1
Feature 2  
"""


def feature_lst(lst=keep_this):
	return list(map(lambda x: x.strip(), filter(None, lst.split('\n'))))


if __name__ == '__main__':
	print("List should be ['Feature 1', 'Feature 2']: %s" % feature_lst())

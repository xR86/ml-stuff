import pandas as pd

# Ideally, selected features should be enumerated in markdown
# ___________
# |_md_______|
# | feature1 |
# | `id`     |
# | feature2 |
# | `...`    |
# |__________|


keep_this = """
Feature 1
Feature 2  
"""


def feature_lst(lst=keep_this):
	return list(map(lambda x: x.strip(), filter(None, lst.split('\n'))))


def init():
	limit_on_flag = False
	if limit_on_flag:
	    pd.set_option('display.max_rows', 60)
	    pd.set_option('display.max_columns', 20)
	else:
	    pd.set_option('display.max_rows', None)
	    pd.set_option('display.max_columns', None)

	# default = 60
	print('display.max_rows    = %s' % pd.get_option('display.max_rows'))
	# default = 20
	print('display.max_columns = %s' % pd.get_option('display.max_columns'))

	pd.set_option('display.float_format', lambda x: '%.3f' % x)
	print('display.float_format = %s' % pd.get_option('display.float_format'))

def info(df):
	print('Dataset range: %s rows, %s columns\n' % df.shape)
	df.info(verbose=False)

if __name__ == '__main__':
	print("List should be ['Feature 1', 'Feature 2']: %s" % feature_lst())

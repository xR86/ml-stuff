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

def chunker(df_tf, init_i = 0, i = 0, small = False):
	# can be wrapped in tqdm ?
	for chunk in df_tf:
		if init_i != 0:
			print('Step ' + str(i))
			print('> left - ' + str(init_i) + ' skip')
			init_i -= 1
			i += 1
			del chunk
			continue
		print('Step ' + str(i))
		print('> Chunk accessed')
		proc_small_df = chunk[lst]
		print('> Chunk selected')

		#if small:
		#	pd.concat([new_proc_df, proc_small_df], ignore_index=True)

		print('> Saving csv')
		proc_small_df.to_csv('proc.csv.' + str(i))
		del proc_small_df
		del chunk
		print('next')

		i += 1


if __name__ == '__main__':
	print("List should be ['Feature 1', 'Feature 2']: %s" % feature_lst())

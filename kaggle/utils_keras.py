'''Keras utility library

Utilities for common Keras use. Oppinionated file naming.

TODO:
+ use globs to set common naming templates:
  + `m_[model_name]_[graph/weight/plot] - model-specific files (folder structure ?)
  + `results_[plot...]` - general analysis plots
  + `spool_[summaries]` - saved spools (if needed separately from the notebook)

Usual stages:
+ save the model
+ save model summaries
+ save/display model plots

'''

# Assuming multiple models, you would represent them like this:
# 
# models = {
# 	'autoencoder': autoencoder,
# 	'encoder': encoder,
# 	'decoder': decoder
# }

def model_save(model_name, model):
	'''Save model graph and weights.

	# eg: model_save('encoder', encoder)
	'''
	# from keras.models import Model

	# serialize model to JSON
	model_json = model.to_json()
	with open('%s.json' % model_name, 'w') as f:
		f.write(model_json)

	# serialize weights to HDF5
	model.save_weights('%s_weights.h5' % model_name)
	print('Saved %s to disk' % model_name)

def model_save_mult(models_dict):
	'''Save multiple model graphs and weights.

	# eg: model_save_mult({'encoder': encoder})
	'''
	for name, model in models_dict.items():
		model_save(name, model)


def model_summary_spool_mult(models_dict, save_flag=True):
	'''Saves multiple model summaries to spool and returns it.

	# eg: summary_spool_mult({'encoder': encoder}, save_flag=False)
	'''
	# from keras.models import Model
	# import numpy as np

	spool = str()

	for name, model in models_dict.items():
		temp_lst = list()
		model.summary(print_fn = lambda x: temp_lst.append(x))

		spool += '## %s ##\n' % name.title() # or .upper()
		spool += '\n'.join(temp_lst) + '\n'
		spool += '***' * 20 + '\n\n'

	if save_flag:
		np.savetxt('spool_summaries.txt', [spool], fmt='%s')

	return spool


# single plot_model use
# from keras.utils import plot_model
# plot_model(model, to_file="model.png")

def model_plot_save_mult(models_dict):
	'''Saves multiple models plot

	# eg: plot_model_mult({'model_name': model})
	'''
	# graphviz and pydot needed for plot_model
	from keras.utils import plot_model

	# single plot_model use
	# plot_model(model, to_file="model.png")

	for name, model in models_dict.items():
		plot_model(model, to_file='%s_plot.png' % name)


def model_display(model_name, figsize=(5,5)):
	'''Displays model plot (if it has been saved)

	# eg: model_display('encoder')
	'''
	# import matplotlib.pyplot as plt
	# %matplotlib inline
	import matplotlib.image as mpimg
	from pathlib import Path

	model_path = '%s_plot.png' % model_name

	if Path(model_path).is_file():
		# plt.rcParams.update({'figure.figsize': (30,30)})
		plt.figure(figsize=figsize)

		img = mpimg.imread(model_path)

		plt.imshow(img)
		plt.axis('off')
		plt.show()


if __name__ == '__main__':
	pass

# https://tableaufriction.blogspot.ro/2012/11/finally-you-can-use-tableau-data-colors.html
# https://www.tableau.com/about/blog/2016/4/examining-data-viz-rules-dont-use-red-green-together-53463

# more palettes here:
# https://gist.github.com/AndiH/c957b4d769e628f506bd
# https://gist.github.com/chebee7i/4041f848ee2710d500e6

from IPython.display import display, HTML
from PIL import Image

# optional imports, used in select functions
# import glob
# import random

# Create a list of colors (from Tableau, iWantHue or coolors)
color_blind_10 = {
	'cb_blue_1': (0/255, 107/255, 164/255),
	'cb_blue_2': (95/255, 158/255, 209/255),
	'cb_blue_3': (162/255, 200/255, 236/255),
	'cb_orange_1': (200/255, 82/255, 0/255),
	'cb_orange_2': (255/255, 128/255, 14/255),
	'cb_orange_3': (255/255, 188/255, 121/255),
	'cb_grey_1': (89/255, 89/255, 89/255),
	'cb_grey_2': (137/255, 137/255, 137/255),
	'cb_grey_3': (171/255, 171/255, 171/255),
	'cb_grey_4': (207/255, 207/255, 207/255)
}

def jp_display_color_palette(colors=color_blind_10):
	col_html = ''
	for item in sorted(colors):
		#print(item)
		#print(colors[item])
		col_html += '<div style="background-color: rgb(' + \
					str(int(colors[item][0]*255)) + ', ' +\
					str(int(colors[item][1]*255)) + ', ' +\
					str(int(colors[item][2]*255)) +\
					'); display: inline-block; padding: 2rem; margin: 0.1rem; border-radius: 5%">' + item + '</div>'
	display(HTML(col_html))
	#return True

# TODO: should include base64 encode
def jp_display_img(path, height):
	"""Display image as HTML with defined height.

	# >>> img_display('path/to/img.png', 20)
	"""
	import random

	# add random number to path string in order to prevent browser caching
	# in the event of future updates to the image
	cnt = random.randint(0, 2e8)
	path += '?' + str(cnt)

	if height:
		display(HTML('<img src="%s" alt="Display image" style="height: %srem">' % (path, height)))
	else:
		display(HTML('<img src="%s" alt="Display image">' % path))

def jp_display_img_mult(path_lst, height):
	"""Display multiple images as HTML based on regex/exact match on path and defined height

	# >>> jp_display_img_mult('path/to/imgs_*.jpg', 10)
	"""
	import glob
	import random

	path_lst = glob.glob(path_lst)

	html = ''
	for path in path_lst:
		cnt = random.randint(0, 2e8)
		path += '?' + str(cnt)
		html += '<img src="%s" \
			alt="Display image" style="\
				height: %srem; display:inline-block; padding:1px;margin-top:0;"\
			>' % (path, height)

	display(HTML(html))

def compare_graphs(img1, img2, alpha = 0.3):
	# img1 = 'fig_sales_price.png'
	background = Image.open(img1)
	foreground = Image.open(img2)

	out = Image.blend(background, foreground, alpha)
	out.show()
	#background.paste(foreground, (0, 0), foreground)
	#background.show()


if __name__ == '__main__':
	print('Please use functions from Jupyter context')

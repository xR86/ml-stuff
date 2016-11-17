"""
https://pythonhosted.org/python-weka-wrapper/
http://weka.sourceforge.net/doc.stable/weka/classifiers/trees/Id3.html
"""

# [[left tree], ["A":{ "+": 2, "-": 1}], [right tree]]
class ID3Tree(object):
	def __init__(self):
		self.tree = []

	def add(self, element, ): #**kwargs
		self.tree.insert(len(self.tree)/2, element)

	def add_left(self, element):
		self.tree.insert(len(self.tree)/3, [element])

	def walk(self, node):
	    """ iterate tree in pre-order depth-first search order """
	    yield node
	    for child in node.children:
	        for n in walk(child):
	            yield n
	def dump(self):
		print self.tree


input = open('ID3-data.txt', 'r').read()

tree = ID3Tree()
tree.add(2)
tree.dump()

tree.add_left(3)
tree.dump()

tree.add_left(3)
tree.dump()

import cPickle, gzip, numpy


class Perceptron(object):
    def __init__(self, name):
        self.name = name

    def description(self):
        print "This is a perceptron object"
        pass

    def activation(self, input):
        """
            Function used for activation of the neuron
        :param input:
        :return:
        """
        if (input > 0): return 1
        return 0


'''

while not allClassified and nrIterations > 0:
    allClassified = True
    for x,t in trainingSet:
        z = w*x + b                         #compute net input
        output = activation(z)              #classify the sample
        w = w + (t-output) * x * lambda     #adjust the weights
        b = b + (t-output) * lambda         #adjust the bias
        if not output = t:
            allClassified = False
        nrIterations -= 1

'''

f = gzip.open('mnist.pkl.gz', 'rb')
# u = pickle._Unpickler(f)
# train_set, valid_set, test_set = u.load()
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()

print train_set

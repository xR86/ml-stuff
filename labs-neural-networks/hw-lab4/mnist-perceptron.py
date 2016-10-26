import cPickle, gzip, numpy as np

epochs = 1
learning_rate = 0.1

class Perceptron(object):

    error = 1
    #errorRate = error * 100 # ?????


    def __init__(self, digit, weight, bias):
        self.digit = digit
        self.weight = weight
        self.bias = bias

    def description(self):
        print "This is a perceptron object"

    def activation(self, input):
        # Function used for activation of the neuron
        if (input > 0): return 1
        return 0

    def expected(self, value):
        if self.digit == value:
            return 1
        return 0


    def train(self):
        global epochs
        allClassified = False

        timeCounter = 0
        while not allClassified and epochs > 0:
            allClassified = True
            # for x, t in train_set:
            x = train_set[0]
            t = train_set[1]
            for i in range(len(train_set[0])):
                # compute net input
                z = np.sum(np.dot(self.weight[i], x[i]), self.bias[self.digit])
                # classify the sample
                output = self.activation(z)
                # adjust the weights
                self.weight[self.digit] = np.sum(self.weight[i], (self.expected(t[i]) - output) * x[i] * learning_rate)  #* a[i] * learning_rate, for j in x[i])# adjust the weights
                # adjust the bias
                self.bias[self.digit] = self.bias[self.digit] + (t[i]-output) * learning_rate
                if output != t[i]:
                    allClassified = False

                self.error = self.expected(t[i]) - output
                if self.digit == 0:
                    str = "%d,%d" % (timeCounter, self.error)
                    print str
                    #f2.write(str + "\n")
                timeCounter += 10
        epochs = epochs - 1
        #f2.close


#py 3
# u = pickle._Unpickler(f)
# train_set, valid_set, test_set = u.load()

f = gzip.open('mnist.pkl.gz', 'rb')
#f2 = open('matplot-text.txt', 'w+')

train_set, valid_set, test_set = cPickle.load(f)
f.close()

print 'train_set length: ', len(train_set[0])
perceptron_layer = []

for i in range(10):
    perceptron_layer.append( Perceptron(i, np.random.rand(1, len(train_set[0])), np.zeros(10)) )

for i in perceptron_layer:
    print i, i.digit #, i.weight, i.bias

for i in perceptron_layer:
    print 'start to train: ', i.digit
    i.train()


import cPickle, gzip, numpy as np


# semi-functional


#py 3
# u = pickle._Unpickler(f)
# train_set, valid_set, test_set = u.load()
f = gzip.open('mnist.pkl.gz', 'rb')
#f2 = open('matplot-text.txt', 'w+')

train_set, valid_set, test_set = cPickle.load(f)
f.close()

print 'train_set length: ', len(train_set[0])
# perceptron_layer = []

epochs = 1
learning_rate = 0.1

class Perceptron_Net(object):
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias
        self.layer = []

    def init_layer(self):
        print "Initializing layer ",
        for j in range(10):
            # print [numpy.random.uniform(0, 1, size=784) for i in range(10)]
            # print len(train_set[0])
            # shapes (50000,) and (784,) not aligned: 50000 (dim 0) != 784 (dim 0) => np.random.rand(1, len(train_set[0]))
            self.layer.append(Perceptron(j))

        # check for initialization
        for i in self.layer:
            print i, i.digit  # , i.weight, i.bias

    def train_network(self):
        # for i in self.layers_no:
        for perceptron in self.layer:
            print '#### NN trains: ', perceptron.digit
            perceptron.train()

    def test(self):
        self.train_network()
        ok = 0
        for i in range(len(test_set[0])):
            maximum = -1
            cifmax = -1
            for digit in range(10):
                z = np.dot(test_set[0][i], self.weight[digit]) + self.weight[digit]
                if z > maximum:
                    maximum = z
                    cifmax = digit
            if cifmax == test_set[1][i]:
                ok += 1
        print(ok)
        print(ok * 1.0 / len(test_set[0]) * 100)

class Perceptron(object):
    error = 1
    #errorRate = error * 100 # ?????

    def __init__(self, digit):
        self.digit = digit

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
        '''
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
        '''

        print("Start of training for digit " + str(self.digit))
        for i in range(len(train_set[0])):
            z = np.dot(train_set[0][i], perceptron_net.weight[self.digit]) + perceptron_net.bias[self.digit]
            output = self.activation(z)
            x = np.array(train_set[0][i]).dot((self.expected(train_set[1][i]) - output) * learning_rate)
            perceptron_net.weight[self.digit] = np.add(perceptron_net.weight[self.digit], x)
            perceptron_net.bias[self.digit] += (self.expected(train_set[1][i]) - output) * learning_rate
        print("End of training for digit " + str(self.digit))




perceptron_net = Perceptron_Net([np.random.uniform(0, 1, size=784) for i in range(10)], np.zeros(10))

perceptron_net.init_layer()
perceptron_net.train_network()
perceptron_net.test()





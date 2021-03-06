import cPickle, gzip, numpy as np

#py 3
# u = pickle._Unpickler(f)
# train_set, valid_set, test_set = u.load()
f = gzip.open('mnist.pkl.gz', 'rb')
f2 = open('matplot-text.txt', 'w+')

train_set, valid_set, test_set = cPickle.load(f)
f.close()

print 'train_set length: ', len(train_set[0])
perceptron_layer = []

epochs = 1
learning_rate = 0.1

class Perceptron_Net(object):
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias
        self.layer = []
        self.ok_rate = 0
        self.error_rate = 0

    def init_layer(self):
        for i in range(10):
            # print [numpy.random.uniform(0, 1, size=784) for i in range(10)]
            # print len(train_set[0])
            # shapes (50000,) and (784,) not aligned: 50000 (dim 0) != 784 (dim 0) => np.random.rand(1, len(train_set[0]))
            self.layer.append(Perceptron(i))

        # check for initialization
        for perceptron in self.layer:
            print perceptron, perceptron.digit  # , i.weight, i.bias

    def train_network(self):
        for perceptron in self.layer:
            print 'queued train: ', perceptron.digit
            perceptron.train()

    def test(self):
        self.train_network()
        ok = 0
        clock_counter = 0
        for i in range(len(test_set[0])):
            maximum = -1
            digitmax = -1
            for digit in range(10):
                z = np.dot(test_set[0][i], self.weight[digit]) + self.bias[digit]
                if z > maximum:
                    maximum = z
                    digitmax = digit
            if digitmax == test_set[1][i]:
                ok += 1
            self.ok_rate = ok * 1.0 / len(test_set[0]) * 100
            self.error_rate = 100 - self.ok_rate

            str = "%d, %f" % (clock_counter, self.error_rate)
            print "clock, error: ", str
            print clock_counter, self.error_rate
            f2.write(str + "\n")
            clock_counter += 10

        #self.ok_rate = ok * 1.0 / len(test_set[0]) * 100
        #self.error_rate = 100 - self.ok_rate
        self.error_rate = 100 - (ok * 1.0 / len(test_set[0]) * 100)
        self.ok_rate = ok * 1.0 / len(test_set[0]) * 100
        print "Final result: ", self.ok_rate, "%"
        print "Error rate: ", self.error_rate, "%"

        f2.close

class Perceptron(object):

    #error = 1
    #errorRate = 100 - perceptron_net.ok_rate

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

        print("###Train digit: " + str(self.digit))
        for i in range(len(train_set[0])):
            z = np.dot(train_set[0][i], perceptron_net.weight[self.digit]) + perceptron_net.bias[self.digit]
            output = self.activation(z)
            x = np.array(train_set[0][i]).dot((self.expected(train_set[1][i]) - output) * learning_rate)
            perceptron_net.weight[self.digit] = np.add(perceptron_net.weight[self.digit], x)
            perceptron_net.bias[self.digit] += (self.expected(train_set[1][i]) - output) * learning_rate
        print("---Digit trained: " + str(self.digit))




perceptron_net = Perceptron_Net([np.random.uniform(0, 1, size=784) for i in range(10)], np.zeros(10))

perceptron_net.init_layer()
perceptron_net.train_network()
perceptron_net.test()


import cPickle, gzip, numpy as np

f = gzip.open('mnist.pkl.gz', 'rb')
f2 = open('matplot-text.txt', 'w+')

train_set, valid_set, test_set = cPickle.load(f)
f.close()

print 'train_set length: ', len(train_set[0])

epochs = 1
learning_rate = 0.1

class MLP(object):
    def __init__(self):
        # Layer init =>
        # tag, no_elements, activation, weight, bias, train_set, valid_set, test_set

        # 100 neurons, sigmoid activation
        hidden_node_no = 100
        self.hidden_layer = PerceptronLayer(
            "hidden",
            hidden_node_no,
            "sigmoid",
            [np.random.uniform(0, 1, size=784) for i in range(hidden_node_no)],
            np.zeros(hidden_node_no),
            train_set,
            valid_set,
            test_set
        )  # 784 -> 100 ?

        # 10 neurons, softmax activation
        perceptron_node_no = 10
        self.perceptron_layer = PerceptronLayer(
            "output",
            perceptron_node_no,
            "softmax",
            [np.random.uniform(0, 1, size=784) for i in range(perceptron_node_no)],
            np.zeros(perceptron_node_no),
            self.hidden_layer.train_set,
            valid_set,
            test_set
        )

        self.hidden_layer.init_layer()
        self.perceptron_layer.init_layer()

    def train(self):
        self.hidden_layer.train_network()
        # self.hidden_layer.test()
        self.perceptron_layer.train_network()

    def test(self):
        self.perceptron_layer.test()


#class Layer(object):
#    pass

class PerceptronLayer(object):
    def __init__(self, tag, no_elements, activation, weight, bias, train_set, valid_set, test_set):
        self.tag = tag
        self.no_elements = no_elements
        self.activation = activation
        self.weight = weight
        self.bias = bias
        self.train_set = train_set
        self.valid_set = valid_set
        self.test_set = test_set

        self.layer = []
        self.ok_rate = 0
        self.error_rate = 0

    def init_layer(self):
        for i in range(self.no_elements):
            # print [numpy.random.uniform(0, 1, size=784) for i in range(10)]
            # print len(self.train_set[0])
            # shapes (50000,) and (784,) not aligned: 50000 (dim 0) != 784 (dim 0) => np.random.rand(1, len(self.train_set[0]))
            self.layer.append(Perceptron(i, self)) #HACK: 1 - should only expose: layer_name, train_set, activation, weight, bias

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
        for i in range(len(self.test_set[0])):
            maximum = -1
            digitmax = -1
            for digit in range(10):
                z = np.dot(self.test_set[0][i], self.weight[digit]) + self.bias[digit]
                if z > maximum:
                    maximum = z
                    digitmax = digit
            if digitmax == self.test_set[1][i]:
                ok += 1
            self.ok_rate = ok * 1.0 / len(self.test_set[0]) * 100
            self.error_rate = 100 - self.ok_rate

            str = "%d, %f" % (clock_counter, self.error_rate)
            print "clock, error: ", str
            print clock_counter, self.error_rate
            f2.write(str + "\n")
            clock_counter += 10

        #self.ok_rate = ok * 1.0 / len(self.test_set[0]) * 100
        #self.error_rate = 100 - self.ok_rate
        self.error_rate = 100 - (ok * 1.0 / len(self.test_set[0]) * 100)
        self.ok_rate = ok * 1.0 / len(self.test_set[0]) * 100
        print "Final result: ", self.ok_rate, "%"
        print "Error rate: ", self.error_rate, "%"

        f2.close

class Perceptron(object):

    #error = 1
    #errorRate = 100 - perceptron_layer.ok_rate

    def __init__(self, digit, parent):
        self.digit = digit
        # HACK-1: - should only expose: layer_name, train_set, activation, weight, bias
        self.parent = parent #should work (pass-by-assignment)

    def description(self):
        print "This is a perceptron object"

    # Functions used for activation of the neuron
    def activation_step(self, input):
        # Step activation function
        if input > 0: return 1
        return 0

    def activation_sigmoid(self, input):
        # Sigmoid activation function.
        f =  1.0 / (1.0 + np.exp(-input))
        if f > 0.5: return f
        return 0

    def activation_sigmoid_deriv(self, input):
        # Derivative of the sigmoid activation function.
        f = self.activation_sigmoid(input) * (1 - self.activation_sigmoid(input))
        if f > 0.5: return f
        return 0

    def activation_softmax(self, input):
        #Compute softmax values for each sets of scores in x.
        f = np.exp(input) / np.sum(np.exp(input), axis=0)
        if f > 0.5: return f
        return 0

    def expected(self, value):
        if self.digit == value:
            return 1
        return 0


    def train(self):
        print(self.parent.tag + "###Train neuron: " + str(self.digit))
        for i in range(len(self.parent.train_set[0])):
            z = np.dot(self.parent.train_set[0][i], self.parent.weight[self.digit]) + self.parent.bias[self.digit]
            output = getattr(self, 'activation_' + self.parent.activation)(z) #self.activation_step(z)
            x = np.array(self.parent.train_set[0][i]).dot((self.expected(self.parent.train_set[1][i]) - output) * learning_rate)
            self.parent.weight[self.digit] = np.add(self.parent.weight[self.digit], x)
            self.parent.bias[self.digit] += (self.expected(self.parent.train_set[1][i]) - output) * learning_rate

            # change self.parent.train_set such that it will be propagated forward
            self.parent.train_set[0][i] = z
        print("---Digit trained: " + str(self.digit))


"""
############# Main code #############
"""

mlp = MLP()
mlp.train()
mlp.test()

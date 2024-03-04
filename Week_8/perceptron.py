import numpy as np

class Perceptron:
    def __init__(self, num_inputs, learning_rate=0.01):
        #Constructor method to initialize the perceptron
        #Randomly initialize weights and bias
        self.weights = np.random.rand(num_inputs) #initialze weights
        self.bias = np.random.rand(1) #initialize bias
        self.learning_rate = learning_rate = learning_rate
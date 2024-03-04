import numpy as np

class Perceptron:
    def __init__(self, num_inputs, learning_rate=0.01):
        #Constructor method to initialize the perceptron
        #Randomly initialize weights and bias
        self.weights = np.random.rand(num_inputs) #initialze weights
        self.bias = np.random.rand(1) #initialize bias
        self.learning_rate = learning_rate = learning_rate # Learning rate for training


    def step_function(self, x):
        #Step function to convert any vlaue to 0 or 1
        return np.where(x >= 0, 1, 0)
    
    
    def predict(self, inputs):
        #Method to make predictions using the perceptron
        #compute the weighted sum of inputs and add bias
        summation = np.dot(input, self.weights) + self.bias
        #Apply step function to determin e output (0 or 1)
        return self.step_function(summation)
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
    
    def train(self, training_inputs, labels, epochs):
        # Training method to adjust weights based on error
        for epoch in range(epochs):
            # Iterate over each training eample
            for inputs, label in zip(training_inputs, labels):
                # Make prediction  using curent weights
                prediction = self.predict(inputs)
                #Update weights based on prediction eror
                self.weights = self.weights + self.learning_rate * (label - prediction) * inputs
                self.bias += self.learning_rate * (label - prediction)


                
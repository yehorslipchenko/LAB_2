import numpy as np
import random


class Relu:
    @staticmethod
    def Func(data):
        return np.maximum(0, data)

    @staticmethod
    def dFunc(data):
        return np.array([1 if i >= 0 else 0 for i in data])


class Sigmoid:
    @staticmethod
    def Func(data):
        return 1.0 / (1.0 + np.exp(-data))

    @staticmethod
    def dFunc(data):
        return data * (1.0 - data)


class Network:
    def __init__(self, InputData, OutputData, learning_rate):
        self.Input_layer = [0] * 3
        self.Hidden_layer = [0] * 3
        self.Output_layer = [0] * 2
        self.learning_rate = learning_rate
        self.Weights = [0] * 5
        self.n_weights = 3
        self.InputDataSet = InputData
        self.OutputDataSet = OutputData
        self.Gradient = [0] * 5
        self.train_error = None
        self.validation_error = None

    def Initialize(self):
        for i in range(len(self.Input_layer)):
            self.Input_layer[i] = self.InputDataSet[0][i]
        for i in range(len(self.Weights)):
            self.Weights[i] = [0] * self.n_weights
        for i in range(len(self.Weights)):
            for j in range(self.n_weights):
                self.Weights[i][j] = random.uniform(-0.5, 0.5)
        self.Forward_Propagate()

    def Error_Function(self, index):
        return (self.Output_layer[0] - self.OutputDataSet[index][0]) ** 2 + (
                self.Output_layer[1] - self.OutputDataSet[index][1]) ** 2

    def Activation(self, layer, i):
        temp = 0
        for l, w in zip(layer, self.Weights[i]):
            temp += l * w
        temp = Sigmoid.Func(temp)
        return temp

    def Forward_Propagate(self):
        OL_index = 0
        for i in range(len(self.Weights)):
            if i <= 2:
                self.Hidden_layer[i] = self.Activation(self.Input_layer, i)
            else:
                self.Output_layer[OL_index] = self.Activation(self.Hidden_layer, i)
                OL_index = OL_index + 1

    def Backward_Propagate(self, expected):
        for i in range(len(self.Output_layer)):
            self.Gradient[i] = expected[i] - self.Output_layer[i] * Sigmoid.dFunc(self.Output_layer[i])
            self.Weights.reverse()
            for j in range(self.n_weights):
                self.Weights[i][j] += self.learning_rate * self.Gradient[i] * self.Hidden_layer[j]
            self.Weights.reverse()

        for i in range(len(self.Hidden_layer)):
            self.Gradient[i + 2] = self.Weights[4][i] * self.Gradient[0] + self.Weights[3][i] * self.Gradient[
                1] * Sigmoid.dFunc(self.Hidden_layer[i])
            self.Weights.reverse()
            for j in range(self.n_weights):
                self.Weights[i + 2][j] += self.learning_rate * self.Gradient[i + 2] * self.Input_layer[j]
            self.Weights.reverse()

    def Train(self, ID, OD):
        print("Train:")
        self.InputDataSet = ID
        self.OutputDataSet = OD
        self.Initialize()
        self.train_error = 0
        for i in range(len(self.InputDataSet)):
            self.Forward_Propagate()
            expected = self.OutputDataSet[i]
            self.Backward_Propagate(expected)
            self.train_error += sum([(self.Output_layer[i]-expected[i])**2 for i in range(len(self.Output_layer))])
            self.train_error /= len(self.InputDataSet)
        print(f"Train error->{self.train_error}")


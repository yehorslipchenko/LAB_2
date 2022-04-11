import math
import random

x1 = 5
x2 = 4
x3 = 3


def func(X):
    return math.sin(X[0]) + math.sin(X[1]) - math.sin(X[2])


def normalize(X, Y):
    for i, xs in enumerate(X):
        nx1 = [xs[0] for xs in X]
        nx2 = [xs[1] for xs in X]
        nx3 = [xs[2] for xs in X]
        maxX = [max(nx1), max(nx2), max(nx3)]
        minX = [min(nx1), min(nx2), min(nx3)]
        for j, x in enumerate(xs):
            X[i][j] = (x - minX[j]) / (maxX[j] - minX[j])

    minY = min([ys[0] for ys in Y])
    maxY = max([ys[0] for ys in Y])

    minY1 = min([ys[1] for ys in Y])
    maxY1 = max([ys[1] for ys in Y])
    for i, ys in enumerate(Y):
        Y[i][0] = (ys[0] - minY) / (maxY - minY)
        Y[i][1] = (ys[1] - minY1) / (maxY1 - minY1)


def generateData(X, Y):
    for i in range(20):
        X[i] = [0] * 3
        Y[i] = [0] * 2

    for i in range(len(X)):
        for j in range(len(X[i])):
            if i == 0 and j == 0:
                X[i][j] = x1
                continue
            if i == 0 and j == 1:
                X[i][j] = x2
                continue
            if i == 0 and j == 2:
                X[i][j] = x3
                continue
            else:
                r = random.random()
                if r > 0.5:
                    X[i][j] = X[i - 1][j] + 1
                else:
                    X[i][j] = X[i - 1][j] - 1

    sum = 0
    for i in range(len(Y)):
        res = func(X[i])
        Y[i][0] = res
        sum += res

    avg = sum / 20

    for i in range(len(Y)):
        for j in range(len(Y[i])):
            if j == 1:
                if func(X[i]) > avg:
                    Y[i][j] = 1

    normalize(X, Y)
    return X, Y


def ShowData(X, Y):
    for i in range(len(X)):
        print(f"{X[i]}===============>{Y[i]}")

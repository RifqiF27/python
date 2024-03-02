# Given a logarithm base X and two values A and B, return a sum of logratihms with the base X: logXA+logX B
import math


def logs(x, a, b):
    return math.log(a, x) + math.log(b, x)


print(logs(10, 2, 3))
print(logs(5, 2, 3))
print(logs(1000, 2, 3))
print(logs(2, 1, 2))
print(logs(0.00001, 0.002, 0.01))
print(logs(0.1, 0.002, 0.01))

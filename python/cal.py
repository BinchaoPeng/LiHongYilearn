import math
import numpy as np

X = np.array([0.026, 0.036, 0.031, 0.033,
              0.016, 0.026, 0.014, 0.031,
              0.025, 0.025, 0.026, 0.036,
              0.017, 0.025, 0.016, 0.026
              ])

mean = X.sum() / 16
print(mean)

Sum = 0
for x in X:
    Sum += math.pow(x - mean, 2)

SD = math.pow(Sum / 15, 0.5)

print(SD)

for i, x in enumerate(X, 0):
    X[i] = (x - mean) / SD

print(X)

X = np.array([0.063, 1.502, 0.783, 1.071,
              -1.376, 0.063, -1.664, 0.783,
              -0.081, -0.081, 0.063, 1.502,
              -1.233, -0.081, -1.376, 0.063])

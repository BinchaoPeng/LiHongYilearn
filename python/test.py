import numpy as np

a = np.ones(3)
b = a.sum()
print(b)

a = "abcd"
print(a[1])

h = np.ones((4,1))
h1 = h.transpose()
print(h.shape)
print(h1.shape)
print(h)
print(h1)
import numpy as np

ATGC = [
    "AA", "AC", "AG", "AT",
    "CA", "CC", "CG", "CT",
    "GA", "GC", "GG", "GT",
    "TA", "TC", "TG", "TT",
]

X = np.array([1.289,
              -0.241,
              2.513,
              -0.623,
              -0.822,
              -0.287,
              -0.241,
              -0.394,
              0.646,
              -0.822,
              1.289,
              -1.511,
              -0.394,
              -0.623,
              0.111,

              ])

str = ""
for name, value in zip(ATGC, X):
    str += f"'{name}':{value},"

print(str)

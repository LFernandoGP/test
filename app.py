print("Docker")

lista = list(range(100))
output = []

for x in lista:
    if x%2==0:
        output.append(x)

print("Valor {}".format(output))

output.sort()

import numpy as np
import opencv as cv

cv.open("install.txt")

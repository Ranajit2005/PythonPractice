import matplotlib
import matplotlib.pyplot as plt

import numpy as nu

a = int(input("Give the renge of -x : "))
b = int(input("Give the renge of x : "))
xpoint = range(a,b)
ypoint = [x**2 for x in xpoint]

xcord = nu.array([1,100])
ycord = nu.array([0,100])

plt.plot(xcord,ycord)

plt.plot(xpoint,ypoint)
# plt.plot(xcord,ycord)

plt.show()
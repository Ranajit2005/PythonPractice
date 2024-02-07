# import matplotlib
import matplotlib.pyplot as plt

import numpy as np

# a = int(input("Give the renge of -x : "))
b = int(input("Give the renge of x : "))
xpoint = range(0,b)
ypoint = [x**2 for x in xpoint]

xcord = np.array([0,b])
ycord = np.array([0,b])
plt.grid()
plt.xlabel("dfghj")
plt.ylabel("dfgvbnm")
plt.plot(xcord,ycord)

plt.plot(xpoint,ypoint)
# plt.plot(xcord,ycord)

plt.show()
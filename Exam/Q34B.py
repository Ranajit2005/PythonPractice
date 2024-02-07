import numpy as np
import matplotlib.pyplot as plt
# import random

points = np.random.rand(30,3)
print(points)

plt.scatter(points[:,0],points[:,1])

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()
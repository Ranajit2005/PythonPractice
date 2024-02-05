import numpy as np
import matplotlib.pyplot as plt

Bill = [12,34,56,34,45,24,35,45,24,24,34,56]
month = np.array(['jan','feb','march','april','may','june','july','aug','sep','oct','nov','dec'])
X = np.arange(12)

plt.bar(X,Bill,0.2,label="month")
plt.xticks(X,month)
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

X = ["Sub1","Sub2","Sub3","Sub4","Sub5"]

Student2 = [90,80,70,60,50]
Student1 = [10,20,30,40,50]

Xln = np.arange(len(X))

plt.bar(Xln-0.1,Student1,0.2,label="Studend1")
plt.bar(Xln+0.1,Student2,0.2,label="Student2")

plt.xticks(Xln,X)
plt.legend()
plt.show()
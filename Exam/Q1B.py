import numpy as np
import matplotlib.pyplot as plt 
X = ['Subject A','Subject B','Subject C','Subject D','Subject E'] 
#Student1 = list(map(int, input('Enter the numbers of student 1: ').split())) #Student2 = list(map(int, input('Enter the numbers of student 2: ').split())) 
Student1=[80, 60, 90, 55, 70] 
Student2=[50, 80, 30, 85, 70] 
X_axis = np.arange(len(X)) 
plt.bar(X_axis - 0.1, Student1, 0.2, label = 'Student 1') 
plt.bar(X_axis + 0.1, Student2, 0.2, label = 'Student 2') 
plt.xlim(-0.5,4.5)
plt.ylim(0,150) 
plt.xticks(X_axis, X) 
plt.xlabel("Subjects:") 
plt.ylabel("Marks in subject:") 
plt.title("Marks obtained by two students") 
plt.legend() 
plt.show()

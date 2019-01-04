# proprietary to BEERA // DO NOT COPY
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

def return_random_array():
	a = []
	for i in range(5): a.append(random.randint(1,10))
	return a

x_axis = np.array(return_random_array())
y_axis = np.array(return_random_array())


plt.xlabel("No. of students")
plt.ylabel("CGPA")
plt.title("Students CGPA analysis")
plt.scatter(x_axis, y_axis, s = 50, c = 'red', label = 'stu_cgpa')
x_axis = (3,5,3,1,4)
y_axis = (7,6,2,7,9)
plt.scatter(x_axis, y_axis, s = 50, c = 'green', label = 'something else')
plt.legend()
plt.show()
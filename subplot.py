# proprietary to BEERA // DO NOT COPY
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
global count
count = 0

x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

x_1 = np.random.choice(x1, 500)
x_2 = np.random.choice(x2, 500)
x_3 = np.random.choice(x3, 500)
x_4 = np.random.choice(x4, 500)


def update(curr):
	global count
	count += 1
	print('curre=',curr)
	print('count=',count)
	if curr == 500: a.event_source.stop()
	ax1.hist(x_1[curr:], bins = np.arange(-6,1,0.5), color = 'blue')
	#ax1.annotate('n={}'.format(curr),[-5,1])
	ax2.hist(x_2[curr:], bins = np.arange(0,12,0.5), color = 'red')
	#ax2.annotate('n={}'.format(curr),[1,1])
	ax3.hist(x_3[curr:], bins = np.arange(6,18,0.5), color = 'green')
	ax3.annotate('n={}'.format(curr),[1,1])
	ax4.hist(x_4[curr:], bins = np.arange(14,20,0.5), color = 'yellow')
	#ax4.annotate('n={}'.format(curr),[1,1])





fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
a = animation.FuncAnimation(fig, update, interval = 0)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2 * np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])


y_all = (np.sin(x))+(np.cos(x))+(1/2 * np.sin(2*x))+(1/2 * np.cos(2*x))+(1/3 * np.sin(3*x))+(1/3 * np.cos(3*x))
plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)


plt.plot(x,y_all,label='sin(x) + cos(x) + 1/2sin(2x) + 1/2cos(2x) + 1/3sin(3x) + 1/3cos(3x)')
plt.legend(loc='lower left')

plt.grid()

plt.show()
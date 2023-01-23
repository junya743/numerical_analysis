import numpy as np
import matplotlib.pyplot as plt

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2 * np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])


y_noko = ((1/2) * np.pi)-(np.sin(2*x))-((1/2) * np.sin(4*x))-((1/3) * np.sin(6*x))-((1/4)*np.sin(8*x))
plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)


plt.plot(x,y_noko,label='π/2 - sin(2t) - 1/2sin4t - 1/3sin6t - 1/4sin8t')
plt.legend(loc='lower left')

plt.grid()

plt.show()
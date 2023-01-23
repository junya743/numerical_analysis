import numpy as np
import matplotlib.pyplot as plt

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2 * np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])

y_sinx = -np.sin(x)
y_cos2x = np.cos(2*x)

y_sin3x = 1/2 * np.sin(3*x)
y_all = (-np.sin(x))+(np.cos(2*x))+(1/2 * np.sin(3*x))
plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)

plt.plot(x,y_sinx,label='-sin(x)')
plt.plot(x,y_cos2x,label='cos(2x)')
plt.plot(x,y_sin3x,label='1/2sin(3t)') # label=r'$¥frac{1}{2}$ sin(3t)'
plt.plot(x,y_all,label='-sin(x) + cos(2x) + 1/2sin(3x)')
plt.legend(loc='lower left')

plt.grid()

plt.show()
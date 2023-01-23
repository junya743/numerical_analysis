import numpy as np
import matplotlib.pyplot as plt

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2 * np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])

y_5sinx = 5 * np.sin(x)
y_2sin3x = 2 * np.sin(3*x)

y_3sin7x = 3 * np.sin(7*x)
y_all = (5 * np.sin(x))+(2 * np.sin(3 * x))+(3 * np.sin(7 * x))
plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)

plt.plot(x,y_5sinx,label='5sin(x)')
plt.plot(x,y_2sin3x,label='2sin(3x)')
plt.plot(x,y_3sin7x,label='3sin(7x)')
plt.plot(x,y_all,label='5sin(x)+2sin(3x)+3sin(7x)')
plt.legend(loc='lower left')

plt.grid()

plt.show()
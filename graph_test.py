import numpy as np
import matplotlib.pyplot as plt

# 範囲s
xmin = 2
xmax = 3
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2 * np.pi,-np.pi,0,1,np.pi,2*np.pi],['-2π','-π','0','1','π','2π'])

# kadai5_1
y1 = 1/np.pi*(1 - np.cos(np.pi*x))
y2 = 1/np.pi*(np.cos(np.pi*(x-1))- np.cos(np.pi * x))
y3 = 1/np.pi*(np.cos(np.pi*(x-1))-1)

plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)

plt.plot(x,y3,label='y')

plt.legend(loc='lower left')

plt.grid()

plt.show()
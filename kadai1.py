import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(2, 3, 1)
ax2 = fig.add_subplot(2, 3, 2)
ax3 = fig.add_subplot(2, 3, 3)
ax4 = fig.add_subplot(2, 3, 4)
ax5 = fig.add_subplot(2, 3, 5)

t = np.arange(-np.pi, np.pi,0.01)
#x = np.cos(2*np.pi*t)
ax1.plot(t,np.sin(np.pi*t),color='r', ls='-', label='sin(πt)')
ax2.plot(t,np.cos(2*t + np.pi/4),color='blue', ls='-', label='cos(2t+π/2)')
ax3.plot(t,1 - np.sin(t),color='black', ls='-', label='1-sin(t)')
ax4.plot(t,np.cos(np.pi*t),color='green', ls='-', label='cos(πt)')
ax5.plot(t,np.sin(2*t+np.pi/2),color='yellow', ls='-', label='sin(2t+π/2)')
plt.show()


import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def update(a):
    plt.cla()
    xmin = -10
    xmax = 10
    x = np.arange(xmin,xmax,0.1)
    y = (2 + a/1000) ** x
    #dy = np.gradient(y)
    dy = ((2 + a/1000)**x)*np.log(2 + a/1000)

    plt.plot(y,color='red')
    plt.plot(dy,color='blue')
    # print(type(y))
    # if np.all(y == dy):
    #     print(a/1000 + 2)
    #     o_base = a/1000+2
    plt.title("base = {0},optimal base = {1}".format(a/1000+2,2.718))
    plt.ylim(0,10)

def main():
    fig = plt.figure()
    plt.xlabel('frequency',rotation=0)
    plt.ylabel('amplitude',rotation=90)

    ani = animation.FuncAnimation(fig, update, interval=100, frames = 2000)
    # ani1 = animation.ArtistAnimation(fig,red_ims, interval=100)
    # ani2 = animation.ArtistAnimation(fig,blue_ims, interval=100)
    plt.show()
    
if __name__ == '__main__':
    main()


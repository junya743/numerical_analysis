import numpy as np
import matplotlib.pyplot as plt


def main():
    xmin = 0
    xmax = 10
    x = np.arange(xmin,xmax,0.01)

    plt.xticks([0,2,4,6,8,10],['0','2','4','6','8','10'])

    y1 = x ** 1
    y2 = x ** 2
    y3 = x ** 3

    plt.xlabel('frequency',rotation=0)
    plt.ylabel('amplitude',rotation=90)


    plt.plot(x,y1,label='f(x) = x')
    plt.plot(x,y2,label='f(x) = x^2')
    plt.plot(x,y3,label='f(x) = x^3')

    plt.legend(loc='lower left')

    plt.grid()

    plt.show()

if __name__ == '__main__':
    main()


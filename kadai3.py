import numpy as np
import matplotlib.pyplot as plt


def cal_sin(x,num):
    y_cal = 0
    for i in range(2,num,2):
        y_cal -= (2/i * np.sin(i * x))
    #print(y_cal)
    return y_cal

def main():
    xmin = -2.0 * np.pi
    xmax = 2.0 * np.pi
    x = np.arange(xmin,xmax,0.01)

    plt.xticks([-2 * np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])

    y_cal = cal_sin(x,200)
    y = (np.pi/2) + y_cal

    plt.xlabel('frequency',rotation=0)
    plt.ylabel('amplitude',rotation=90)


    plt.plot(x,y,label='π/2 - sin(2t) - 1/2sin4t - 1/3sin6t - ・・・ - 1/99sin198t')
    plt.legend(loc='lower left')

    plt.grid()

    plt.show()

if __name__ == '__main__':
    main()


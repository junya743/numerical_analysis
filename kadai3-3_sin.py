import numpy as np
import matplotlib.pyplot as plt
import math


def sin_maclaurin(x, n):
    # 初期化
    y = 0
    
    # n次近似を計算
    for i in range(n):
        c = (-1)**i / math.factorial(2 * i + 1)
        t = c * x**(2 * i + 1)
        y = y + t
    return y
def main():
    xmin = -2.0 * np.pi
    xmax = 2.0 * np.pi
    x = np.arange(xmin,xmax,0.01)

    plt.xticks([-2 * np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])

    y = sin_maclaurin(x,10)

    plt.xlabel('frequency',rotation=0)
    plt.ylabel('amplitude',rotation=90)


    plt.plot(x,y,label='t - t^3/3! + t^5/5! - t^7/7! + ・・・ ')
    plt.legend(loc='lower left')

    plt.grid()

    plt.show()


if __name__ == '__main__':
    main()

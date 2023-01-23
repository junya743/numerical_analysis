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

    plt.xticks([-2 * np.pi,-np.pi,0,1,2,np.pi,4,2*np.pi],['-2π','-π','0','1','2','π','4','2π'])

    #y = sin_maclaurin(x,10)
    # ステップ関数
    step = 1 * (x > 0)
    # step1 = -1 * (x > 0)
    # step2 = x * (x > 0)
    # step3 = -2 * (x - 1) * (x > 1)
    # step4 = (x - 2) * (x > 2)
    

    plt.xlabel('frequency',rotation=0)
    plt.ylabel('amplitude',rotation=90)


    plt.plot(x,np.exp(-x) * np.sin(x) * step ,label='')
    plt.legend(loc='lower left')

    plt.grid()

    plt.show()


if __name__ == '__main__':
    main()

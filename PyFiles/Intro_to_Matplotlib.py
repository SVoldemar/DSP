import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    t = np.arange(0, 2, 0.01)  # time range with interval

    s1 = np.sin(1 * np.pi * t)  # sin waves
    s2 = np.sin(4 * np.pi * t)
    s3 = np.sin(8 * np.pi * t)
    s4 = np.sin(14 * np.pi * t)

    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(t, s1, c='r', linewidth=4.0)
    ax1.set(xlabel='Час (с)', ylabel='Значення', title='Сінус функція з частотою 0.5 Гц')
    ax1.grid()

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(t, s2, c='r', linewidth=4.0)
    ax2.set(xlabel='Час (с)', ylabel='Значення', title='Сінус функція з частотою 2 Гц')
    ax2.grid()

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(t, s3, c='r', linewidth=4.0)
    ax3.set(xlabel='Час (с)', ylabel='Значення', title='Сінус функція з частотою 4 Гц')
    ax3.grid()

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(t, s4, c='r', linewidth=4.0)
    ax4.set(xlabel='Час (с)', ylabel='Значення', title='Сінус функція з частотою 7 Гц')
    ax4.grid()

    plt.show()

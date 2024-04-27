#!/usr/bin/env python3

""" Task3: Using the libraries required in Task2 to perform some basic tasks """

import numpy as np
import matplotlib.pyplot as plt


def np_demo():
    """ Generate a 2d array of uniform randoms numbers in [0, 1) and write it to a file 'np_demo.csv'. """
    data = np.random.rand(10, 10)
    np.savetxt("np_demo.csv", data, fmt='%1.4e',
               delimiter=',', encoding='utf8')
    print("Random numbers saved in 'np_demo.csv'")


def mpl_demo():
    """ Sample two intervals of sin(x) and plot the intervals to a file 'mpl_demo.svg'. """
    x = np.arange(0, 4*np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y, "-or", label="sin(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("mpl_demo.svg")
    print("Plotted values in 'mpl_demo.svg'")    

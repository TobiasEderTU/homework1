#!/usr/bin/env python3

""" Task2: Obtaining basic information on required libraries """

import numpy
import matplotlib


def numpy_info():
    """ Obtains information on the numpy package in use and logs it to a file 'numpy_info.txt'. """
    numpy_name = numpy.__name__
    numpy_ver = numpy.__version__
    print(f"{numpy_name}\n{numpy_ver}\n")
    with open("numpy_info.txt", "w") as f:
        f.write(f"{numpy_name}\n{numpy_ver}\n")


def matplotlib_info():
    """ Obtains information on the matplotlib package in use and logs it to a file 'matplotlib_info.txt'. """
    matplotlib_name = matplotlib.__name__
    matplotlib_ver = matplotlib.__version__
    print(f"{matplotlib_name}\n{matplotlib_ver}\n")
    with open("matplotlib_info.txt", "w") as f:
        f.write(f"{matplotlib_name}\n{matplotlib_ver}\n")

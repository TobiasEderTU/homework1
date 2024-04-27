#!/usr/bin/env python3

""" Task1: Obtaining detailed information on the operating system and Python installation """

import platform


def os_info():
    """ Collects basic info on the operating system and logs it to a file 'os_info.txt'. """
    os_type = platform.system()
    os_rel = platform.release()
    os_ver = platform.version()
    print(f"{os_type}\n{os_rel}\n{os_ver}\n")
    with open("os_info.txt", "w") as f:
        f.write(f"{os_type}\n{os_rel}\n{os_ver}\n")


def python_info():
    """ Obtains information on Python installation in use and logs it to a file 'python_info.txt'. """
    python_ver = platform.python_version()
    python_impl = platform.python_implementation()
    print(f"{python_impl}\n{python_ver}\n")
    with open("python_info.txt", "w") as f:
        f.write(f"{python_impl}\n{python_ver}\n")

#!/usr/bin/env python3

""" Test for Task1: Checking the functionality in 'task1.py' using assertions """

import task1
import unittest
import os

class Test(unittest.TestCase):

    def test_os_info(self):
        expected_file = "os_info.txt"
        task1.os_info()
        self.assertTrue(os.path.isfile(expected_file))

    def test_python_info(self):
        expected_file = "python_info.txt"
        task1.python_info()
        self.assertTrue(os.path.isfile(expected_file))


if __name__ == '__main__':
    unittest.main()

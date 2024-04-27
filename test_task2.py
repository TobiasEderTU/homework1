#!/usr/bin/env python3

""" Test for Task2: Checking the functionality in 'task2.py' using assertions """

import task2
import unittest
import os


class Test(unittest.TestCase):

    def test_numpy_info(self):
        expected_file = "numpy_info.txt"
        task2.numpy_info()
        self.assertTrue(os.path.isfile(expected_file))

    def test_matplotlib_info(self):
        expected_file = "matplotlib_info.txt"
        task2.matplotlib_info()
        self.assertTrue(os.path.isfile(expected_file))


if __name__ == '__main__':
    unittest.main()

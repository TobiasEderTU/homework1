#!/usr/bin/env python3

""" Test for Task3: Checking the functionality in 'task3.py' using assertions """

import task3
import unittest
import os


class Test(unittest.TestCase):

    def test_np_demo(self):
        expected_file = "np_demo.csv"
        task3.np_demo()
        self.assertTrue(os.path.isfile(expected_file))

    def test_mpl_demo(self):
        expected_file = "mpl_demo.svg"
        task3.mpl_demo()
        self.assertTrue(os.path.isfile(expected_file))


if __name__ == '__main__':
    unittest.main()

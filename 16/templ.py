#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(foo(), 'BAR')

with open('input.txt', 'r') as fd:
    input_data = fd.read()

class Bar(object):
    def __init__(self):
        pass

    def __str__(self):
        pass

    __repr__ = __str__

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

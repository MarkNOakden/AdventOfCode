#!/usr/bin/env python2
import unittest
from hashlib import md5

input_key = 'iwrupvqb'

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertTrue(isAdventcoin('abcdef', 609043, 5))
    def test_2(self):
        self.assertTrue(isAdventcoin('pqrstuv', 1048970, 5))
    def test_3(self):
        self.assertFalse(isAdventcoin('pqrstuv', 10, 5))


def isAdventcoin(key, n, m):
    return md5(key+str(n)).hexdigest()[0:m] == '0'*m

def mineAdventcoin(key, start, m):
    i = start
    while not isAdventcoin(key, i, m):
        i+=1
    return i


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print "Part 1:", mineAdventcoin(input_key, 1, 5)
    print "Part 2:", mineAdventcoin(input_key, 1, 6)
    



#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(isvalid(3,4,5), True)
    def test_2(self):
        self.assertEqual(isvalid(5, 10, 25), False)

with open('input.txt', 'r') as fd:
    input_data = fd.read()

def isvalid(a, b, c):
    return not ((a + b) <= c)
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    count = 0

    for line in input_data.splitlines():
        l = map(int, line.split())
        a, b, c = sorted(l)
        if isvalid(a,b,c):
            count += 1

    print 'valid triangles: ', count

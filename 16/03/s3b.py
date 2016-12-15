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

    c1, c2, c3 = [], [], []

    for line in input_data.splitlines():
        l = map(int, line.split())

        c1.append(l[0])
        c2.append(l[1])
        c3.append(l[2])

        if len(c1) == 3:
            for k in [c1, c2, c3]:
                a, b, c = sorted(k)
                if isvalid(a,b,c):
                    count += 1
            c1, c2, c3 = [], [], []

    print 'valid triangles: ', count

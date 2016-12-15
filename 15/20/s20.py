#!/usr/bin/env python2
import unittest
from math import sqrt, floor

class TestIt(unittest.TestCase):
     # Part 1 tests
        
    def test_1(self):
        self.assertEqual(presents(1), 10)
 
    def test_2(self):
        self.assertEqual(presents(2), 30)

    def test_3(self):
        self.assertEqual(presents(3), 40)

    def test_4(self):
        self.assertEqual(presents(4), 70)
        
    def test_5(self):
        self.assertEqual(presents(5), 60)
 
    def test_6(self):
        self.assertEqual(presents(6), 120)

    def test_7(self):
        self.assertEqual(presents(7), 80)

    def test_8(self):
        self.assertEqual(presents(8), 150)

    def test_9(self):
        self.assertEqual(presents(9), 130)


def presents(house):
    n = house * 10 + 10 # elf N and elf 1
    n += 10 * sum(factors(house))
    return n

def factors(n):
    highest = int(sqrt(n))
    #yield 1
    for i in range(2, highest+1):
        if n % i == 0:
            if i*i == n:
                yield i
            else:
                yield i
                yield n/i
    #yield n
    
def presents2(house):
    n = house * 11
    if n < 50:
        n += 11
    for i in factors(house):
        if house <= 50*i:
            n += 11*i
    return n


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #house = 1
    #while presents(house) < 29000000:
    #    house += 1

    #print house, presents(house)

    house = 1
    while presents2(house) < 29000000:
        house += 1

    print house, presents2(house)

    
    
    


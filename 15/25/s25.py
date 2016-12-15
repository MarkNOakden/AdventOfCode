#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    # Part 1 tests
        
    def test_1(self):
        self.assertEqual(ordinal(1, 1), 1)
 
    def test_2(self):
        self.assertEqual(ordinal(1, 6), 21)

    def test_3(self):
        self.assertEqual(ordinal(6, 1), 16)

    def test_4(self):
        self.assertEqual(ordinal(3, 3), 13)

    def test_4a(self):
        self.assertEqual(ordinal(3, 1), 4)

    def test_4b(self):
        self.assertEqual(ordinal(3, 2), 8)

    def test_4c(self):
        self.assertEqual(ordinal(3, 4), 19)
 
    def test_5(self):
        self.assertEqual(code(1, 1, initial, multiplier, modulus), 20151125)

    def test_6(self):
        self.assertEqual(code(2, 1, initial, multiplier, modulus), 31916031)

    def test_7(self):
        self.assertEqual(code(6, 1, initial, multiplier, modulus), 33071741)

def ordinal(r, c):
    return 1 + (r * (r - 1))/2 + (c * (c - 1))/2 + r * (c - 1)

#
# code is essentially starting value * multiplier^(ordinal - 1) mod modulus
#
# i.e. if starting value is a, multiplier is b, ordinal - 1 is e
# and modulus is m
#
# code = (a * b^e) mod m
# code = (a mod m) * (b^e mod m)
# code = a * (b^e mod m) (a mod m is a since a < m)
#
# b^e mod m can be efficiently computed
# (see https://en.wikipedia.org/wiki/Modular_exponentiation)
#
# python pow has optional third argument to do modular exponent
#
def code(r, c, a, b, m): # row, column, initial, multiplier, modulus
    e = ordinal(r, c) - 1
    output = a

    if e == 0:
        return output

    exponent = pow(b, e, m)
    
    return (initial * exponent) % m
    
if __name__ == '__main__':
    row = 2978
    column = 3083

    multiplier = 252533
    modulus = 33554393

    initial = 20151125
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print 'Part 1'
    print 'code is', code(row, column, initial, multiplier, modulus)
    
    
    
    


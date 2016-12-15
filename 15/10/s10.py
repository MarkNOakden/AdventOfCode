#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    # Part 1 tests
        
    def test_1(self):
        self.assertEqual(doit('1'), '11')
 
    def test_2(self):
        self.assertEqual(doit('11'), '21')

    def test_3(self):
        self.assertEqual(doit('21'), '1211')

    def test_4(self):
        self.assertEqual(doit('1211'), '111221')

    def test_5(self):
        self.assertEqual(doit('111221'), '312211')
 
input_data = '3113322113'
N = 50

def doit(instr):
    count = 1
    last = instr[0]
    output = ''
    for c in instr[1:]:
        if c != last:
            output += str(count)
            output += last
            last = c
            count = 1
        else:
            count += 1
    output += str(count)
    output += last
    return output

def shorten(str, N = 12):
    if len(str) < N*2:
        return str
    else:
        return str[0:N]+'...'+str[len(str)-N:]


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    s = input_data
    for i in range(N):
        s = doit(s)
        print str(i+1) + ' ' + shorten(s) + ' ' + str(len(s))
        
    


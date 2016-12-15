#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    # Part 1 tests
        
    def test_1(self):
        self.assertEqual(total_wastage(test_data), 19)
        
    #def test_2(self):
    #    self.assertEqual(self.c.nodeValue('e', 0), '507')
        
    #def test_3(self):
    #    self.assertEqual(self.c.nodeValue('f', 0), '492')
        
    #def test_4(self):
    #    self.assertEqual(self.c.nodeValue('g', 0), '114')
        

# test input
fd = open("test.txt", 'r')
test_data = fd.read()
fd.close()

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

def wastage(escapedStr):
    return len(encoded(escapedStr)) - len(escapedStr)


def encoded(instr):
    out=''
    for c in instr:
        if c == '\\':
            out += '\\\\'
        elif c == '"':
            out += '\\"'
        else:
            out += c
    return '"' + out + '"'

    
def total_wastage(data):
    w = 0
    for l in data.splitlines():
        w += wastage(l)
    return w

for l in test_data.splitlines():
    foo=encoded(l)
    print l + ' ; '+str(len(l))+' ; /'+foo+'/ '+str(len(foo))
                      
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print "Part 2 - total wastage = "+str(total_wastage(input_data))
    


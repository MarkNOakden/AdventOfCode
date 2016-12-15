#!/usr/bin/env python2
import unittest
from collections import Counter

test_data = '''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
'''

with open('input.txt', 'r') as fd:
    input_data = fd.read()

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(msg(test_data)[0], 'easter')
    def test_2(self):
        self.assertEqual(msg(test_data)[1], 'advent')

def msg(str):
    strlist = str.splitlines()
    output = []
    output2 = []
    for i in range(len(strlist[0])):
        column = [x[i] for x in strlist]
        counter = Counter(column)
        output.append(counter.most_common(1)[0][0])
        output2.append(counter.most_common()[-1][0])
    return ''.join(output), ''.join(output2)
                   

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print 'Message1 is:',msg(input_data)[0]
    print 'Message2 is:',msg(input_data)[1]
    

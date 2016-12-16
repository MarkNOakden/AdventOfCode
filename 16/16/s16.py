#!/usr/bin/env python2
import unittest
import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--part',
                    help='Part 1 or 2 (use part 0 to test)',
                    type=int)
parser.add_argument('-v', '--verbose',
                    help='produce verbose output',
                    action='store_true')
parser.add_argument('-i', '--input',
                    help='input string',
                    type=str)
parser.add_argument('-d', '--disklen',
                    help='length of disk',
                    type=int)

args = parser.parse_args()

if args.part is None:
    part = 0
else:
    part = args.part

if args.input is None:
    input_data = '10001001100000001'
else:
    input_data = args.input

if args.disklen is None:
    if part == 1:
        disklen = 272
    elif part == 2:
        disklen = 35651584
else:
    disklen = args.disklen

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(nextPat('1'), '100')
    def test_2(self):
        self.assertEqual(nextPat('0'), '001')
    def test_3(self):
        self.assertEqual(nextPat('11111'), '11111000000')
    def test_4(self):
        self.assertEqual(nextPat('111100001010'),
                         '1111000010100101011110000')
    def test_5(self):
        self.assertEqual(checksum('110010110100'), '100')
    def test_6(self):
        self.assertEqual(checksum('10000011110010000111'), '01100')
    def test_7(self):
        self.assertEqual(pattern('10000', 20),
                         '10000011110010000111')

TRANSTABLE = string.maketrans('10', '01')

def nextPat(lastPat):
    return lastPat + '0' + lastPat[::-1].translate(TRANSTABLE)

def checksum(pat):
    assert(len(pat) % 2 == 0)
    while len(pat) % 2 != 1:
        newPat = ''
        for i, j in zip(pat[::2], pat[1::2]):
            newPat += '1' if i == j else '0'
        pat = newPat
    return pat

def pattern(inputPat, disklen):
    while len(inputPat) < disklen:
        inputPat = nextPat(inputPat)
    return inputPat[:disklen]

if __name__ == '__main__':
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif part == 1 or part == 2:
        print ('Checksum for disk of length {}, from pattern \'{}\''
               + ' is \'{}\'').format(disklen, input_data,
                                      checksum(pattern(input_data,
                                                       disklen)))
    else:
        print 'Part {} not implemented'.format(part)

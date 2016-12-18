#!/usr/bin/env python2
import unittest
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--part',
                    help='Part 1 or 2 (use part 0 to test)',
                    type=int)
parser.add_argument('-v', '--verbose',
                    help='produce verbose output',
                    action='store_true')
parser.add_argument('-o', '--optimise',
                    help='Don\'t calculate the entire block',
                    action='store_true')

args = parser.parse_args()

if args.part is None:
    part = 0
else:
    part = args.part

tdata1 = '''..^^.
.^^^^
^^..^
'''.splitlines()

tdata2 = '''.^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^
'''.splitlines()

class TestIt(unittest.TestCase):
    def _tblock(self, block):
        last = block[0]
        for line in block[1:]:
            self.assertEqual(nextLine(last), line)
            last = line
            
    def test_1(self):
        self._tblock(tdata1)
        
    def test_2(self):
        self._tblock(tdata2)

    def test_3(self):
        self.assertEqual(mkBlock(tdata1[0], 3), tdata1)

    def test_4(self):
        self.assertEqual(mkBlock(tdata2[0], 10), tdata2)

    def test_5(self):
        self.assertEqual(countSafeBlock(tdata1[0], 3), 6)

    def test_6(self):
        self.assertEqual(countSafeBlock(tdata2[0], 10), 38)
        

        
rules = {'^^.': '^',
         '.^^': '^',
         '^..': '^',
         '..^': '^'}
         
def nextLine(lastLine):
    xlastLine = '.' + lastLine + '.'
    out = ''
    for i in range(len(lastLine)):
        lcr = xlastLine[i:i+3]
        if lcr in rules:
            out += rules[lcr]
        else:
            out += '.'
    return out
        
def countSafeBlock(initial, rows):
    block = mkBlock(initial, rows)
    return len([x for x in ''.join(block) if x == '.'])

def mkBlock(initial, length):
    out = [initial]
    lastLine = initial
    while len(out) != length:
        lastLine = nextLine(lastLine)
        out.append(lastLine)
    return out

def countSafeStream(initial, rows):
    return sum(stream(initial, rows))

def stream(initial, rows):
    last = initial
    for i in range(rows):
        yield len([x for x in last if x == '.'])
        last = nextLine(last)

        
if args.optimise:
    countSafe = countSafeStream
else:
    countSafe = countSafeBlock

with open('input.txt', 'r') as fd:
    input_data = fd.read()

if __name__ == '__main__':
    input_data = input_data.splitlines()[0]
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif part == 1:
        print 'Part 1 #traps is {}'.format(
            countSafe(input_data, 40))
    elif part == 2:
        print 'Part 2 #traps is {}'.format(
            countSafe(input_data, 400000))
    else:
        print 'Part {} not implemented'.format(part)

#!/usr/bin/env python2
import unittest
from itertools import count
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--part',
                    help='part 1 or part 2 (0 to test)',
                    type=int)
parser.add_argument('-o', '--optimise',
                    help='use optimised discStack class',
                    action='store_true')

args = parser.parse_args()
if args.part is not None:
    part = args.part
else:
    part = 0

class TestIt(unittest.TestCase):
    def setUp(self):
        self.stack = discStack(parseInput(test_data))
        
    def test_1(self):
        self.assertFalse(self.stack.capsulePasses(0))
        
    def test_2(self):
        self.assertTrue(self.stack.capsulePasses(5))

    def test_3(self):
        self.assertEqual(self.stack.firstPassTime(), 5)

test_data = '''Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
'''

# assume discs listed in order
parseRE = re.compile(r' has ([0-9]+) .*ion ([0-9]+).')

def parseInput(s):
    discs = []
    for line in s.splitlines():
        match = parseRE.search(line)
        discs.append((int(match.group(1)), int(match.group(2))))
    return discs

        
with open('input.txt', 'r') as fd:
    input_data = fd.read()

class discStackOrig(object):
    def __init__(self, discs):
        self.discPositions = [i[0] for i in discs]
        self.discStart = [i[1] for i in discs]


    def capsulePasses(self, t):
        delay = count(1)
        for p, offset in zip(self.discPositions, self.discStart):
            delta = delay.next()
            if (t + offset + delta) % p != 0:
                return False
        return True

    def firstPassTime(self):
        i = 0
        while not self.capsulePasses(i):
            i += 1
        return i
        
    def __str__(self):
        
        pass

    __repr__ = __str__

class discStackOpt(discStackOrig):
    def __init__(self, discs):
        discStackOrig.__init__(self, discs)
        delay = count(1)
        # pre-add the delays
        self.discStart = [i + delay.next() for i in self.discStart]
        # re-order so we check the biggest disc first (== most
        # likely to fail)
        self.discPositions, self.discStart = zip(
            *sorted(zip(self.discPositions, self.discStart),
                    key=lambda i: -i[0]))

    def capsulePasses(self, t):
        for p, offset in zip(self.discPositions, self.discStart):
            if (t + offset) % p != 0:
                return False
        return True

if args.optimise:
    print 'using optimised discStack class'
    discStack = discStackOpt
else:
    print 'using original discStack class'
    discStack = discStackOrig

if __name__ == '__main__':
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif part == 1:
        d = discStack(parseInput(input_data))
        print 'Part 1: capsule passes at t={}'.format(
            d.firstPassTime())
    elif part == 2:
        part2_input = parseInput(input_data)
        part2_input.append((11, 0))
        d = discStack(part2_input)
        print 'Part 2: capsule passes at t={}'.format(
            d.firstPassTime())
        

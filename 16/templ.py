#!/usr/bin/env python2
import unittest
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--part',
                    help='Part 1 or 2 (use part 0 to test)',
                    type=int)
parser.add_argument('-v', '--verbose',
                    help='produce verbose output',
                    action='store_true')

args = parser.parse_args()

if args.part is None:
    part = 0
else:
    part = args.part


class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(foo(), 'BAR')

with open('input.txt', 'r') as fd:
    input_data = fd.read()

class Bar(object):
    def __init__(self):
        pass

    def __str__(self):
        pass

    __repr__ = __str__

if __name__ == '__main__':
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif part == 1:
        pass
    elif part == 2:
        pass
    else:
        print 'Part {} not implemented'.format(part)

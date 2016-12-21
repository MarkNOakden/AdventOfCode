#!/usr/bin/env python2
import unittest
import argparse
import re
from itertools import permutations

swapRE = re.compile(
    r'swap (position|letter) (\d+|[a-z])'
    + r' with (position|letter) (\d+|[a-z])')

rotateLRRE = re.compile(r'rotate (left|right) (\d+) steps?')

rotateLetterRE = re.compile(
    r'rotate based on position of letter ([a-z])')

reverseRE = re.compile(
    r'reverse positions (\d+) through (\d+)')

moveRE = re.compile(
    r'move position (\d+) to position (\d+)')


class TestIt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.process = Scrambler('abcde').process
        
    def test_1(self):
        self.assertEqual(
            str(TestIt.process('swap position 4 with position 0')),
            'ebcda')
        
    def test_2(self):
        self.assertEqual(
            str(TestIt.process('swap letter d with letter b')),
            'edcba')
        
    def test_3(self):
        self.assertEqual(
            str(TestIt.process('reverse positions 0 through 4')),
            'abcde')
        
    def test_4(self):
        self.assertEqual(
            str(TestIt.process('rotate left 1 step')),
            'bcdea')
        
    def test_5(self):
        self.assertEqual(
            str(TestIt.process('move position 1 to position 4')),
            'bdeac')
        
    def test_6(self):
        self.assertEqual(
            str(TestIt.process('move position 3 to position 0')),
            'abdec')
        
    def test_7(self):
        self.assertEqual(
            str(TestIt.process('rotate based on position of letter b')),
            'ecabd')
        
    def test_8(self):
        self.assertEqual(
            str(TestIt.process('rotate based on position of letter d')),
            'decab')


class Scrambler(object):
    def __init__(self, seed):
        self._state = list(seed)
        self._funcs = ((swapRE, self._swap),
                       (rotateLRRE, self._rotateLR),
                       (rotateLetterRE, self._rotateLetter),
                       (reverseRE, self._reverse),
                       (moveRE, self._move))

    def set(self, newseed):
        self._state = newseed
        return self

    def process(self, instructions):
        for instr in instructions.splitlines():
            self._dispatcher(instr)
        return self
            
    def _dispatcher(self, line):
        matched = False
        for _re, _func  in self._funcs:
            match = _re.search(line)
            if match:
                matched = True
                _func(match)
                break
        if not matched:
            raise ValueError(
                'line /{}/ did not match any RE'.format(line))
        return self

    def _swap(self, match):
        mode, a, b = match.group(1, 2, 4)
        
        if mode == 'position':
            a, b = int(a), int(b)
        else:
            a, b = map(int, map(self._state.index, (a, b)))
        
        self._state[a], self._state[b] = (self._state[b],
                                          self._state[a])
            

    def _rotateLR(self, match):
        lr, steps = match.group(1, 2)
        steps = int(steps) % len(self._state)
        if lr == 'right':
            steps = len(self._state) - steps
        self._state = self._state[steps:] + self._state[:steps]

    def _rotateLetter(self, match):
        a = match.group(1)
        ix = self._state.index(a)
        steps = 1 + ix + (1 if ix >= 4 else 0)
        # to the right
        steps = len(self._state) - steps
        self._state = self._state[steps:] + self._state[:steps]
        

    def _reverse(self, match):
        a, b = sorted(map(int, match.group(1, 2)))
        self._state = (self._state[:a]
                       + list(reversed(self._state[a:b+1]))
                       + self._state[b+1:])

    def _move(self, match):
        a, b = map(int, match.group(1, 2))
        ch = self._state[a]
        del self._state[a]
        self._state.insert(b, ch)


    def __str__(self):
        return ''.join(self._state)

    __repr__ = __str__


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--part',
                        help='Part 1 or 2 (use part 0 to test,'
                        + ' or 3 to show \'rotate based on'
                        + ' position of letter\' mappings)',
                        type=int)
    parser.add_argument('-l', '--length',
                        help='Password length for '
                        + ' \'position of letter\' mappings',
                        type=int)
    parser.add_argument('-v', '--verbose',
                        help='produce verbose output',
                        action='store_true')

    args = parser.parse_args()

    with open('input.txt', 'r') as fd:
        input_data = fd.read()

    if args.part is None:
        part = 0
    else:
        part = args.part

    if args.length is None:
        args.length = 4
        
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif part == 1:
        print 'Part 1 password is {}'.format(
            Scrambler('abcdefgh').process(input_data))
    elif part == 2:
        scrambler = Scrambler('abcdefgh')
        tried = 0
        for start in permutations('abcdefgh'):
            tried += 1
            out = str(scrambler.set(list(start)).process(input_data))
            if out == 'fbgdceah':
                print ('Part 2 password is {}\n'
                       + '(Tried {} passwords)').format(
                    ''.join(start))
                
                break
    elif part == 3:
        # bonus extra section because I was interested in when the
        # rotate based on position of letter X mapping was one-to-one
        # and hence reversible
        testpat = list('.' * args.length)
        s = Scrambler(testpat)
        seen = set()
        print 'Results of \'rotate based on position of letter f\''
        print 'Input length is {}'.format(args.length)
        print ''
        print ('{:' + str(args.length + 2)
               + '}  {:' + str(args.length + 1)
               + '}').format('In', 'Out')
        print ''
        for i in range(len(testpat)):
            x = testpat[:]
            x[i] = 'f'
            out = str(s.set(x).process(
                'rotate based on position of letter f'))
            seen.add(out)
            print ''.join(x), '->', out
        print ''
        print '{} one-to-one'.format(
            'IS' if len(seen) == len(testpat) else 'IS NOT')
        print ''
        print '-'*40          
    else:
        print 'Part {} not implemented'.format(part)

#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(nextdigit('5', 'ULL'), '1')
    def test_2(self):
        self.assertEqual(nextdigit('1', 'RRDDD'), '9')
    def test_3(self):
        self.assertEqual(nextdigit('9', 'LURDL'), '8')
    def test_4(self):
        self.assertEqual(nextdigit('8', 'UUUUD'), '5')
    def test_5(self):
        self.assertEqual(nextdigit2('5', 'ULL'), '5')
    def test_6(self):
        self.assertEqual(nextdigit2('5', 'RRDDD'), 'D')
    def test_7(self):
        self.assertEqual(nextdigit2('D', 'LURDL'), 'B')
    def test_8(self):
        self.assertEqual(nextdigit2('B', 'UUUUD'), '3')


with open('input.txt', 'r') as fd:
    input_data = fd.read()

initial = '5'

def nextdigit(initial, instr):
    where = initial
    for i in instr:
        where = move(where, i)
    return where


def move(ifrom, c):
    result='X'
    #ifrom is 123456789
    # layout
    # 123
    # 456
    # 789
    if c == 'U':
        if ifrom in '123':
            result = ifrom
        else:
            result = str(int(ifrom) - 3)
    elif c == 'D':
        if ifrom in '789':
            result = ifrom
        else:
            result = str(int(ifrom) + 3)
    elif c == 'L':
        if ifrom in '147':
            result = ifrom
        else:
            result = str(int(ifrom) - 1)
    elif c == 'R':
        if ifrom in '369':
            result = ifrom
        else:
            result = str(int(ifrom) + 1)
    return result

def nextdigit2(initial, instr):
    where = initial
    for i in instr:
        where = move2(where, i)
    return where

mx = ['.......',
      '...1...',
      '..234..',
      '.56789.',
      '..ABC..',
      '...D...',
      '.......']

def move2(ifrom, c):
    irow, icol = 0, 0
    for row, string in enumerate(mx):
        if ifrom in string:
            irow = row
            icol = string.index(ifrom)
    if c == 'U':
        irow = irow - 1
    elif c == 'D':
        irow = irow + 1
    elif c == 'L':
        icol = icol - 1
    elif c == 'R':
        icol = icol + 1

    if mx[irow][icol] != '.':
        return mx[irow][icol]
    else:
        return ifrom


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    on = initial
    code = ''

    for line in input_data.splitlines():
        on = nextdigit(on, line)
        code += on

    print code

    on = initial
    code = ''

    for line in input_data.splitlines():
        on = nextdigit2(on, line)
        code += on

    print code

#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    # using class method setUpClass because we want this object
    # created once and reused for all tests
    @classmethod
    def setUpClass(cls):
        cls.disp = Display(rows=3, columns=7)
    def test_00(self):
        self.assertEqual(TestIt.disp.dump(),
                         '.......\n.......\n.......')
    def test_01(self):
        self.assertEqual(TestIt.disp.litCount(), 0)
    def test_02(self):
        self.assertEqual(TestIt.disp.rect(3, 2).dump(),
                         '###....\n###....\n.......')
    def test_03(self):
        self.assertEqual(TestIt.disp.rotatex(1, 1).dump(),
                         '#.#....\n###....\n.#.....')
    def test_04(self):
        self.assertEqual(TestIt.disp.rotatey(0, 4).dump(),
                         '....#.#\n###....\n.#.....')
    def test_05(self):
        self.assertEqual(TestIt.disp.rotatex(1, 1).dump(),
                         '.#..#.#\n#.#....\n.#.....')
    def test_06(self):
        self.assertEqual(TestIt.disp.litCount(), 6)

with open('input.txt', 'r') as fd:
    input_data = fd.read()

class Display(object):
    def __init__(self, rows=6, columns=50, init=None):
        self.rows = rows
        self.columns = columns
        if init is None:
            self.array = [list('.' * columns) for i in range(rows)]
        else:
            assert(len(init)==self.rows * self.columns)
            self.array = []
            for i in rows:
                rowlist = list(init[i*columns:(i+1)*columns])

    def rect(self, x, y):
        for i in range(y):
            for j in range(x):
                self.array[i][j] = '#'
        return self

    def rotatex(self, col, count):
        count = count % self.rows
        for i in range(count):
            self.stepx(col)
        return self

    def stepx(self, col):
        carry = self.array[-1][col]
        for i in reversed(range(self.rows - 1)):
            self.array[i + 1][col] = self.array[i][col]
        self.array[0][col] = carry

    def rotatey(self, row, count):
        count = count % self.columns
        self.array[row] = self.array[row][-count:] \
            + self.array[row][:-count]
        return self       

    def dump(self):
        return '\n'.join([''.join(r) for r in self.array])

    def prettyDump(self):
        on = unichr(0x2588)
        off = ' '
        return '\n'.join([''.join(on if c =='#' else off for c in r)
                          for r in self.array])

    def litCount(self):
        return sum([len([x for x in r if x == '#'])
                    for r in self.array])

    def dispatch(self, instr):
        if instr.startswith('rect'):
            x, y = map(int, instr[5:].split('x'))
            self.rect(x,y)
        elif instr.startswith('rotate '):
            direction, sep, instr = instr[7:].partition(' ')
            discard, sep, instr = instr.partition('=')
            which, sep, count = instr.partition(' by ')
            if direction == 'row':
                self.rotatey(int(which), int(count))
            else:
                self.rotatex(int(which), int(count))
    
    def __str__(self):
        pass

    __repr__ = __str__

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    display = Display(rows=6, columns=50)
    for instr in input_data.splitlines():
        display.dispatch(instr)

    print '{} pixels are lit'.format(display.litCount())

    print display.prettyDump()

#!/usr/bin/env python2
import unittest
from exceptions import IndexError

import re
class TestIt(unittest.TestCase):
    def setUp(self):
        self.initial = LightArray(test_data)
        self.initial2 = LightArray2(test_data)

    def tearDown(self):
        del self.initial
        del self.initial2
      
    def test_1(self):
        self.initial.evolve(1)
        self.assertEqual(str(self.initial), test_out[0])
    def test_2(self):
        self.assertEqual(str(self.initial.evolve(2)), test_out[1])
    def test_3(self):
        self.assertEqual(str(self.initial.evolve(3)), test_out[2])
    def test_4(self):
        self.assertEqual(str(self.initial.evolve(4)), test_out[3])

    def test_5(self):
        self.assertEqual(self.initial.evolve(4).count(), 4)

    def test_6(self):
        self.initial2.evolve(5)
        self.assertEqual(str(self.initial2), test_out2)
        

# test input
#fd = open("test.txt", 'r')
#test_data = fd.read()
#fd.close()
test_data='''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''

test_out=[]
test_out.append('''..##..
..##.#
...##.
......
#.....
#.##..''')

test_out.append('''..###.
......
..###.
......
.#....
.#....''')

test_out.append('''...#..
......
...#..
..##..
......
......''')

test_out.append('''......
......
..##..
..##..
......
......''')

test_out2 = '''##.###
.##..#
.##...
.##...
#.#...
##...#'''

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

class LightArray(object):

    def __init__(self, str):
        self.elements = str.splitlines()

    def evolve(self, steps = 1):
        for i in range(steps):
            nextElements = []
            for y, row in enumerate(self.elements):
                nextRow = ''
                for x, column in enumerate(row):
                    nextRow += self.nextEl(x, y)
                nextElements.append(nextRow)
            self.elements = nextElements
        return self

    def nextEl(self, x, y):
        this = self.element(x, y)
        count = 0
        for m, n in [ (x-1, y-1), (x-1, y), (x-1, y+1),\
                      (x, y-1),             (x, y+1), \
                      (x+1, y-1), (x+1, y), (x+1, y+1) ]:
            neighbour = self.element(m, n)
            if neighbour == '#':
                count += 1
        if this == '#':
            if count == 2 or count == 3:
                nxt = '#'
            else:
                nxt = '.'
        else:
            if count == 3:
                nxt = '#'
            else:
                nxt = '.'
        return nxt

    def element(self, x, y):
        if x < 0 or y < 0:
            return '.'
        size = len(self.elements)
        
        try:
            return self.elements[y][x]
        except IndexError:
            return '.'

    def count(self):
        return sum( [sum([1 for i in row if i == '#']) \
                     for row in self.elements])
                
    def __str__(self):
        return '\n'.join(self.elements)

    __repr__ = __str__

class LightArray2(LightArray):
    def __init__(self, str):
        LightArray.__init__(self, str)
        self.lightCorners()

    def lightCorners(self):
        self.elements[0]= '#'+self.elements[0][1:-1]+'#'
        self.elements[-1]= '#'+self.elements[-1][1:-1]+'#'


    def evolve(self, steps):
        for i in range(steps):
            LightArray.evolve(self, 1)
            self.lightCorners()
        return self
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    part1 = LightArray(input_data)
    print 'lights on:', part1.evolve(100).count()
    part2 = LightArray2(input_data)
    print 'pt2, lights on', part2.evolve(100).count()

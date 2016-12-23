#!/usr/bin/env python2
from __future__ import division
import unittest
import argparse
import re
from itertools import permutations

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(foo(), 'BAR')

class Node(object):
    def __init__(self, x, y, size, used, *ignored):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.containsGoalData = False
        self.isAccessNode = False

    @property
    def avail(self):
        return self.size - self.used

    @property
    def usepct(self):
        return int(100 * self.used / self.size)
    
    def move(otherNode):
        assert(self.isNeighbour(otherNode))

    def isNeighbour(self, otherNode):
        return otherNode in self.neighbours()

    def neighbours(self):
        l = []
        #find neighbours here
        return l

    def gridrep(self):
        l, c, r = ' . '
        if self.isAccessNode:
            l, r = '()'
        if self.containsGoalData:
            c = 'G'
        elif self.usepct >= 90:
            c = '#'
        elif self.used == 0:
            c = '_'
        return ''.join((l, c, r))

    def __repr__(self):
        return 'Node({}, {}, {}, {}, {}, {})'.format(self.x,
                                                     self.y,
                                                     self.size,
                                                     self.used,
                                                     self.avail,
                                                     self.usepct)
    def  __str__(self):
        name = 'x{}-y{}'.format(self.x, self.y)
        fmt = '/dev/grid/node-{:<7} {:>4}T {:>4}T {:>5}T {:>4}%'
        return fmt.format(name, self.size, self.used, self.avail,
                          self.usepct)
            

nodeRE = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)'
                    + r'\s+(\d+)T'
                    + r'\s+(\d+)T'
                    + r'\s+(\d+)T'
                    + r'\s+(\d+)%')
          
def loadConfig(input_data):
    nodelist = []
    for l in input_data.splitlines():
        match = nodeRE.match(l)
        if match:
            x, y, size, used, avail, usepct = map(int,
                                                  match.group(1, 2, 3,
                                                          4, 5, 6))
            node = Node(x, y, size, used)
            assert(node.avail == avail)
            assert(node.usepct == usepct)
            nodelist.append(node)
    return nodelist

def viablePair(nodeA, nodeB):
    #print 'Comparing {} with {}'.format(nodeA, nodeB)
    if nodeA.x == nodeB.x and nodeA.y == nodeB.y:
        #print '   Node A = Node B'
        return False
    if nodeA.used == 0:
        #print '   NodeA is empty'
        return False
    if nodeB.avail < nodeA.used:
        #print '   Not enough space'
        return False
    return True

def countPairs(nodeList, filterFunc):
    count = 0
    for i, j in permutations(nodeList, 2):
        if filterFunc(i, j):
            count += 1
    return count

class Grid(object):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.nodelist = []
        self.grid = []
        for _ in range(columns):
            l = []
            for z in range(rows):
                l.append(None)
            self.grid.append(l)

    def __getitem__(self, i):
        return self.grid[i]

    def initialise(self, nodeList):
        print 'initialising'
        self.nodelist = nodeList[:] # copy
        for node in self.nodelist:
            self.grid[node.x][node.y] = node
        return self

    def dump(self, showmoves=False):
        s = ''
        for y in range(self.rows):
            for x in range(self.columns):
                s += grid[x][y].gridrep()
            s += '\n'
        print s
        return s

            

def getPairs(nodeList, filterFunc):
    return [i for i in permutations(nodeList, 2) if viablePair(i[0], i[1])]
            
if __name__ == '__main__':
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

    with open('input.txt', 'r') as fd:
        input_data = fd.read()

    nl = loadConfig(input_data)
    print 'Loaded {} nodes...'.format(len(nl))
    
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif part == 1:
        print 'Part 1: # viable pairs is {} (out of {})'.format(
            len(getPairs(nl, viablePair)), len(list(permutations(nl, 2))))
    elif part == 2:
        rows = max(node.y for node in nl) + 1
        columns = max(node.x for node in nl) + 1
        assert(len(nl) == rows * columns)
        grid = Grid(rows, columns)
        grid.initialise(nl)
        grid.dump()
        grid[0][0].isAccessNode = True
        grid[-1][0].containsGoalData = True
        grid.dump()
    else:
        print 'Part {} not implemented'.format(part)

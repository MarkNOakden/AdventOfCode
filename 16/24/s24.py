#!/usr/bin/env python2
from collections import deque
import unittest
import argparse
from itertools import combinations, permutations

test_data = '''###########
#0.1.....2#
#.#######.#
#4.......3#
###########
'''

GOALCHARS = '0123456789' # assumes no more than 10

class TestIt(unittest.TestCase):
    def setUp(self):
        self.map = Map(test_data)

    def test_0(self):
        self.assertEqual(self.map.goal,
                         set(('0', '1', '2', '3', '4')))
        
    def test_1(self):
        self.assertEqual(self.map.getDepth()[0], 14)

    def test_2(self):
        self.assertEqual(self.map.startPos(), (1, 1))

    def test_3(self):
        dump = self.map.dumps()
        #self.map.dump(10, 10)
        self.assertEqual(dump, test_data)

class Map(object):
    def __init__(self, map_data):
        self.map = [ list(l) for l in map_data.splitlines()]
        self.goal = self.getGoal()

    def startPos(self):
        return self.findNum('0')
    
    def findNum(self, char):
        for r, row  in enumerate(self.map):
            try:
                c = row.index(char)
                return r, c
            except ValueError:
                pass
        return None

    def getGoal(self):
        goal = set()
        for a in self.map:
            for b in a:
                if b in GOALCHARS:
                    goal.add(b)
        return goal

    def getDepth(self, part2=False):
        # build a dict of inter-digit distances
        goalList = sorted(list(self.goal))
        distances = {}
        for pair in combinations(goalList, 2):
            if args.verbose:
                print 'searching {}...'.format(pair)
            start = self.findNum(pair[0])
            end = self.findNum(pair[1])
            depth, path = self.getDepthByBFS(start, end)
            distances[pair] = depth, path
            if args.verbose:
                print '... distance is {}'.format(depth)
        # check each permutation starting from 0
        zero = goalList[0]
        rest = goalList[1:]
        shortest = None
        for numberPath in permutations(rest, len(rest)):
            thisdistance = 0
            lastNum = zero
            for nextNum in numberPath:
                ix = tuple(sorted((lastNum, nextNum)))
                thisdistance += distances[ix][0]
                lastNum = nextNum
            if part2:
                thisdistance += distances[tuple(('0', nextNum))][0]
            if shortest is None or thisdistance < shortest:
                shortest = thisdistance
        return shortest
        
        
    def getDepthByBFS(self, start, end, maxdepth = None):
        depth = 0
        queue = deque()
        path = []
        # we always start at a number
        path.append(start)
        queue.append((depth, start, path))
        # still doing the canonical "visited is set()" thang
        # since I hear "in set()" is quicker than  "in dict()"
        visited = set(start)

        while queue:
            depth, node, path = queue.popleft()
            if maxdepth is not None:
                if depth >= maxdepth:
                    return None

            if node == end:
                return depth, path

            nextList = self.getChildren(node)
            for childpos in nextList:
                newpath = list(path)
                if childpos not in visited:
                    r, c = childpos
                    newpath.append(childpos)
                    queue.append((depth + 1, childpos, newpath))
                    visited.add(childpos)
        # No path
        return None

    def getChildren(self, node):
        offsets = ((0,-1), (1, 0), (0, 1), (-1, 0))
        nodelist = []
        for delta in offsets:
            candidate = (node[0] + delta[0], node[1] + delta[1])
            if self.isPassage(candidate):
                nodelist.append(candidate)
        return nodelist

    def isPassage(self, node):
        x = node[0]
        y = node[1]
        return self.map[x][y] != '#'

    def dumps(self):
        s = ''
        for y in range(len(self.map)):
            s += ''.join(self.map[y]) + '\n'
        return s

    def dump(self):
        print self.dumps()
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--part',
                        help='part 1 or 2 (0 to test)',
                        type=int)
    parser.add_argument('-v', '--verbose',
                        help='whether to dump maps or not',
                        action='store_true')

    args = parser.parse_args()

    if args.part is None:
        part = 0
    else:
        part = args.part

    with open('input.txt', 'r') as fd:
        input_data = fd.read()
        
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif part == 1:
        part1 = Map(input_data)
        print 'Shortest path was {} steps'.format(
            part1.getDepth())
    elif part == 2:
        part2 = Map(input_data)
        print 'Shortest path was {} steps'.format(
            part2.getDepth(part2 = True))


    

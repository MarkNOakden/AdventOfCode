#!/usr/bin/env python2
from collections import deque
import unittest

class TestIt(unittest.TestCase):
    def setUp(self):
        self.map = Map(10)
        
    def test_1(self):
        self.assertEqual(self.map.getDepthByBFS((1,1), (7, 4)), 11)

    def test_2(self):
        self.map.getDepthByBFS((1,1), (7, 4), maxdepth=2)
        #self.map.dump(10, 10)
        self.assertEqual(self.map.visitcount(), 5)

class Map(object):
    def __init__(self, fav):
        self.favourite = fav
        self.cache = {}

    def getDepthByBFS(self, start, end, maxdepth = None):
        depth = 0
        queue = deque()
        queue.append((depth, start))
        # still doing the canonical "visited is set()" thang
        # since I hear "in set()" is quicker than  "in dict()"
        visited = set(start)

        while queue:
            depth, node = queue.popleft()
            #print depth, node
            if maxdepth is not None:
                if depth >= maxdepth:
                    return None
            #print node

            if node == end:
                return depth

            nextList = self.getChildren(node)
            for childpos in nextList:
                if childpos not in visited:
                    queue.append((depth + 1, childpos))
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
        if node in self.cache:
            return self.cache[node]
        else:
            x = node[0]
            y = node[1]
            if x < 0 or y < 0:
                self.cache[node] = False
                return False
            num = x * (x + 3) + y * (x + x + 1 + y) + self.favourite
            bits = len([i for i in '{:b}'.format(num) if i == '1'])
            self.cache[node] = (bits % 2) == 0
            return self.cache[node]

    def visitcount(self):
        return len([key for key in self.cache.keys()
                      if (key[0] >=0 and key[1] >= 0
                          and self.cache[key])])

    def dump(self, cols, rows):
        print ''
        for y in range(cols):
            for x in range(rows):
                if (x, y) in self.cache:
                    if self.cache[(x, y)]:
                        print 'O',
                    else:
                        print '#',
                else:
                    print '.',
            print ''
                    
        
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    part1 = Map(1362)
    print 'Shortest path to (31,39) was {} steps'.format(
        part1.getDepthByBFS((1,1), (31, 39)))
    #part1.dump(41, 41)

    part2 = Map(1362)
    part2.getDepthByBFS((1,1), (31, 39), maxdepth=50)
    visitcount = part2.visitcount()
    #part2.dump(41, 41)

    print '{} nodes were visited within 50 steps'.format(visitcount)

    

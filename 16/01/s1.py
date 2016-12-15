#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            Walker('R2, L3').followDocument().blocksFromStart(), 5)
    def test_2(self):
        self.assertEqual(
            Walker('R2, R2, R2').followDocument().blocksFromStart(), 2)
    def test_3(self):
        self.assertEqual(
            Walker('R5, L5, R5, R3').followDocument().blocksFromStart(), 12)
    def test_4(self):
        self.assertEqual(
            Walker('R8, R4, R4, R8').followDocument(part2=True).blocksFromStart(), 4)

with open('input.txt', 'r') as fd:
    input_data = fd.read()

class Walker(object):

    def __init__(self, document=None, origin=(0,0)):
        self.origin = origin
        if document is None:
            self.document = ''
        else:
            self.document = document
        self.x = 0
        self.y = 0
        self.dir = 0 # 0 = N, 1 = E etc.
        self.visited = []

    def __str__(self):
        return 'Walker at ({}, {}) facing {}'.format(self.x,
                                                     self.y,
                                                     'NEWS'[self.dir])

    __repr__ = __str__

    dirs = {'R': 1, 'L': -1}
    
    def move(self, instruction, part2):
        terminate = False
        direction = instruction[0]
        distance = int(instruction[1:])
        self.dir = (self.dir + Walker.dirs[direction]) % 4
        xf, yf = [(0, 1), (1, 0), (0, -1), (-1, 0)][self.dir]
        xn = self.x
        yn = self.y
        for i in range(distance):
            xn += xf
            yn += yf
            if part2:
                if (xn, yn) in self.visited:
                    terminate = True
                    break
                else:
                    self.visited.append((xn, yn))
        return (xn, yn, terminate)
    
    def followDocument(self, part2=False):
        for i in self.document.split(', '):
            x, y, finished = self.move(i, part2)
            self.x = x
            self.y = y
            #print 'moving {}, visited={}'.format(i, self.visited)
            if finished:
                #print 'terminating at ({}, {})'.format(self.x, self.y)
                break
        return self

    def blocksFromStart(self):
        # taxicab metric
        #print self
        return abs(self.x) + abs(self.y)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    walker1 = Walker(input_data)
    walker1.followDocument()
    print "Part 1: number of blocks ", walker1.blocksFromStart()
    walker2 = Walker(input_data)
    walker2.followDocument(part2=True)
    print "Part 2: number of blocks ", walker2.blocksFromStart()
    
    
    

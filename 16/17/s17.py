#!/usr/bin/env python2
import unittest
import argparse
from collections import deque
from hashlib import md5

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--part',
                    help='Part 1 or 2 (use part 0 to test)',
                    type=int)
parser.add_argument('-v', '--verbose',
                    help='produce verbose output',
                    action='store_true')
parser.add_argument('-c', '--code',
                    help='Easter bunny security passcode',
                    type=str)

args = parser.parse_args()

if args.part is None:
    part = 0
else:
    part = args.part

if args.code is None:
    PASSCODE = 'veumntbg'
else:
    PASSCODE = args.code

STARTCOORD = (0, 0)
STARTPOS = STARTCOORD + ('',) # (x, y, pathSoFar)
FINISHCOORD = (3, 3)
OPENCHARS = 'bcdef'

# Only the first four characters of the hash are used; they represent,
# respectively, the doors up, down, left, and right from your current
# position.
DIRECTIONS = ((0, -1), # U
              (0, 1),  # D
              (-1, 0), # L
              (1, 0))  # R
DIRECTIONNAMES = 'UDLR'

class TestIt(unittest.TestCase):
    def test_1(self):
        global PASSCODE
        PASSCODE = 'ihgpwlah'
        self.assertEqual(getPathByBFS(STARTPOS),
                         'DDRRRD')

    def test_2(self):
        global PASSCODE
        PASSCODE = 'kglvqrro'
        self.assertEqual(getPathByBFS(STARTPOS),
                         'DDUDRLRRUDRD')

    def test_3(self):
        global PASSCODE
        PASSCODE = 'ulqzkmiv'
        self.assertEqual(getPathByBFS(STARTPOS),
                         'DRURDRUDDLLDLUURRDULRLDUUDDDRR')

    def test_4(self):
        global PASSCODE
        PASSCODE = 'ihgpwlah'
        self.assertEqual(getPathByBFS(STARTPOS, getLongest=True),
                         370)

    def test_5(self):
        global PASSCODE
        PASSCODE = 'kglvqrro'
        self.assertEqual(getPathByBFS(STARTPOS, getLongest=True),
                         492)

    def test_6(self):
        global PASSCODE
        PASSCODE = 'ulqzkmiv'
        self.assertEqual(getPathByBFS(STARTPOS, getLongest=True),
                         830)

def getPathByBFS(start, getLongest=False):
    queue = deque()
    queue.append(start)

    longest = 0

    while queue:
        # Queue entries look like positionAndPath where
        # positionAndPath is (x, y, UDLRpath).
        # Although the UDLRpath implies the (x,y) coords, I store the
        # (x,y) anyway to make the edge and success tests quicker.

        x, y, path = queue.popleft()

        if isFinalPos(x, y):
            if not getLongest: # part 1
                return path
            longest = len(path) # BFS so each time is len >= last
            continue # no children at finalPos

        children = getChildren((x, y, path))
        
        if len(children):
            queue.extend(children)

    return longest

def isFinalPos(x, y):
    return (x, y) == FINISHCOORD

def inGrid(x, y):
    if x < 0 or x >= 4:
        return False
    if y < 0 or y >= 4:
        return False
    return True

def getChildren(coordsPath):
    posList = []
    x, y, path = coordsPath

    doorFlags = md5(PASSCODE + path).hexdigest()[:4]

    for i, c in enumerate(doorFlags):
        if c in OPENCHARS:
            nx, ny = map(sum, zip((x, y), DIRECTIONS[i]))
            if inGrid(nx, ny):
                posList.append((nx, ny,
                                path + DIRECTIONNAMES[i]))
    return posList

if __name__ == '__main__':
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif part == 1:
        print getPathByBFS(STARTPOS)
    elif part == 2:
        print getPathByBFS(STARTPOS, getLongest=True)
    else:
        print 'Part {} not implemented'.format(part)

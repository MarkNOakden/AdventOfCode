#!/usr/bin/env python2
import unittest
from collections import deque
from itertools import combinations
import argparse
import time

#
# optimised version created after solving the problem using my
# non-optimised s11.py version
#
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--part',
                    help='0 -> test, 1 -> Part 1, 2-> Part 2',
                    type=int)

args = parser.parse_args()

if args.part is None:
    part = 0
else:
    part = args.part

class TestIt(unittest.TestCase):
    def setUp(self):
        global pairs, names
        pairs = 2
        names = [' H', ' L']
        self.startpos = [1, # Elevator
                    1, # HM
                    1, # LM
                    2, # HG
                    3] # LG

    def test_1(self):
        self.assertEqual(getDepthByBFS(self.startpos), 11)

with open('input.txt', 'r') as fd:
    input_data = fd.read()

def getDepthByBFS(start):
    depth = 0
    queue = deque()
    queue.append((depth, start))
    visited = set(start)

    while queue:
        depth, node = queue.popleft()

        if isFinalPos(node):
            return depth

        for childpos in getChildren(node):
            if childpos not in visited:
                queue.append((depth + 1, childpos))
                visited.add(childpos)
                
    return None

def posHash(pos):
    return ','.join(str(i) for i in pos)

# I'm going to represent a state by a list
# element 0 is the floor that the elevator is on
# elements 1 to N are the floors that the chips are on
# elements N+1 to 2N are the floors that the RTGs are on

# [Elevator, chip1, chip2, ..., chipN, RTG1, RTG2, ..., RTGN]
#
# chips = pos[1:N+1]
# RTGs = pos[N+1:2N+1]

# Floors are numbered 1 to 4 as per the problem


def dump(pos):
    for floor in range(4, 0, -1):
        fstr = 'F{} '.format(floor)
        fstr += 'E   ' if pos[0] == floor else '.   '
        for i, name in enumerate(names):
            fstr += '{}  '.format(names[i] + 'G'
                                  if pos[pairs + i + 1] == floor
                                  else '...')
            fstr += '{}   '.format(names[i] + 'M'
                                  if pos[i + 1] == floor
                                  else '...')
        print fstr

def isFinalPos(pos):
    return all(i == 4 for i in pos)

def getChildren(pos):
    posList = []
    E = pos[0]
    
    for newFloor in [E + 1, E - 1]:
        if newFloor == 0 or newFloor == 5:
            continue
        itemsOnSourceFloor = [i + 1 for i, v in enumerate(pos[1:])
                              if v == E]
        #print itemsOnSourceFloor
        # create all candidate positions moving either one or two
        # items from itemsOnSourceFloor to floor newFloor
        # (one chip, two chips, one RTG, two RTGs, one matched chip+RTG)
        chips = [i for i in itemsOnSourceFloor if i < pairs + 1]
        RTGs = [i for i in itemsOnSourceFloor if i >= pairs + 1]
        # so we need all combinations(allChips, 1)
        for c in combinations(chips, 1):
            newpos = list(pos) # copy of the list
            newpos[0] = newFloor # move the elevator
            newpos[c[0]] = newFloor # move the chip
            if chipsSafe(newpos):
                posList.append(tuple(newpos))
        #                combinations(allChips, 2)
        for c in combinations(chips, 2):
            newpos = list(pos[:]) # copy of the list
            newpos[0] = newFloor # move the elevator
            newpos[c[0]] = newFloor # move the first chip
            newpos[c[1]] = newFloor # move the second chip
            if chipsSafe(newpos):
                posList.append(tuple(newpos))
        # so we need all combinations(allRTGs, 1)
        for c in combinations(RTGs, 1):
            newpos = list(pos[:]) # copy of the list
            newpos[0] = newFloor # move the elevator
            newpos[c[0]] = newFloor # move the RTG
            if chipsSafe(newpos):
                posList.append(tuple(newpos))
        #                combinations(allRTGs, 2)
        for c in combinations(RTGs, 2):
            newpos = list(pos[:]) # copy of the list
            newpos[0] = newFloor # move the elevator
            newpos[c[0]] = newFloor # move the first RTG
            newpos[c[1]] = newFloor # move the second RTG
            if chipsSafe(newpos):
                posList.append(tuple(newpos))
        #                plus each matched Chip,RTG pair
        # except that all matched pairs on this floor are equivalent
        # so lets just consider the first one (tip from the reddit
        # solutions thread)
        for c in [(x, x + pairs) for x in chips
                  if (x + pairs) in RTGs]:
            newpos = list(pos[:]) # copy of the list
            newpos[0] = newFloor # move the elevator
            newpos[c[0]] = newFloor # move the chip
            newpos[c[1]] = newFloor # move the RTG
            if chipsSafe(newpos):
                posList.append(tuple(newpos))
            break
           
        # if all 5 chips and 5 RTGs are on the floor, we have
        # 70 = (5 + 10 + 5 + 10 + 5) * 2 possibilities
        # compare with naive 1 or two choice from all 10:
        # 110  = (10 + 45) * 2
        # (assuming its not floor 1 or 4)
        # if one chip is missing
        # 46 = (4 + 0 + 5 + 10 + 4) * 2
        # if 3 chips and their matching RTGs
        # 30 = (3 + 3 + 3 + 3 + 3) * 2
        # if one chip and its RTG
        # 6 = (1 + 0 + 1 + 0 + 1) * 2
        # check if the candidate position
        #print posList
    return posList

def chipsSafe(pos):
    for chip in range(pairs):
        chipFloor = pos[chip + 1] # position of this chip
        RTGfloor = pos[chip + pairs + 1] # the corresponding RTG
        if RTGfloor != chipFloor:
            # chip not protected - if there are any other RTGs here
            # then return False - this chip will be fried
            if len([i for i in pos[pairs + 1:]
                   if i == chipFloor]) != 0:
                return False
    return True
   
if __name__ == '__main__':
    start = time.time()
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
        # chips/rtgs in order Po, Tm, Pm, Ru, Co
        pairs = 3
        names = (' H', 'He', ' L')
        startpos = (3, # Elevator
                    4, #  HM
                    4, # HeM
                    3, #  LM
                    2, #  HG
                    2, # HeG
                    3) #  LG
        dump(startpos)
        print getDepthByBFS(startpos)
    elif part == 1:
        # chips/rtgs in order Po, Tm, Pm, Ru, Co
        pairs = 5
        names = ('Po', 'Tm', 'Pm', 'Ru', 'Co')
        startpos = (1, # Elevator
                    2, # PoM
                    1, # TmM
                    2, # PmM
                    1, # RuM
                    1, # CoM
                    1, # PoG
                    1, # TmG
                    1, # PmG
                    1, # RuG
                    1) # CoG

        dump(startpos)
        print 'Part 1 number of steps is {}'.format(getDepthByBFS(startpos))
    elif part == 2:
        pairs = 7
        names = ('Po', 'Tm', 'Pm', 'Ru', 'Co', 'El', 'Dl')
        startpos = (1, # Elevator
                    2, # PoM
                    1, # TmM
                    2, # PmM
                    1, # RuM
                    1, # CoM
                    1, # ElM
                    1, # DlM
                    1, # PoG
                    1, # TmG
                    1, # PmG
                    1, # RuG
                    1, # CoG
                    1, # ElG
                    1) # DlG
        dump(startpos)
        print 'Part 2 number of steps is {}'.format(getDepthByBFS(startpos))
    else:
        print 'part {} not implemented'.format(part)
    
    end = time.time()
    print 'elapsed time {:.2f}'.format(end - start)

    

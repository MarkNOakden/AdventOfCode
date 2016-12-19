#!/usr/bin/env python2
import unittest
import argparse
from itertools import repeat
from math import floor, log


 
class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mkElfList(5), [(0, 1),
                                        (1, 1),
                                        (2, 1),
                                        (3, 1),
                                        (4, 1)])

    def test_2(self):
        self.assertEqual(doRound(mkElfList(5)),
                         [(0, 0),
                          (1, 0),
                          (2, 2),
                          (3, 0),
                          (4, 3)])

    def test_3(self):
        self.assertEqual(lastElf(mkElfList(5), doRound), 3)

    def test_4(self):
        self.assertEqual(lastElf(mkElfList(5), doRound2), 2)

def mkElfList(count):
    return list(zip(range(count), repeat(1, count)))

def doRound(elves):
    if args.verbose:
        print ''
        print elves
    count = len(elves)
    eligible = [e for e in elves if e[1]]
    for i, e in enumerate(elves):
        if e[1] == 0:
            # elf has no presents... skip
            continue
        j = (i + 1) % count
        while j != i:
            if elves[j][1] != 0:
                # take elf j's presents
                if args.verbose:
                    print ' elf {} takes elf {}\'s presents'.format(
                        i, j)
                elves[i] = (elves[i][0], elves[i][1] + elves[j][1])
                elves[j] = (elves[j][0], 0)
                if args.verbose:
                    print ':: ', elves
                break
            else:
                j += 1
                j = j % count
    if args.verbose:
        print '    result:', elves
    return elves

def doRound2(elves):
    if args.verbose:
        print ''
        print elves
    count = len(elves)
    halfway = count // 2 # explicit integer division
    nextElf = elves[halfway]
    elves[0] = (elves[0][0], elves[0][1] + nextElf[1])
    elves = elves[1:halfway] + elves[halfway+1:] + [elves[0]]
    if args.verbose:
        print '    result:', elves
    return elves

def lastElf(elves, roundfunc):
    r = 1
    while len([e for e in elves if e[1]]) != 1:
        elves = roundfunc(elves)
    return [e for e in elves if e[1]][0][0] + 1 # e[0][0] is the index
#
# based on the pattern of answers ...  answer for N a power of 3 is N
# answers for N-1, N-2 etc. reduce by 2 each time until the answer is
# the mid-point with the next lower power of 3 when they start to
# reduce by 1
# 
def algebraicLastElf(N):
    lowerExponent = int(floor(log(N)/log(3)))
    upperExponent = lowerExponent + 1

    lower = pow(3, lowerExponent)
    upper = pow(3, upperExponent)

    if N == lower:
        ans = N
    elif N <= lower * 2:
        ans = N - lower
    else:
        ans = upper - (upper - N) * 2

    #print 'N={}, lower={}, upper={}, ans={}'.format(N, lower,
    #                                                upper, ans)
    return int(ans)

#
# Added after initial solution:
#
# Optimising the brute force by implementing a circular
# linked list structure
#
# If we maintain a reference to the mid-point elf, then as we delete
# him, the new mid-point elf will be his .next, or the .next of that
# elf depending on whether there are an odd or even number of elves
# left
#
# e.g. (* is next elf to steal, + is the victim)
#
#   
#   1*
# 5   2
#  4 3+
#
# becomes
#
#   1
# 5+  2*
#   4
#
# (four elves left, so the new victim is the successor of the
# successor of the original victim).  This then becomes
#
#   1+
#     2
#   4*
#
# (next victim is successor of the previous one as three is odd)
#
# finally
#
#  2*
#
#  4+
#
# (two elves left so next victim is successor of the successor)

class Elf(object):
    def __init__(self, index):
        self.index = index
        self.next = None
        self.prev = None

    def delete(self):
        self.next.prev = self.prev
        self.prev.next = self.next

def mkElfListOpt(count):
    elves = map(Elf, xrange(count))
    for i in xrange(count):
        elves[i].next = elves[(i + 1) % count]
        elves[i].prev = elves[(i - 1) % count]
    return elves[0], elves[count // 2]

def lastElfOpt(count):
    remaining = count
    elf0, elfToKill = mkElfListOpt(count)
    nextElfToTake = elf0
    while remaining != 1:
        elfToKill.delete()
        elfToKill = elfToKill.next
        if remaining % 2 == 1:
            elfToKill = elfToKill.next
        remaining -= 1
        nextElfToTake = nextElfToTake.next
    return nextElfToTake.index + 1
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--part',
                        help='Part 1 or 2 (use part 0 to test)',
                        type=int)
    parser.add_argument('-e', '--elves',
                        help='Number of elves at the start',
                        type=int)
    parser.add_argument('-v', '--verbose',
                        help='produce verbose output',
                        action='store_true')
    parser.add_argument('-a', '--algebraic',
                        help='do part 2 algebraically',
                        action='store_true')
    parser.add_argument('-o', '--optimise',
                        help='do part 2 using brute force on optimised structure',
                        action='store_true')

    args = parser.parse_args()

    if args.part is None:
        part = 0
    else:
        part = args.part

    if args.elves is None:
        ELFCOUNT = 3014387
    else:
        ELFCOUNT = args.elves
    
    if part == 0:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif part == 1:
        print 'Part1: Elf {} has all the presents'.format(
            lastElf(mkElfList(ELFCOUNT), doRound))
    elif part == 2:
        if args.algebraic:
            print 'Part2: Elf {} has all the presents'.format(
                algebraicLastElf(ELFCOUNT))
        else:
            if args.optimise:
                print 'Part2: Elf {} has all the presents'.format(
                    lastElfOpt(ELFCOUNT))
            else:
                print 'This will take a looong time to return for large counts'
                print 'Part2: Elf {} has all the presents'.format(
                    lastElf(mkElfList(ELFCOUNT), doRound2))
    else:
        print 'Part {} not implemented'.format(part)

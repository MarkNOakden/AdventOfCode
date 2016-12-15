#!/usr/bin/env python2
import unittest
from exceptions import KeyError

dist_test={}
dist_test['London to Dublin'] = 464
dist_test['London to Belfast'] = 518
dist_test['Dublin to Belfast'] = 141

locs_test = ['London', 'Dublin', 'Belfast']

class TestIt(unittest.TestCase):
    # Part 1 tests
        
    def test_1(self):
        self.assertEqual(dist('London', 'Dublin'), 464)
 
    def test_2(self):
        self.assertEqual(dist('Dublin', 'London'), 464)

    def test_3(self):
        self.assertEqual(shortestPath(locs_test)[0], 605)

    def test_4(self):
        self.assertEqual(longestPath(locs_test)[0], 982)
 
        

# test input
#fd = open("test.txt", 'r')
#test_data = fd.read()
#fd.close()

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

dist_day9 = {}
locs_day9 = []
for l in input_data.splitlines():
    key, sep, dist_str = l.partition(' = ')
    dist_day9[key] = int(dist_str)
    l, sep, r = key.partition(' to ')
    if l not in locs_day9:
        locs_day9.append(l)
    if r not in locs_day9:
        locs_day9.append(r)

print locs_day9

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

def pathLen(path):
    d = 0
    for i in range(len(path) - 1):
        d += dist(path[i], path[i+1])
    return d

def shortestPath(locs):
    s = None
    for p in all_perms(locs):
        d = pathLen(p)
        if s is None or d < s:
            s = d
            sp = p
    return s, sp

def longestPath(locs):
    s = None
    for p in all_perms(locs):
        d = pathLen(p)
        if s is None or d > s:
            s = d
            sp = p
    return s, sp
    
def dist(A, B):
    try:
        d=dist_table[A + ' to ' + B]
    except KeyError:
        d = dist_table[B + ' to ' + A]
    return d


if __name__ == '__main__':
    dist_table  = dist_test
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    dist_table = dist_day9
    sd, path =  shortestPath(locs_day9)
    print 'Part1 - shortest dist: ' + str(sd)
    print 'Path: ', path
    sd, path =  longestPath(locs_day9)
    print 'Part2 - longest dist: ' + str(sd)
    print 'Path: ', path
    
    
    


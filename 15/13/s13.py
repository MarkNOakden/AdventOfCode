#!/usr/bin/env python2
import unittest
from exceptions import KeyError

#mode = 'test'
mode = 'prod'

class TestIt(unittest.TestCase):
    # Part 1 tests
        
    def test_1(self):
        self.assertEqual(hap_table['Alice,Bob'], 54)
 
    def test_2(self):
        self.assertEqual(hap_table['Alice,Carol'], -79)
 
    def test_3(self):
        self.assertEqual(hap_table['Carol,Alice'], -62)

    def test_4(self):
        self.assertEqual(happiest(ppl)[0], 330)
 

    # def test_2(self):
    #     self.assertEqual(dist('Dublin', 'London'), 464)

    # def test_3(self):
    #     self.assertEqual(shortestPath(locs_test)[0], 605)

    # def test_4(self):
    #     self.assertEqual(longestPath(locs_test)[0], 982)
 
        

# test/prod input
if mode == 'test':
    fd = open("test.txt", 'r')
else:
    fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

hap_table = {}
ppl = []
for l in input_data.splitlines():
    l = l.replace('lose ', 'gain -')
    l = l.replace('.', '')
    p1, sep, rest = l.partition(' would gain ')
    rest = rest.split()
    hap, p2 = rest[0], rest[-1]
    #print p1, hap, p2
    hap_table[p1+','+p2] = int(hap)
    if p1 not in ppl:
        ppl.append(p1)

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

def hapScore(seats):
    d = 0
    for i in range(len(seats) - 1):
        d += hap_table[seats[i]+','+seats[i+1]]
        d += hap_table[seats[i+1]+','+seats[i]]
    #table is circular
    d += hap_table[seats[0]+','+seats[-1]]
    d += hap_table[seats[-1]+','+seats[0]]
    
    return d

def happiest(ppl):
    besth = None
    for p in all_perms(ppl):
        h = hapScore(p)
        if besth is None or h > besth:
            besth = h
            bestppl = p
    return besth, bestppl

if __name__ == '__main__':
    if mode == 'test':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        print 'for people:', ppl
        hap, seating = happiest(ppl)
        print 'max happiness change is', hap
        print 'seating arrangement is', seating
        print 'Part 2'
        for i in ppl:
            hap_table[i+',Oaky'] = 0
            hap_table['Oaky,'+i] = 0
        ppl.append('Oaky')
        print 'for people:', ppl
        hap, seating = happiest(ppl)
        print 'max happiness change is', hap
        print 'seating arrangement is', seating
        
        
        
    
    


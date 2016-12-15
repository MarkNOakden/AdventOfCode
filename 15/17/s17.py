#!/usr/bin/env python2
import unittest

# class TestIt(unittest.TestCase):
#     # Part 1 tests
        
#     def test_1(self):
#         self.assertEqual(dist('London', 'Dublin'), 464)
 
#     def test_2(self):
#         self.assertEqual(dist('Dublin', 'London'), 464)

#     def test_3(self):
#         self.assertEqual(shortestPath(locs_test)[0], 605)

#     def test_4(self):
#         self.assertEqual(longestPath(locs_test)[0], 982)

test_data =  [ 20, 15, 10, 5, 5 ]
test_data.sort()
test_total = 25


input_data = [ 43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, \
               17, 44, 36, 31, 46, 9, 27, 38 ]
input_data.sort()

total = 150

def isok(l, total):
    return sum(l) == total

def masked(l, mask):
    return [x for (x, y) in zip(l, mask) if y == '1']

def combination(l, total):
    i = 1
    bits = len(l)
    fmt = '{:0>'+str(bits)+'b}'
    while i < 2**bits:
        mask = fmt.format(i)
        if isok(masked(l, mask),total):
            yield masked(l, mask)
        i += 1
        

if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    #unittest.TextTestRunner(verbosity=2).run(suite)

    combs = []
    for comb in combination(input_data, total):
        combs.append(comb)
    print 'part 1', len(combs)
    smallest = min(map(len, combs))
    print 'part 2 smallest number was', smallest
    print len([x for x in combs if len(x)==smallest]), 'ways'

    
    


#!/usr/bin/env python2
import unittest
import json
from exceptions import TypeError, AttributeError

import re
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
 
        

# test input
#fd = open("test.txt", 'r')
#test_data = fd.read()
#fd.close()

# get the input
fd = open("input.txt", 'r')
raw_input_data = fd.read()
fd.close()

input_data = json.loads(raw_input_data)

def summing_walk(jsondata, part, depth):
    #print '>'*depth
    total = 0
    # is it a dict (object)?
    try:
        keys = jsondata.keys()
        # process values here to look for red
        process_this_one = True
        if part == 2:
            for i in keys:
                if jsondata[i] == 'red':
                    process_this_one = False
        if process_this_one:
            for i in keys:
                total += summing_walk(jsondata[i], part, depth + 1)
    except AttributeError:
        # OK this wasn't a dict
        # is it a list?
        try:
            jsondata.append('MNO')
            jsondata.pop() # remove it again if we succeeded
            # process list
            for i in jsondata:
                total += summing_walk(i, part, depth + 1)
        except AttributeError:
            # not a list either - must be string (ignore)
            # or int (add to total)
            try:
                total += jsondata
            except TypeError:
                # it was a string
                pass
    return total

# total cheat for part 1:-
numRE = re.compile(r'[-]?[1-9][0-9]*')
def sum_by_re(data):
    return sum(map(int, numRE.findall(data)))

if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    print 'total is ', sum_by_re(raw_input_data)
    for i in (1, 2):
        print 'part ' + str(i) + ': ' + \
          str(summing_walk(input_data, i, 0))
    
    
    
    


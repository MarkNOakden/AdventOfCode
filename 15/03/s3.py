#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(nhouses('>'), 2)
    def test_2(self):
        self.assertEqual(nhouses('^>v<'), 4)
    def test_3(self):
        self.assertEqual(nhouses('^v^v^v^v^v'), 2)
    def test_4(self):
        self.assertEqual(nhouses2('^v'), 3)
    def test_5(self):
        self.assertEqual(nhouses2('^>v<'), 3)
    def test_6(self):
        self.assertEqual(nhouses2('^v^v^v^v^v'), 11)
        
moves = { "^": (0, 1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()

fd.close()

# will use x, y coords, with starting point (0, 0)
# store present count in a dict, with key 'x,y'
def mkkey(x, y):
    return str(x)+','+str(y)

def incr(d, key):
    if d.has_key(key):
        d[key] += 1
    else:
        d[key] = 1

        
def houses(instructions):
    x = y = 0
    h = dict()

    # initial house
    incr(h, mkkey(x, y))

    # elf-instructions
    for i in instructions:
        dx, dy = moves[i]
        x += dx
        y += dy
        incr(h, mkkey(x, y))
        
    return h

def houses2(instructions):
    x = [0, 0]
    y = [0, 0]
    j = 0 # will be 0 fro Santa, 1 for RoboSanta
    h = dict()

    #initial house
    for j in [0, 1]:
        incr(h, mkkey(x[j], y[j]))

    j = 0 # Santa goes first
    for i in instructions:
        dx, dy = moves[i]
        x[j] += dx
        y[j] += dy
        incr(h, mkkey(x[j], y[j]))
        j = 1 - j
        
    return h
    

def nhouses(instructions):
    return len(houses(instructions))

def nhouses2(instructions):
    return len(houses2(instructions))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print "Part 1: number of houses with at least one present is ", \
        nhouses(input_data)
    print "Part 2: number of houses with at least one present is ", \
        nhouses2(input_data)
    
    

#!/usr/bin/env python2
import unittest
from exceptions import KeyError

import re
class TestIt(unittest.TestCase):
    # Part 1 tests
    def setUp(self):
        subs = [ ('H', 'HO'), ('H', 'OH'), ('O', 'HH') ]
        inMol = 'HOH'
        self.machine = Maker(subs, inMol)
        print self.machine.allMols()

    def tearDown(self):
        del self.machine
        
    def test_1(self):
        self.assertTrue('HOOH' in self.machine.allMols())
 
    def test_2(self):
        self.assertTrue('HOHO' in self.machine.allMols())

    def test_3(self):
        self.assertTrue('OHOH' in self.machine.allMols())

    def test_4(self):
        self.assertTrue('HHHH' in self.machine.allMols())
 
        
class Maker(object):

    def __init__(self, ops, mol):
        self.ops = ops
        self.mol = mol

    def sub(self, atomIn, atomOut):
        rest = self.mol
        front = ''
        while rest != '':
            head, sep, rest = rest.partition(atomIn)
            if sep != '':
                front += head
                yield front + atomOut + rest
                front += sep

    def allMols(self):
        molDict = {}
        for atomIn, atomOut in self.ops:
            for mol in self.sub(atomIn, atomOut):
                try:
                    molDict[mol] += 1
                except KeyError:
                    molDict[mol] = 1
        return molDict
            
    def setMol(self, mol):
        self.mol = mol
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # get the input
    fd = open("input.txt", 'r')
    input_data = fd.read()
    fd.close()

    subs = []
    for l in input_data.splitlines():
        atomIn, sep, atomOut = l.partition(' => ')
        if sep == '':
            if atomIn != '':
                mol = atomIn
        else:
            subs.append((atomIn, atomOut))

    machine = Maker(subs, mol)

    outputs  = machine.allMols()
    print len(outputs), 'distinct molecules'


    backsubs = []
    for a, b in subs:
        if a != 'e':
            backsubs.append((b,a))
        
    pt2machine = Maker(backsubs, mol)

    steps = 2 # start at two because we are testing for
              # stuff one step away from e

    outputs = pt2machine.allMols().keys()

    def finished(outputs):
        for mol in ['HF', 'NAl', 'OMg']:
            if mol in outputs:
                return True
        return False

    while not finished(outputs):
        new = []
        for m in outputs:
            pt2machine.setMol(m)
            new += [x for x in pt2machine.allMols().keys() \
                    if x not in new]
        outputs = new
        steps += 1


    print "got desired molecule in", steps, "steps"
    
    


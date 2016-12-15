#!/usr/bin/env python2
import unittest
from exceptions import IndexError

debug = True

def dprint(msg):
    if debug:
        print msg

class TestIt(unittest.TestCase):
    # Part 1 tests
    testCircuit = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''
    def setUp(self):
        self.c = Circuit()
        self.c.fromInput(TestIt.testCircuit)

    def tearDown(self):
        del self.c
        
    def test_1(self):
        self.assertEqual(self.c.nodeValue('d', 0), '72')
        
    def test_2(self):
        self.assertEqual(self.c.nodeValue('e', 0), '507')
        
    def test_3(self):
        self.assertEqual(self.c.nodeValue('f', 0), '492')
        
    def test_4(self):
        self.assertEqual(self.c.nodeValue('g', 0), '114')
        
    def test_5(self):
        self.assertEqual(self.c.nodeValue('h', 0), '65412')
        
    def test_6(self):
        self.assertEqual(self.c.nodeValue('i', 0), '65079')
        
    def test_7(self):
        self.assertEqual(self.c.nodeValue('x', 0), '123')
        
    def test_8(self):
        self.assertEqual(self.c.nodeValue('y', 0), '456')

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

fd = open("input2.txt", 'r')
input_data2 = fd.read()
fd.close()

# symbolic 'constants'
AND, OR, NOT, LSHIFT, RSHIFT = 'AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT'

operations = {'AND': AND, \
              'OR': OR, \
              'NOT': NOT, \
              'LSHIFT': LSHIFT, \
              'RSHIFT': RSHIFT}



class Gate(object):

    # Will use inputs as list of input node names
    # op will be AND, OR, LSHIFT, RSHIFT, NOT for the
    # provided BITWISE operations and None for a
    # provided value
    #
    # 123 -> x:
    #     inputs = [None, '123']
    #     op = None
    #
    # x AND y -> z:
    #     inputs = ['x', 'y']
    #     op = AND
    #
    # p LSHIFT 2 -> q:
    #     inputs = ['p', 2]
    #     op = LSHIFT
    #
    # NOT e -> f:
    #     inputs = [None, 'e']
    #     op = NOT

    def __init__(self, inputs = None, op = None):
        self.inputs = inputs
        self.op = op
        self.val = None
       
class Circuit(object):

    def __init__(self):
        self.nodes = {}

    def addNode(self, spec):
        dprint("addNode('" + spec + "')")
        rest, sep, name = spec.partition(' -> ')
        
        if name in self.nodes:
            # barf with enough information
            print "tried to create duplicate node:", name
            print "existing node: ", self.nodes[name]
            print "spec was: ", spec
            exit()
        if not name.islower():
            print "found a non-lowercase name: '" + name + "'"
            exit()

        rl = rest.split()

        #
        try:
            if rl[0].isupper():
                # first word is a command, so this was a NOT
                inputs = [None, rl[1]] # no first input
                op = NOT
            elif len(rl) == 1:
                # supplied value NNN -> name
                inputs = [None, rl[0]]
                op = None
            else:
                inputs = [rl[0], rl[2]]
                #op = operations[rl[1]]
                op = rl[1]
        except IndexError:
            print "Index error when parsing '" + spec + "'"
            raise

        dprint(" --> " + name + " :- inputs: " + str(inputs) + " op: " + str(op))
        self.nodes[name] = Gate(inputs, op)

    def fromInput(self, input_data):
        for spec in input_data.splitlines():
            self.addNode(spec)

    def nodeValue(self, name, cn):
        dprint(" "*cn + "nodeValue('" + name + "')")
        if name.isdigit():
            dprint(" "*cn + "## " + name)
            #gate.val = name
            return name
        gate = self.nodes[name]
        if gate.val is not None:
            dprint(" "*cn + "** Cache HIT !! **")
            return gate.val
        l, r = gate.inputs
        if gate.op is None:
            if r.isdigit():
                dprint(" "*cn + "numeric " + r)
                gate.val = r
                return r
            else:
                return self.nodeValue(r, cn + 1)
        elif gate.op == NOT:
            dprint(" "*cn + "NOT")
            x = str(65535 ^ int(self.nodeValue(r, cn + 1)))
        elif gate.op == AND:
            dprint(" "*cn + "AND")
            x = str(int(self.nodeValue(l, cn + 1)) \
                & int(self.nodeValue(r, cn + 1)))
        elif gate.op == OR:
            dprint(" "*cn + "OR")
            x = str(int(self.nodeValue(l, cn + 1)) \
                | int(self.nodeValue(r, cn + 1)))
        elif gate.op == LSHIFT:
            dprint(" "*cn + "LSHIFT " + r)
            x =  str(int(self.nodeValue(l, cn + 1)) \
                << int(r))
        elif gate.op == RSHIFT:
            dprint(" "*cn + "RSHIFT " + r)
            x = str(int(self.nodeValue(l, cn + 1)) \
                >> int(r))
        else:
            print "unhandled operator: ", gate.op
            exit()
        dprint(" "*cn + "--> " + x)
        gate.val = x
        return x


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print '====================================================='
    s7part1 = Circuit()
    s7part1.fromInput(input_data)
    print "part 1 " + s7part1.nodeValue('a', 0)
    s7part2 = Circuit()
    s7part2.fromInput(input_data2)
    print "part 2 " + s7part2.nodeValue('a', 0)
    #print "part 1 - a gets signal:", s7part1.nodeValue('a')
    
    
    

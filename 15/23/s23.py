#!/usr/bin/env python2
import unittest
from exceptions import TypeError, AttributeError

class TestIt(unittest.TestCase):
    # Part 1 tests
    def setUp(self):
        self.VM = VM()
        self.VM.load(test_data)

    def tearDown(self):
        del self.VM
        
    def test_1(self):
        self.assertEqual(self.VM.run().get('a'), 2)
 
#     def test_2(self):
#         self.assertEqual(dist('Dublin', 'London'), 464)

#     def test_3(self):
#         self.assertEqual(shortestPath(locs_test)[0], 605)

#     def test_4(self):
#         self.assertEqual(longestPath(locs_test)[0], 982)
 
        

test_data = '''inc a
jio a, +2
tpl a
inc a
'''

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

class VM(object):

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        self.pc = 0 # Program counter
        self.prog = []

    def load(self, progStr):
        self.prog = progStr.splitlines()
        return self

    def step(self):
        if self.pc < 0 or self.pc >= len(self.prog):
            self.terminate()
            return False # terminated
        # process instruction here
        instr = self.prog[self.pc]
        #jmp offset
        #jio x, offset
        #jie x, offset
        #inc x
        #tpl x
        #hlf x
        instr, dummy, offset = instr.partition(', ')
        cmd, dummy, op = instr.partition(' ')
        if offset != '':
            # jio/jie instruction
            if cmd == 'jio':
                # JIO
                # Jump if ONE
                if self.get(op) == 1:
                    self.pc += int(offset)
                else:
                    self.pc +=1
            else:
                # JIE
                # Jump if EVEN
                if self.is_even(op):
                    self.pc += int(offset)
                else:
                    self.pc +=1
        else:
            if cmd =='jmp':
                # JMP
                self.pc += int(op)
            else:
                # all other instructions are class methods
                VM.__dict__[cmd](self, op)
                self.pc += 1
        return True

    def is_even(self, reg):
        return self.__dict__[reg] %2 == 0

    def is_odd(self, reg):
        return not self.is_even(reg)
    
    def get(self, reg):
        return self.__dict__[reg]

    def inc(self, reg):
        self.__dict__[reg] += 1

    def tpl(self, reg):
        self.__dict__[reg] *= 3

    def hlf(self, reg):
        self.__dict__[reg] /= 2

    def run(self):
        running = True
        while running:
            running = self.step()
        return self
    
    def terminate(self):
        print 'Program terminated:'
        self.dump()
        return

    def dump(self):
        print str(self)
        return

    def __str__(self):
        s = 'VM pc=' +  str(self.pc) + ' a=' + str(self.a) + ' b=' + str(self.b)
        return s
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    vm = VM()
    vm.load(input_data)
    vm.run()

    print '#'*72

    del vm
    vm = VM(a=1)
    vm.load(input_data)
    vm.run()
    
    
    


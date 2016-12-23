#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    # Part 1 tests
    def setUp(self):
        self.VM = VM()
        self.VM.load(test_data)

    def tearDown(self):
        del self.VM
        
    def test_1(self):
        self.assertEqual(self.VM.run().get('a'), 3)

test_data = '''cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
'''

with open('input.txt', 'r') as fd:
    input_data = fd.read()

class VM(object):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.PC = 0
        self.steps = 0 # step count
        self.prog = []
    
    def load(self, progStr):
        self.prog = [l.split() for l in progStr.splitlines()]
        return self

    def get(self, reg):
        return self.__dict__[reg]

    def step(self):
        line = self.prog[self.PC]
        instr = '_' + line[0]
        args = line[1:]
        # use the class __dict__ to invoke the methods...
        VM.__dict__[instr](self, *args)
        return self

    def run(self):
        while self.PC >= 0 and self.PC < len(self.prog):
            self.step()
        return self

    def debug(self):
        while self.PC >= 0 and self.PC < len(self.prog):
            for i, l in enumerate(self.prog):
                s = '--> ' if i == self.PC else '    '
                s += ' '.join(l)
                print s
            print ''
            print 'Registers: a: {} b: {} c: {} d: {}'.format(self.a,
                                                              self.b,
                                                              self.c,
                                                              self.d)
            print '\n%',
            a = raw_input()
            self.step()
        
                

    def value(self, regOrInt):
        return (self.__dict__[regOrInt]
                if regOrInt in 'abcd'
                else int(regOrInt))
        
    # instructions
    def _inc(self, reg):
        if reg in 'abcd':
            self.__dict__[reg] += 1
        self.PC += 1

    def _dec(self, reg):
        if reg in 'abcd':
            self.__dict__[reg] -= 1
        self.PC += 1

    def _cpy(self, regOrInt, reg):
        if reg in 'abcd':
            self.__dict__[reg] = self.value(regOrInt)
        self.PC += 1

    def _jnz(self, reg, offset):
        if self.value(reg) != 0:
            self.PC += int(self.value(offset))
        else:
            self.PC += 1

    tglTable = {'inc': 'dec',
                'dec': 'inc',
                'tgl': 'inc',
                'jnz': 'cpy',
                'cpy': 'jnz'}
        
    def _tgl(self, regOrInt):
        addr = self.PC + self.value(regOrInt)
        if addr < len(self.prog):
            self.prog[addr][0] = VM.tglTable[self.prog[addr][0]]
        self.PC += 1
        
    def __str__(self):
        s = 'VM() PC={}, a={}, b={}, c={}, d={}'.format(self.PC,
                                                        self.a,
                                                        self.b,
                                                        self.c,
                                                        self.d)
        return s

    __repr__ = __str__

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    part1VM = VM()
    part1VM.a = 7
    part1VM.load(input_data).run()
    print 'Part 1: register a is {}'.format(part1VM.get('a'))

    part2VM = VM()
    part2VM.a = 12
    part2VM.load(input_data).run()
    print 'register a is {}'.format(part2VM.get('a'))

    
    

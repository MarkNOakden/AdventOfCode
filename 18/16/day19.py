import re

INSTRS = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

instRE = re.compile(r'([a-z]{4}) (\d+) (\d+) (\d+)')
directiveRE = re.compile(r'#ip (\d+)')

class VMExecutionStop(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self,*args,**kwargs)

class VM(object):
    
    def __init__(self, prog, nregisters=6, debug=False):
        self.prog = prog[:] # list of strings
        self.ip = 0 # instruction pointer
        self.nregisters = nregisters
        self.registers = [0] * nregisters
        self.debug = debug
        self.ip_register = None
        self.steps = 0
        self._run_preprocessor()
        
    # == CORE ROUTINES =============================================================================
    
    def parse(self, line):
        '''Splits program line into instruction name and arguments, converting the args to int()'''
        match = re.search(instRE, line)
        if match:
            instr, *args = match.groups()
            args = list(map(int, args))
        else:
            raise ValueError(f'Malformed program line: \'{line}\'')
        return instr, args
    
    def dispatch(self, instr, A, B, C):
        '''Runs the appropriate method function with the arguments A, B, C'''
        if instr not in INSTRS:
            raise RuntimeError(f'No such instruction {instr}')
        VM.__dict__[instr](self, A, B, C)
        
    def step(self):
        '''Executes the instruction at the instruction pointer, ip, maintain the instruction pointer and any defined #ip register'''
        # test for program completion
        if self.ip < 0 or self.ip >= len(self.prog):
            raise VMExecutionStop(f'Finished execution of program at address {self.ip} after {self.steps} steps. Registers are {self.registers}.')
            
        # When the instruction pointer is bound to a register, its value is written to that register just before each instruction is executed
        if self.ip_register is not None:
            self.registers[self.ip_register] = self.ip
        
        # Parse and dispatch
        line = self.prog[self.ip]
        instr, (A, B, C) = self.parse(line)
        self.dispatch(instr, A, B, C)
        
        # the value of that register is written back to the instruction pointer immediately after each instruction finishes execution
        if self.ip_register is not None:
            self.ip = self.registers[self.ip_register]
        # 
        self.steps += 1
        self.ip += 1
        
        
    def run(self):
        '''Runs the program until completion'''
        while True:
            try:
                self.step()
            except VMExecutionStop as e:
                print(e)
                return self.registers[0]
        
    # == UTILITIES =================================================================================
    
    def _run_preprocessor(self):
        processed = []
        for line in self.prog:
            directive_match = re.search(directiveRE, line)
            if directive_match:
                self.ip_register = int(directive_match.groups()[0])
            else:
                processed.append(line)
        self.prog = processed
    
    def _set_registers(self, l):
        if len(l) != self.nregisters:
            raise ValueError(f'Wrong number of register values provided - got {len(l)}, should be {self.nregisters}')
        self.registers = l[:]
    
    # == INTROSPECTION =============================================================================
    
    def __str__(self):
        out = f'VM: IP={self.ip}'
        if self.ip < 0 or self.ip >= len(self.prog):
            out += ' HALTED'
        else:
            out += f' Current Instr: {self.prog[self.ip]}'
        out += f'\nIP Register: {repr(self.ip_register)}'
        out += f'\nRegister values: {self.registers}'
        return out
        
    __repr__ = __str__
    
    def dump(self):
        print(str(self))
    
    # == INSTRUCTIONS ==============================================================================
    
    # Addition:
   
    def addr(self, A, B, C):
        # addr (add register) stores into register C the result of adding register A and register B.
        self.registers[C] = self.registers[A] + self.registers[B]
          
    def addi(self, A, B, C):
        # addi (add immediate) stores into register C the result of adding register A and value B.
        self.registers[C] = self.registers[A] + B

    # Multiplication:
        
    def mulr(self, A, B, C):
        # mulr (multiply register) stores into register C the result of multiplying register A and register B.
        self.registers[C] = self.registers[A] * self.registers[B]
        
    def muli(self, A, B, C):
        # muli (multiply immediate) stores into register C the result of multiplying register A and value B.
        self.registers[C] = self.registers[A] * B

    # Bitwise AND:
        
    def banr(self, A, B, C):
        # banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
        self.registers[C] = self.registers[A] & self.registers[B]
        
    def bani(self, A, B, C):
        # bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
        self.registers[C] = self.registers[A] & B
        
    # Bitwise OR:
    
    def borr(self, A, B, C):
        # borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
        self.registers[C] = self.registers[A] | self.registers[B]
        
    def bori(self, A, B, C):
        # bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
        self.registers[C] = self.registers[A] | B

    # Assignment:

    def setr(self, A, B, C):
        # setr (set register) copies the contents of register A into register C. (Input B is ignored.)
        self.registers[C] = self.registers[A]
    
    def seti(self, A, B, C):
        # seti (set immediate) stores value A into register C. (Input B is ignored.)
        self.registers[C] = A
        
    # Greater-than testing:

    def gtir(self, A, B, C):
        # gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
        self.registers[C] = 1 if A > self.registers[B] else 0
        
    def gtri(self, A, B, C):
        # gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
        self.registers[C] = 1 if self.registers[A] > B else 0
        
    def gtrr(self, A, B, C):
        # gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
        self.registers[C] = 1 if self.registers[A] > self.registers[B] else 0
        
    # Equality testing:

    def eqir(self, A, B, C):
        # eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
        self.registers[C] = 1 if A == self.registers[B] else 0
        
    def eqri(self, A, B, C):
        # eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
        self.registers[C] = 1 if self.registers[A] == B else 0
        
    def eqrr(self, A, B, C):
        # eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
        self.registers[C] = 1 if self.registers[A] == self.registers[B] else 0

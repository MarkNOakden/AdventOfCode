from day19 import *
from colorama import Fore, Back, Style, init

INSTR_COLORS = {'addr': Fore.RED,
                'addi': Fore.RED,
                'mulr': Fore.GREEN,
                'muli': Fore.GREEN,
                'banr': Fore.MAGENTA,
                'bani': Fore.MAGENTA,
                'borr': Fore.MAGENTA,
                'bori': Fore.MAGENTA,
                'setr': Fore.WHITE,
                'seti': Fore.WHITE,
                'gtir': Fore.YELLOW,
                'gtri': Fore.YELLOW,
                'gtrr': Fore.YELLOW,
                'eqir': Fore.YELLOW,
                'eqri': Fore.YELLOW,
                'eqrr': Fore.YELLOW,
                'jmpabsr': Fore.CYAN,
                'jmprelr': Fore.CYAN,
                'jmpabsi': Fore.CYAN,
                'jmpreli': Fore.CYAN}
RST = Style.RESET_ALL

class Debug(VM):

    def __init__(self, prog, nregisters=6):
        VM.__init__(self, prog, debug=False)
        self.instr_display_mode = 'orig' # 'orig' or 'jmp'
        self.breakpoints = []

    def init_display(self, parameter_list):
        pass

    def toggle_instr_display(self):
        if self.instr_display_mode == 'orig':
            self.instr_display_mode = 'jmp'
        else:
            self.instr_display_mode = 'orig'
        return self

    def listing(self):
        display_status = Fore.CYAN + 'Registers: ' + ',  '.join(f'r{i}: {v:>8}' for i, v in enumerate(self.registers))
        display_status += f'\nInstructions: {self.steps}  IP: {self.ip}  ipr: {self.ip_register}' + RST
        print(display_status)
        print()
        addrwidth = len(str(len(self.prog)))
        for addr, line in enumerate(self.prog):
            display_line = self.prepare_for_display(line)
            display_addr = Fore.BLUE + f'{addr:>{addrwidth}}:' + RST
            display_ptr = '=>' if addr == self.ip else '  '
            display_brk = Fore.RED + '*' if addr in self.breakpoints else ' '
            print(f' {display_ptr} {display_brk} {display_addr} {display_line}')
        print()

    def prepare_for_display(self, line):
        l = line.split(' ')
        if self.instr_display_mode == 'jmp':
            if l[-1] == '4':
                if l[0] == 'seti':
                    l[0] = 'jmpabsi'
                elif l[0] == 'setr':
                    l[0] = 'jmpabsr'
                elif l[0] == 'addi':
                    l[0] = 'jmpreli'
                elif l[0] == 'addr':
                    l[0] = 'jmprelr'
        col = INSTR_COLORS[l[0]]
        l[0] = col + Style.BRIGHT + l[0] + RST
        line = ' '.join(l)
        return line

    def run_until_breakpoint(self):
        '''Runs the program until completion'''
        while True:
            try:
                if self.ip in self.breakpoints:
                    return self.registers[0]
                else:
                    try:
                        self.step()
                    except KeyboardInterrupt:
                        return self.registers[0] # back to debugger prompt
            except VMExecutionStop as e:
                print(e)
                return self.registers[0]

    def repl(self):
        while True:
            self.listing()
            cmd = input('ElfCode> ')
            if len(cmd) == 0:
                continue
            if cmd == 'q':
                self.quit()
            if cmd == 'l':
                self.listing()
            elif cmd == 's':
                self.step()
            elif cmd == 'r':
                self.step() # otherwise we get stuck at breakpoints forever
                self.run_until_breakpoint()
            elif cmd == 't':
                self.toggle_instr_display()
            elif cmd[0] == 'p':
                try:
                    val = int(cmd[1:])
                    self.registers[0] = val
                except ValueError:
                    print(f'OOPS! \'{cmd[1:]}\' is not a valid value!')
            elif cmd[0] == 'b':
                try:
                    addr = int(cmd[1:])
                    if addr >= 0 and addr < len(self.prog):
                        if addr not in self.breakpoints:
                            self.breakpoints.append(addr)
                except ValueError:
                    print(f'OOPS! \'{cmd[1:]}\' is not a valid value!')
            elif cmd[0] == 'u':
                try:
                    addr = int(cmd[1:])
                    if addr >= 0 and addr < len(self.prog):
                        if addr in self.breakpoints:
                            self.breakpoints.remove(addr)
                except ValueError:
                    print(f'OOPS! \'{cmd[1:]}\' is not a valid value!')


    def quit(self):
        print('Bye')
        exit()

if __name__ == '__main__':
    init() # colorama
    prog = open('input.txt').read().splitlines()
    dbg = Debug(prog)
    #dbg.listing()
    dbg.repl()
from elfcodedbg import *
import sys

# Takes too long to run - see the Jupyter notebook for solution via translation to Python

prog = open('input.txt').read().splitlines()

dbg = Debug(prog)

dbg.breakpoints.append(28)

seen = set()
last = None
part1 = True

while True:
    dbg.run_until_breakpoint()
    r1 = dbg.registers[1]
    #print(r1, dbg.steps)
    if part1:
        print(f'Part 1 answer: {r1}')
        part1 = False
    if r1 in seen:
        print(f'Part 2 answer: {last}')
        break
    if len(seen) % 100 == 0:
        print('#', end='')
        sys.stdout.flush()
    seen.add(r1)
    last = r1
    dbg.step()

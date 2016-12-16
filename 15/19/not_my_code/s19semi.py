#!/usr/bin/env python
import re
import random
fd = open("input.txt", 'r')
input = fd.read()
fd.close()

molecule = input.split('\n')[-2][::-1]

#print(molecule)
reps = {m[1][::-1]: m[0][::-1] 
        for m in re.findall(r'(\w+) => (\w+)', input)}
def rep(x):
    return reps[x.group()]

foo = [x for x in reps.keys()]
random.shuffle(foo)
count = 0
oldmolecule = ''

while molecule != 'e':
    molecule = re.sub('|'.join(foo), rep, molecule, 1)
    count += 1
    if molecule == oldmolecule:
        print('stuck at: '+molecule)
        break
    oldmolecule = molecule

print(count)

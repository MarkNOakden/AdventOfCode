#!/usr/bin/env python2
#from random import randint
#import re

def applicable(subs, mol):
    return [i for i in subs if isSubList(i[1], mol)]

def isSubList(s, l):
    for i in range(len(l)-len(s)):
        if l[i:i+len(s)] == s:
            return True
    return False

def subListIndex(s, l):
    for i in range(len(l)-len(s), -1, -1):
        if l[i:i+len(s)] == s:
            return i
    return None
    
    
# def doSub(s, m):
#     head, x, tail = m.rpartition(s[1])
#     return head+s[0]+tail

def doSub(old, new, m):
    start = subListIndex(old, m)
    m[start:start+len(old)] = new
    return m

def tokenise(mol):
    tokens = []
    i = 0
    while i < len(mol):
        tok = mol[i]
        if i+1 < len(mol):
            if mol[i+1].islower():
                tok += mol[i+1]
                i +=1
        tokens.append(tok)
        i+=1
    return tokens

def success(mol):
    return mol == ['H', 'F'] or mol == ['N', 'Al'] or mol == ['O', 'Mg']
    
def randomFrom(l):
    return l[randint(0,len(l)-1)]

def lastPair(mol):
    S = len(mol) - 1
    E = len(mol)
    while S >= 0:
        if mol[S] == Left and mol[S-1] in preLeft:
            S = S - 1 # include the character before Left
            E = S + 1 # skip the Left
            break
        S -= 1
    while E < len(mol):
        if mol[E] == Right:
            E += 1 # include the Right
            break
        E += 1
    return S, E

def deepestPair(mol, direction=+1):
    S = 0
    depth = 0
    maxdepth = 0
    for i in mol:
        char = '.'
        if i == Left:
            char = '('
            depth += 1
            if depth > maxdepth:
                maxdepth = depth
        elif i == Right:
            char = ')'
            depth -= 1
        print char*depth,i
    print 'maxdepth => ',maxdepth
    depth = 0
    if direction == -1:
        E = len(mol) - 1
        while E >= 0:
            if mol[E] == Right:
                depth += 1
                if depth == maxdepth:
                    E += 1 # include the right
                    break
            E -= 1
        if E == -1:
            return -1, len(mol)
        S = E - 1
        while S >= 0:
            if mol[S] == Left:
                return S - 1, E
            S -= 1
        if S == -1:
            return -1, len(mol)
    else:
        S = 0
        while S < len(mol):
            if mol[S] == Left:
                depth += 1
                if depth == maxdepth:
                    S -= 1 # include the pre-left
                    break
            S += 1
        if S >= len(mol):
            return -1, len(mol)
        E = S + 1
        while E < len(mol):
            if mol[E] == Right:
                E += 1 # include the Right
                break
            E += 1
    return S, E

def wholeMol(mol):
    return 0, len(mol)

if __name__ == '__main__':

    # get the input
    fd = open("input.txt", 'r')
    input_data = fd.read()
    fd.close()

    nonArSubs = []
    ArSubs = []
    for l in input_data.splitlines():
        atomIn, sep, atomOut = l.partition(' => ')
        if sep == '':
            if atomIn != '':
                molstr = atomIn
        else:
            if atomOut.endswith('Ar'):
                ArSubs.append(([atomIn], tokenise(atomOut)))
            else:
                nonArSubs.append(([atomIn], tokenise(atomOut)))

    ArSubs.sort(key=lambda x: -len(x[1]))
    nonArSubs.sort(key=lambda x: -len(x[1]))

    mol = tokenise(molstr)
    Left = 'Rn'
    preLeft = set(x[1][0] for x in ArSubs)
    Right = 'Ar'

    steps = 0
    print 'len mol', len(mol)
    print 'left', Left
    print 'right', Right
    print 'preLeft', preLeft

    while True:
        if success(mol): break
        # select S,E based on deepest bracket
        #replace from here
        # this picks the last matching bracket pair
        #S, E = lastPair(mol)
        S, E = deepestPair(mol, -1)
        #S, E = wholeMol(mol)
        #end replace
        if S < 0:
            print 'no LB left.  mol is ' + ''.join(mol)
            S = 0
            E = len(mol)
        subMol = [x for x in mol[S:E]]

        print 'first submol ' + ''.join(subMol)
        print 'at pos [', S, ':', E, ']'

        bracketsPresent = True

        while bracketsPresent:
            # try the ArSubs, longest first...
            subsAvail = False
            for subst, pat in nonArSubs:
                patPos = subListIndex(pat, subMol)
                if patPos is not None:
                    print steps+1, 'subst ' + ''.join(pat) + ' => ' + ''.join(subst)
                    doSub(pat, subst, subMol)
                    steps += 1
                    subsAvail = True
                    break
            for subst, pat in ArSubs:
                patPos = subListIndex(pat, subMol)
                if patPos is not None:
                    print steps+1,'subst ' + ''.join(pat) + ' => ' + ''.join(subst)
                    doSub(pat, subst, subMol)
                    steps += 1
                    bracketsPresent = False
                    subsAvail = True
                    break

            if not subsAvail:
                print 'Ran out of Subs'
                break

        print 'submol substitute to', ''.join(subMol), 'in', steps, 'steps'

        mol[S:E] = subMol

        print 'length is now', len(mol)
        print '#'*len(mol)

        if bracketsPresent:
            print 'got stuck trying to sub',''.join(subMol), 'after', steps, 'steps'
            break
        

    print 'got to', ''.join(mol), 'after', steps, 'steps'
    if success(mol):
        print 'answer is therefore', steps + 1
    else:
        print 'failed'

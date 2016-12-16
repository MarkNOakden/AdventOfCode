#!/usr/bin/env python2
#from random import randint
#import re
import random

def subListIndex(s, l):
    for i in range(0, len(l)-len(s)+1):
        if l[i:i+len(s)] == s:
            return i
    return None

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
    return mol == ['e']

def shorten(s, N):
    if len(s) <=N:
        return s
    half = (N-2)/2
    return s[:half]+'..'+s[-half:]

def checkmol(molstr, patterns):

    #print '|'.join([''.join(x[1][::-1]) for x in patterns])
    #patterns.sort(key=lambda x: -len(x[1]))
    random.shuffle(patterns)
    #for subst, pat in patterns:
    #    print ''.join(pat),'=>',''.join(subst)
        
    mol = tokenise(molstr)
    mol.reverse()

    steps = 0
    #print 'len mol', len(mol)
    #print 'mol: ' + shorten(''.join(mol), 72)

    #print '*'*36+' start '+'*'*36

    canSub = True

    while canSub:
        canSub = False
        for subst, pat in patterns:
            patPos = subListIndex(pat, mol)
            if patPos is not None:
                canSub = True
                break
        if canSub:
            steps += 1
            #print 'step',steps,'subst ' + ''.join(pat) + ' => ' + ''.join(subst)
            #print 'sub '+''.join(pat[::-1])+' for '+''.join(subst)
            doSub(pat, subst, mol)
            #print 'mol:',shorten(''.join(mol), 72)
            #print 'length is now:',len(mol)
            #print '#'*(len(mol)/5)


    #print '*'*37+' end '+'*'*37

    #print 'got to', ''.join(mol), 'after', steps, 'steps'
    if success(mol):
        return steps
    else:
        return -1

if __name__ == '__main__':

    # get the input
    fd = open("input.txt", 'r')
    input_data = fd.read()
    fd.close()
    
    patterns = []
    for l in input_data.splitlines():
        atomIn, sep, atomOut = l.partition(' => ')
        if sep == '':
            if atomIn != '':
                molstr = atomIn
        else:
            subst = tokenise(atomOut)
            subst.reverse()
            patterns.append(([atomIn], subst))

    oddities = []
    successes = 0
    failures = 0
    for i in range(1000):
        res = checkmol(molstr, patterns)
        if res == 195:
            successes += 1
        elif res == -1:
            failures += 1
        else:
            oddities.append(res)

    print successes, failures, oddities

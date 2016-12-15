#!/usr/bin/env python2
from random import randint
import re

def applicable(subs, mol):
    return [i for i in subs if isSubList(i[1], mol)]

def isSubList(s, l):
    for i in range(len(l)-len(s)):
        if l[i:i+len(s)] == s:
            return True
    return False

def SubListIndex(s, l):
    for i in range(len(l)-len(s)):
        if l[i:i+len(s)] == s:
            return i
    
    
def doSub(s, m):
    head, x, tail = m.rpartition(s[1])
    return head+s[0]+tail

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


def randomFrom(l):
    return l[randint(0,len(l)-1)]
        
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
                ArSubs.append((atomIn, tokenise(atomOut)))
            else:
                nonArSubs.append((atomIn, tokenise(atomOut)))

    ArSubs.sort(key=lambda x: -len(x[1]))
    nonArSubs.sort(key=lambda x: -len(x[1]))

    mol = tokenise(molstr)
    Rn = 'Rn'
    Ar = 'Ar'

    
    pos = 0
    lastRn = None
    lastAr = None
    steps = 0
    i = 0
    print mol
    while True:
        if mol[i] == Rn:
            print 'lastRn =',lastRn
            lastRn = i
        elif mol[i] == Ar:
            print 'lastAr =',lastAr
            lastAr = i
            chunk = mol[lastRn-1:lastAr+1]
            ArSubList = applicable(ArSubs, chunk)
            if len(ArSubList) == 1:
                a, b = ArSubList[0]
                print 'Pre Subbing',b,'in mol',mol[lastRn-1:lastAr+1],'for',a
                steps += 1
                mol[lastRn-1:lastAr+1] = a
            else:
                SubList = applicable(nonArSubs, chunk)
                while True:
                    ArSubList = applicable(ArSubList, chunk)
                    if len(ArSubList) ==1:
                        a, b = ArSubList[0]
                        print 'ArLoop Subbing',b,'in mol',mol[lastRn-1:lastAr+1],'for',a
                        steps += 1
                        mol[lastRn-1:lastAr+1] = a
                        break
                    while SubList != []:
                        a, b = SubList[0]
                        steps += 1
                        indx = SubListIndex(b, chunk)
                        if indx != -1:
                            print 'Subloop Subbing',b,'in mol',\
                                mol[lastRn-1+indx:lastRn-1+indx+len(b)],'for',a
                            mol[lastRn-1+indx:lastRn-1+indx+len(b)] = a # not right - need to replace just hte match for this sub
                        LastAr = LastAr - (len(b)-len(a))
                        chunk = mol[lastRn-1:LastAr+1]
                        SubList = applicable(nonArSubs, chunk)
        i += 1
                    
                        
            
        
    
    # s = 0

    # while True:
    #     print 'Molecule length', len(mol)
    #     subMols = []
    #     while mol != '':
    #         head, Ar, mol = mol.partition('Ar')
    #         subMols.append(head+Ar)

    #     for i, m in enumerate(subMols):
    #         print "Submolecule {}: {}".format(i, m)


    #         while applicable(nonArSubs, m) != []:
    #             s += 1
    #             m = doSub(applicable(nonArSubs, m)[0], m)
    #             print s, m
    #         while applicable(ArSubs, m) != []:
    #             s += 1
    #             m = doSub(applicable(ArSubs, m)[0], m)
    #             print s, m

    #         subMols[i] = m

    #         print 'after ',s,' :',m

    #     mol = ''.join(subMols)

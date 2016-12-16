#!/usr/bin/env python2
import unittest
import argparse
import re
from hashlib import md5

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--part', help='part 1 or part 2', type=int)
parser.add_argument('-s', '--salt', help='salt value', type=str)
parser.add_argument('-v', '--verbose',
                    help='dump out all keys and the quint table',
                    action='store_true')
parser.add_argument('-o', '--optimise', help='use sets for lookup',
                    action='store_true')

args = parser.parse_args()

if args.salt is not None:
    salt = args.salt
else:
    salt = 'zpqevtbw'

if args.part is not None:
    part = args.part
else:
    part = 1
#salt = 'abc'
#
# for an attempted optimisation (use sets instead of lists)
class mySet(set):
    def __init__(self, *args, **kwargs):
        set.__init__(self, *args, **kwargs)

    def append(self, *args, **kwargs):
        self.add(*args, **kwargs)

# triples and quins will keep a list of all indices that generate
# triples or quintuplets of each of the possible digits
#
hexdigits = '0123456789abcdef'

triples = {}
quins = {}

for i in hexdigits:
    if args.optimise:
        triples[i] = mySet()
        quins[i] = mySet()
    else:
        triples[i] = []
        quins[i] = []

keys = []

triplesRE = re.compile(r'(.)\1{2,2}')
quinsRE = re.compile(r'(.)\1{4,4}')

if part == 1:
    def smd5(s):
        return md5(s).hexdigest()
else:
    def smd5(s):
        for i in range(2017):
            s = md5(s).hexdigest()
        return s

if __name__ == '__main__':
    i = 0
    run = True
    last = None
    while run:
        keyCandidate = smd5('{}{}'.format(salt, i))
        match = triplesRE.search(keyCandidate)
        if match:
            triples[match.group(1)].append(i)
        # not the following - instructions said only consider
        # the FIRST triple found!
        # for match in triplesRE.finditer(keyCandidate):
        #     triples[match.group(1)].append(i)
        for match in quinsRE.finditer(keyCandidate):
            digit = match.group(1)
            quins[digit].append(i)
            correspondingTriples = [index for index in triples[digit]
                                    if index >= i - 1000
                                    and index != i]
            for key in correspondingTriples:
                keys.append((key, i))
        if len(keys) >= 64 and last is None:
            # check another 1000 hashes in case any of the earlier
            # triples is a key
            last = i + 1000
        if last is not None and i > last:
            # finished
            run = False
        i += 1

    if args.verbose:
        print 'last index checked: {}'.format(i - 1)
        
    keys.sort(key=lambda k: k[0])
    if args.verbose:
        for n, x in enumerate(keys):
            lastkey, correspondingQuin = x
            print 'N={:2} key {} {} (quin {} {})'.format(
                n + 1,
                lastkey,
                smd5('{}{}'.format(salt, lastkey)),
                correspondingQuin,
                smd5('{}{}'.format(salt, correspondingQuin)))

    print 'Part {} answer for salt \'{}\': key {}'.format(part,
                                                          salt,
                                                          keys[63][0])
    #print quins
    if args.verbose:
        print 'quintuples:-'
        for digit in hexdigits:
            print '{}: {}'.format(digit, quins[digit])
        print 'triples:-'
        for digit in hexdigits:
            print '{}: list() of {} indices'.format(digit, len(triples[digit]))
        
    
    
    
    



#!/usr/bin/env python2
import unittest
from itertools import combinations
import string

DEBUG = False

class TestIt(unittest.TestCase):
    def test_01(self):
        self.assertTrue(supportsTLS('abba[mnop]qrst'))
    def test_02(self):
        self.assertFalse(supportsTLS('abcd[bddb]xyyx'))
    def test_03(self):
        self.assertFalse(supportsTLS('aaaa[qwer]tyui'))
    def test_04(self):
        self.assertTrue(supportsTLS('ioxxoj[asdfgh]zxcvbn'))
    def test_05(self):
        self.assertFalse(containsABBA('xxx'))
    def test_06(self):
        self.assertFalse(containsABBA('abcdefghi'))
    def test_07(self):
        self.assertFalse(containsABBA('abab'))
    def test_08(self):
        self.assertTrue(containsABBA('abba'))
    def test_09(self):
        self.assertTrue(containsABBA('xxabbax'))
    def test_10(self):
        self.assertTrue(supportsTLS('xxxabba[foolkoi]lkjhgfds'))
    def test_11(self):
        self.assertTrue(containsABBA('zduoybbzxigwggwu'))
    #Pt 2 tests
    def test_12(self):
        self.assertEqual(getABAs('asdfd'), set(['dfd']))
    def test_13(self):
        self.assertEqual(getABAs('xababyaba'), set(['aba', 'bab']))
    def test_14(self):
        self.assertEqual(ABA2BAB('dfd'), 'fdf')
    def test_15(self):
        self.assertTrue(supportsSSL('aba[bab]xyz'))
    def test_16(self):
        self.assertFalse(supportsSSL('xyx[xyx]xyx'))
    def test_17(self):
        self.assertTrue(supportsSSL('aaa[kek]eke'))
    def test_18(self):
        self.assertTrue(supportsSSL('zazbz[bzb]cdb'))
    # assumption about set objects
    def test_19(self):
        self.assertEqual(set(['a', 'b']), set(['b', 'a']))



with open('input.txt', 'r') as fd:
    input_data = fd.read()

def dprint(s):
    if DEBUG:
        print s

alpha = string.ascii_lowercase
#ABBAs = [''.join(x + x[::-1]) for x in combinations(alpha, 2)]

ABBAs = []
for x in combinations(alpha, 2):
    ABBAs.append(''.join(x + x[::-1]))
    ABBAs.append(''.join(x[::-1] + x))

# Addresses are strings of lowercase characters with 0 or more
# sections in square brackets [].  Square brackets are always
# in matched pairs and are not nested.
#
# Logic:
#
# 1. Check for ABBAs in sections in square brackets.  If found,
# immediately return False
#
# 2. If not failed by (1) then check for ABBAs in the strings
# not in square brackets. If one is found, return True
#
# 3. If neither of the above, return False

def splitHypernets(addr):
    hypernets = []
    supernets = []

    while '[' in addr:
        non, bracket, hyper = addr.partition('[')
        if len(non):
            supernets.append(non)
        hyper, bracket, addr = hyper.partition(']')
        if len(hyper):
            hypernets.append(hyper)

    if len(addr):
        supernets.append(addr)
    
    return hypernets, supernets


def containsABBA(s):
    # Too short? return False immediately
    if len(s) < 4:
        return False
    # Are any length 4 substrings ABBAs?
    for i in range(len(s) - 3):
        sub = s[i:i+4]
        if sub in ABBAs:
            return True
    # Otherwise False
    return False


def supportsTLS(addr):
    hypernets, supernets = splitHypernets(addr)

    # check the hypernet gateways...
    for s in hypernets:
        if containsABBA(s):
            return False

    # check the non-hypernets
    for s in supernets:
        if containsABBA(s):
            return True

    return False

def getABAs(s):
    abas = set()
    for i in range(len(s)-2):
        sub = s[i:i+3]
        if (sub[0] == sub[2]) and (sub[0] != sub[1]):
            abas.add(sub)
    return abas


def ABA2BAB(aba):
    return aba[1]+aba[0:2]


def supportsSSL(addr):
    hypernets, supernets = splitHypernets(addr)

    # get the ABAs fromt eh supernets
    ABAs = set()
    for s in supernets:
        ABAs |= getABAs(s)
    # get the BABs from hypernets
    BABs = set()
    for s in hypernets:
        BABs |= getABAs(s)

    # convert BABs to corresponding ABAs
    hyperABAs = set(map(ABA2BAB, BABs))

    # if ABAs and hyperABAs are not disjoint, the network supports SSL
    
    return not ABAs.isdisjoint(hyperABAs)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    tlsCount = 0
    sslCount = 0
    for addr in input_data.splitlines():
        if supportsTLS(addr):
            tlsCount += 1
        if supportsSSL(addr):
            sslCount += 1

    print '{} addresses support TLS'.format(tlsCount)
    print '{} addresses support SSL'.format(sslCount)

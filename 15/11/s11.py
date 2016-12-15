#!/usr/bin/env python2
import unittest, re

class TestIt(unittest.TestCase):
    # Part 1 tests
        
    def test_01(self):
        self.assertEqual(incr('aa'), 'ab')
 
    def test_02(self):
        self.assertEqual(incr('az'), 'ba')
 
    def test_03(self):
        self.assertEqual(incr('zz'), 'aaa')

    def test_04(self):
        self.assertFalse(pwOK('hijklmmn'))

    def test_05(self):
        self.assertFalse(pwOK('abbceffg'))

    def test_06(self):
        self.assertFalse(pwOK('abbcegjk'))

    def test_07(self):
        self.assertTrue(pwOK('abcdffaa'))

    def test_08(self):
        self.assertTrue(pwOK('ghjaabcc'))

    def test_09(self):
        self.assertEqual(jumpPW('abcdi'), 'abcdj')

    def test_10(self):
        self.assertEqual(jumpPW('obcde'), 'paaaa')

    def test_11(self):
        self.assertEqual(jumpPW('ablde'), 'abmaa')

    #def test_12(self):
    #    self.assertEqual(nextPW('abcdefgh'), 'abcdffaa')

    #def test_13(self):
    #    self.assertEqual(nextPW('ghijklmn'), 'ghjaabcc')




input_data = 'hepxcrrq'

OVER=chr(ord('z') + 1)

def incr(s):
    if s == 'z':
        return 'aa'
    head = s[0:-1]
    tail = s[-1]
    tail = chr(ord(tail) + 1)
    if tail == OVER:
        return incr(head) + 'a'
    #elif tail == 'i' or tail == 'l' or tail == 'o':
    #    # skip an extra one
    #    return head + chr(ord(tail) + 1)
    else:
        return head + tail
    
twopairs = re.compile(r'.*(.)\1.*(.)\2.*')

def pwOK(pw):
    # check i, l, o
    for i in ['i', 'l', 'o']:
        if i in pw:
            return False
    # check for a run (skip the ones containing i,l o)
    run = False
    for i in ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', \
              'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', \
              'vwx', 'wxy', 'xyz']:
        if i in pw:
            run = True
    if not run:
        return False
    # check for two doubles
    if twopairs.search(pw) is None:
        return False
    return True

ilo = re.compile(r'[ilo]')

def jumpPW(s):
    if 'i' in s  or 'l' in s or 'o' in s:
        pos = ilo.search(s).start()
        res = s[0:pos] + chr(ord(s[pos]) + 1) + 'a' * len(s[pos+1:])
        #print 'Jump from ' + s + ' to ' + res
        return res
    else:
        return s

def nextPW(s):
    s = incr(s)
    while not pwOK(s):
        s = incr(s)
        s = jumpPW(s)
    return s


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    nextSantaPassword = nextPW(input_data)
    print 'next santa password is', nextSantaPassword
    print 'part 2 - and the next one is:', nextPW(nextSantaPassword)
    
    
        
    


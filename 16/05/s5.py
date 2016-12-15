#!/usr/bin/env python2
import sys
import random
import unittest
from hashlib import md5

input_key = 'uqwqemis'

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(nextInputNum('abc', 0, 5),
                         (3231929, '1'))
    def test_2(self):
        self.assertEqual(nextInputNum('abc', 3231930, 5),
                         (5017308, '8'))
    def test_3(self):
        self.assertEqual(nextInputNum('abc', 5017309, 5),
                         (5278568, 'f'))
    def test_4(self):
        self.assertEqual(password('abc', 5, 8), '18f47a30')
    def test_5(self):
        self.assertEqual(password2('abc', 5, 8), '05ace8e3')

def nextInputNum(key, start, m):
    i = start
    while True:
        md5hash = md5(key+str(i)).hexdigest()
        if md5hash[0:m] == '0'*m:
            char = md5hash[m]
            break
        i+=1
    return i, char

def password(key, m, pwlen):
    pw = ''
    i = 0
    for x in range(pwlen):
        last, c = nextInputNum(key, i, m)
        i = last + 1
        pw += c
    return pw

hexdigits = '0123456789abcdef'
def nextInputNum2(key, start, m, pw):
    # with added HollywoodOS style "animation"
    i = start
    while True:
        md5hash = md5(key+str(i)).hexdigest()
        if md5hash[0:m] == '0'*m:
            char = md5hash[m]
            break
        i += 1
        if i % 1000 == 0:
            print '\rPassword:', hwos(pw),
            sys.stdout.flush()
    return i, char

def password2(key, m, pwlen):
    valid = hexdigits[:pwlen]
    pw = '_'*pwlen
    i = 0
    while '_' in pw:
        last, pos = nextInputNum2(key, i, m, pw)
        if pos in valid:
            if pw[int(pos)] == '_':
                p = int(pos)
                pw = pw[0:p] + \
                  md5(key+str(last)).hexdigest()[m+1] + \
                  pw[p+1:]
        print '\rPassword:', hwos(pw),
        sys.stdout.flush()
        i = last + 1
    print ''
    return pw

def hwos(s):
    return ''.join([c if c != '_' else random.choice(hexdigits) for c in s])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print "Part 1:", password(input_key, 5, 8)
    print "Part 2:", password2(input_key, 5, 8)

    



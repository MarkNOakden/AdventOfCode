#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    # Part 1 tests
    def test_hasBadStrings_1(self):
        self.assertTrue(hasBadStrings('abc'))
    def test_hasBadStrings_2(self):
        self.assertTrue(hasBadStrings('abcdpqxy'))
    def test_hasBadStrings_3(self):
        self.assertFalse(hasBadStrings('aaaaaaaaa'))
    def test_vowels_1(self):
        self.assertTrue(lessThanThreeVowels('abc'))
    def test_vowels_2(self):
        self.assertTrue(lessThanThreeVowels('aec'))
    def test_vowels_3(self):
        self.assertFalse(lessThanThreeVowels('aei'))
    def test_vowels_4(self):
        self.assertFalse(lessThanThreeVowels('aaaaaaa'))
    def test_noDouble_1(self):
        self.assertTrue(noDoubleLetter('abcdefg'))
    def test_noDouble_2(self):
        self.assertTrue(noDoubleLetter('jchzalrnumimnmhp'))
    def test_noDouble_3(self):
        self.assertFalse(noDoubleLetter('ugknbfddgicrmopn'))
    # Part 1 examples
    def test_1(self):
        self.assertTrue(isNice('ugknbfddgicrmopn'))
    def test_2(self):
        self.assertTrue(isNice('aaa'))
    def test_3(self):
        self.assertFalse(isNice('jchzalrnumimnmhp'))
    def test_4(self):
        self.assertFalse(isNice('haegwjzuvuyypxyu'))
    def test_5(self):
        self.assertFalse(isNice('dvszwmarrgswjxmb'))
    # Part 2 tests
    def test_noDoublePair_1(self):
        self.assertTrue(noDoublePair('abcdefghijklmnop'))
    def test_noDoublePair_2(self):
        self.assertFalse(noDoublePair('abab'))
    def test_noDoublePair_3(self):
        self.assertFalse(noDoublePair('hjaaiuytaah'))
    def test_noDoublePair_4(self):
        self.assertFalse(noDoublePair('aafriuytaa'))
    def test_noRepeat_1(self):
        self.assertTrue(noRepeat('abcdefghij'))
    def test_noRepeat_2(self):
        self.assertFalse(noRepeat('xyxabcdefghij'))
    def test_noRepeat_3(self):
        self.assertFalse(noRepeat('abcxyxdefghij'))
    def test_noRepeat_4(self):
        self.assertFalse(noRepeat('abcdefghijxyx'))
    # Part 2 examples
    def test_6(self):
        self.assertTrue(isNice2('qjhvhtzxzqqjkmpb'))
    def test_7(self):
        self.assertTrue(isNice2('xxyxx'))
    def test_8(self):
        self.assertFalse(isNice2('uurcxstgmygtbstg'))
    def test_8(self):
        self.assertFalse(isNice2('ieodomkazucvgmuy'))


# get the input
fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

doubleLetters = []
for letter in 'abcdefghijklmnopqrstuvwxyz':
    doubleLetters.append(letter*2)

print doubleLetters

badstrings = ['ab', 'cd', 'pq', 'xy']


# return True for a nice string False for naughty
def isNice(testString):
    if hasBadStrings(testString):
        return False
    if lessThanThreeVowels(testString):
        return False
    if noDoubleLetter(testString):
        return False
    return True

def lessThanThreeVowels(testString):
    return (len(testString) \
            - len(testString.translate(None, 'aeiou'))) < 3

def hasBadStrings(testString):
    for bs in badstrings:
        if bs in testString:
            return True
    return False

def noDoubleLetter(testString):
    for i in range(0,len(testString)-1):
        if testString[i:i+2] in doubleLetters:
            return False
    return True

# Part 2
def isNice2(testString):
    if noDoublePair(testString):
        return False
    if noRepeat(testString):
        return False
    return True

def noDoublePair(testString):
    for i in range(0, len(testString)-2):
        if testString[i:i+2] in testString[i+2:]:
            return False
    return True

def noRepeat(testString):
    for i in range(0,len(testString)-2):
        if testString[i] == testString[i+2]:
            return False
    return True


niceCount = 0
niceCount2 = 0

for santaString in input_data.split():
    if isNice(santaString):
        niceCount += 1
    if isNice2(santaString):
        niceCount2 += 1

    

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print "Part 1: number of nice strings is ", \
        niceCount
    print "Part 2: number of nice strings is ", \
        niceCount2
    
    

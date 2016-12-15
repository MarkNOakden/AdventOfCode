#!/usr/bin/env python2
import unittest
import re

class TestIt(unittest.TestCase):
    def test_01(self):
        self.assertEqual(dLen('ADVENT',
                              gen_output=True),
                         (6, 'ADVENT'))
    def test_02(self):
        self.assertEqual(dLen('A(1x5)BC',
                              gen_output=True),
                         (7, 'ABBBBBC'))
    def test_03(self):
        self.assertEqual(dLen('(3x3)XYZ',
                              gen_output=True),
                         (9, 'XYZXYZXYZ'))
    def test_04(self):
        self.assertEqual(dLen('A(2x2)BCD(2x2)EFG', gen_output=True),
                         (11, 'ABCBCDEFEFG'))
    def test_05(self):
        self.assertEqual(dLen('(6x1)(1x3)A', gen_output=True),
                         (6, '(1x3)A'))
    def test_06(self):
        self.assertEqual(dLen('X(8x2)(3x3)ABCY', gen_output=True),
                         (18, 'X(3x3)ABC(3x3)ABCY'))
    def test_07(self):
        self.assertEqual(dLen('(1x11)B', gen_output=True),
                         (11, 'BBBBBBBBBBB'))
    def test_08(self):
        self.assertEqual(dLen('(11x11)BBBBBBBBBBB', gen_output=True),
                         (121, 'B'*121))
    def test_09(self):
        self.assertEqual(dLen2('(3x3)XYZ'),
                         9)
    def test_10(self):
        self.assertEqual(dLen2('X(8x2)(3x3)ABCY'),
                         20)
    def test_10(self):
        self.assertEqual(dLen2('(27x12)(20x12)(13x14)(7x10)(1x12)A'),
                         241920)
    def test_10(self):
        self.assertEqual(dLen2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'),
                         445)
    def test_11(self):
        self.assertEqual(dLen2('(19x14)(3x2)ZTN(5x14)MBPWH'),
                         76*14)
                               

with open('input.txt', 'r') as fd:
    input_data = fd.read()

marker = re.compile('\(([0-9]+)x([0-9]+)\)')

# Since we're not asked for the string in part 1, just the length
# lets not explicitly construct the string, just keep a running
# tally of its length.  This decision will probably come back to
# bite me in part 2

def dLen(comp, gen_output=False):
    output = ''
    runningLen = 0
    match = marker.search(comp)
    while match:
        mlen = int(match.group(1))
        mrepeats = int(match.group(2))
        startpos = match.start()
        endpos = match.end()
        # characters before the match are verbatim in the output
        runningLen += startpos
        if gen_output:
            output += comp[:startpos]
        # add on the uncompressed length
        runningLen += mlen * mrepeats
        if gen_output:
            output += comp[endpos:(endpos + mlen)] * mrepeats
        # chop the front of the string off
        comp = comp[(endpos + mlen):]
        match = marker.search(comp)
    # anything left over must be added verbatim
    runningLen += len(comp)
    if gen_output:
        output += comp
    return runningLen, output

# multiplier = 1
# runningTotal = 0
# find a match...
# discard characters up to the match and add to runningTotal
# copy match-end -> match end + mlen to chunk
# multiplier = multiplier * repeats
# if chunk contains no matches:
#    add len(chunk) *  multiplier to runningTotal
# else
#   for each match
#     recurse on match-end -> match-end + mlen
def dLen2(comp):
    p1 = 0
    p2 = len(comp)
    match = marker.search(comp)
    sum = 0
    while match:
        front = comp[p1:match.start()]
        sum += len(front)
        
        mlen = int(match.group(1))
        mrepeats = int(match.group(2))

        p1 = match.end()
        p2 = match.end() + mlen

        if marker.search(comp, p1, p2):
            sum += mrepeats * dLen2(comp[p1:p2])
        else:
            sum += mlen * mrepeats

        p1 = p2 # advance...
        match = marker.search(comp, p1)

    sum += len(comp[p2:])
    return sum


    

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    input_data = input_data.strip()
    
    length, output = dLen(input_data)
    print 'Part 1 - Input decompresses to {} chars'.format(length)

    length2 = dLen2(input_data)
    print 'Part 2 - Input decompresses to {} chars'.format(length2)
    


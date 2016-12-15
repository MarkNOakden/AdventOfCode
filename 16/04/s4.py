#!/usr/bin/env python2
import unittest

import string
from collections import Counter

class TestIt(unittest.TestCase):
    def test_1(self):
        r = Room('aaaaa-bbb-z-y-x-123[abxyz]')
        self.assertEqual(r.checksum, 'abxyz')

    def test_2(self):
        r = Room('aaaaa-bbb-z-y-x-123[abxyz]')
        self.assertEqual(r.isvalid(), True)

    def test_3(self):
        r = Room('a-b-c-d-e-f-g-h-987[abcde]')
        self.assertEqual(r.checksum, 'abcde')

    def test_4(self):
        r = Room('a-b-c-d-e-f-g-h-987[abcde]')
        self.assertEqual(r.isvalid(), True)

    def test_5(self):
        r = Room('not-a-real-room-404[oarel]')
        self.assertEqual(r.checksum, 'oarel')

    def test_6(self):
        r = Room('not-a-real-room-404[oarel]')
        self.assertEqual(r.isvalid(), True)

    def test_7(self):
        r = Room('totally-real-room-200[decoy]')
        self.assertEqual(r.checksum, 'decoy')
    
    def test_8(self):
        r = Room('totally-real-room-200[decoy]')
        self.assertEqual(r.isvalid(), False)

    def test_9(self):
        r = Room('qzmt-zixmtkozy-ivhz-343[zzzzz]')
        self.assertEqual(r.decrypted(), 'very encrypted name')

with open('input.txt', 'r') as fd:
    input_data = fd.read()

class Room(object):
    def __init__(self, entry):
        self.name, sep, rest = entry.partition('[')
        self.name, sep, self.sectorid = self.name.rpartition('-')
        self.sectorid = int(self.sectorid)
        self.checksum, sep, rest = rest.partition(']')

    def check(self):
        counted = Counter(self.name.replace('-', ''))
        most_common = counted.most_common()
        most_common_sorted = sorted(most_common, key=lambda x: (-x[1], x[0]))[0:5]
        check = ''.join([x[0] for x in most_common_sorted])
        # won't work since ordering of ties is not handled...
        return check

    def isvalid(self):
        return self.checksum == self.check()

    def decrypted(self):
        rot = self.sectorid % 26
        lowerchars = string.ascii_lowercase
        upperchars = string.ascii_uppercase
        shiftedlower = lowerchars[rot:] + lowerchars[:rot]
        shiftedupper = upperchars[rot:] + upperchars[:rot]

        alphabet = '-' + lowerchars + upperchars
        shiftedalphabet = ' ' + shiftedlower + shiftedupper

        trans = string.maketrans(alphabet, shiftedalphabet)
        return self.name.translate(trans)
        
    def __str__(self):
        fmt = 'Room: name={}, sectorid={}, check={}, checksum={}, isvalid={}'
        return fmt.format(self.name,
                          self.sectorid,
                          self.check(),
                          self.checksum,
                          self.isvalid())

    __repr__ = __str__

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    allRooms = map(Room, input_data.splitlines())

    sectorsum = sum([x.sectorid for x in allRooms if x.isvalid()])
    print 'the sector sum for valid rooms is: ',sectorsum

    decrypted = [(x.decrypted(), x.sectorid) for x in allRooms]

    for i in decrypted:
        if 'north' in i[0]:
            print '{}: {}'.format(i[0], i[1])

        

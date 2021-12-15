"""Tests for Advent of Code 2021 day 01"""

import pandas as pd
from io import StringIO

import unittest

from day01 import part1, part2

depths_test_txt = StringIO(
    """199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """
)

depths_test = pd.read_csv(
    depths_test_txt,
    header=None,
    names=['depth'],
    dtype=int,
)


class TestDay01(unittest.TestCase):

    def test_part1_01(self):
        self.assertEqual(part1(depths_test), 7)

    def test_part2_01(self):
        self.assertEqual(part2(depths_test), 5)


if __name__ == '__main__':
    unittest.main()

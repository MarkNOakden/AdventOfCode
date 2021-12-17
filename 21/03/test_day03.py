"""Tests for Advent of Code 2021 day 03"""

import unittest
from day03 import P1Diagnostic, P2Diagnostic, parse_input
from io import StringIO

test_data_str = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


class TestDayNN(unittest.TestCase):

    def setUp(self):
        fd = StringIO(test_data_str)

        self.test_data = parse_input(fd)
        self.part1_01_result = 198
        self.part2_01_result = 230

    def test_part1_01(self):
        self.assertEqual(
            P1Diagnostic(self.test_data).power_consumption,
            self.part1_01_result
        )

    def test_part2_01(self):
        self.assertEqual(
            P2Diagnostic(self.test_data).life_support_rating,
            self.part2_01_result
        )


if __name__ == '__main__':
    unittest.main()

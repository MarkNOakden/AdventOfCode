"""Tests for Advent of Code 2021 day 01"""

import unittest
from day02 import part1, part2, parse_input

from io import StringIO

test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class TestDay02(unittest.TestCase):

    def setUp(self):
        test_fd = StringIO(test_data)

        self.part1_01_result = 150
        self.part2_01_result = 900

        self.input_prog = parse_input(test_fd)

    def test_part1_01(self):
        self.assertEqual(part1(self.input_prog), self.part1_01_result)

    def test_part2_01(self):
        self.assertEqual(part2(self.input_prog), self.part2_01_result)


if __name__ == '__main__':
    unittest.main()

"""Tests for Advent of Code 2021 day NN"""

import unittest
from dayNN import part1, part2, parse_input
from io import StringIO

test_data_str = """"""


class TestDayNN(unittest.TestCase):

    def setUp(self):
        fd = StringIO(test_data_str)

        self.test_data = parse_input(fd)
        self.part1_01_result = None
        self.part2_01_result = None

    def test_part1_01(self):
        self.assertEqual(
            self.part1_01_result,
            part1(self.test_data)
        )

    def test_part2_01(self):
        self.assertEqual(
            self.part2_01_result,
            part2(self.test_data)
        )


if __name__ == '__main__':
    unittest.main()

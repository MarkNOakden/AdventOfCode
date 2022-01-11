"""Tests for Advent of Code 2021 day 07"""

import unittest
from day07 import part1, part2, fuel_cost, parse_input
from io import StringIO

test_data_str = """16,1,2,0,4,2,7,1,2,14"""
test_pos_fuel = {1: 41, 2: 37, 3: 39, 10: 71}
test_min_pos = 2
test_min_fuel = 37

test_min_fuel_2 = 168


class TestDay07(unittest.TestCase):

    def setUp(self):
        fd = StringIO(test_data_str)

        self.crabs = parse_input(fd)
        self.part1_01_result = test_min_fuel
        self.part1_01_pos = test_min_pos
        self.pos_fuel = test_pos_fuel
        self.part2_01_result = test_min_fuel_2

    def test_fuel_cost(self):
        for pos in self.pos_fuel.keys():
            with self.subTest(position=pos):
                self.assertEqual(
                    self.pos_fuel[pos],
                    fuel_cost(self.crabs, pos)
                )

    def test_part1_01(self):
        self.assertEqual(
            self.part1_01_result,
            part1(self.crabs)[1]
        )

    def test_part1_02(self):
        self.assertEqual(
            self.part1_01_pos,
            part1(self.crabs)[0]
        )

    def test_part2_01(self):
        self.assertEqual(
            self.part2_01_result,
            part2(self.crabs)[1]
        )


if __name__ == '__main__':
    unittest.main()

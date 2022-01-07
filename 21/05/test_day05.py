"""Tests for Advent of Code 2021 day 05"""

import unittest
from day05 import Line, VentField, parse_input
from io import StringIO

test_data_str = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


class TestDay05(unittest.TestCase):

    def setUp(self):
        fd = StringIO(test_data_str)

        self.test_data = parse_input(fd)

        self.part1_01_result = 5
        self.part2_01_result = 12

        # An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
        # An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
        self.line1 = Line(1, 1, 1, 3)
        self.line1_points = [(1, 1), (1, 2), (1, 3)]

        self.line2 = Line(9, 7, 7, 7)
        self.line2_points = [(9, 7), (8, 7), (7, 7)]

        # An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
        # An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
        self.line3 = Line(1, 1, 3, 3)
        self.line3_points = [(1, 1), (2, 2), (3, 3)]

        self.line4 = Line(9, 7, 7, 9)
        self.line4_points = [(9, 7), (8, 8), (7, 9)]

        self.vf1 = VentField(self.test_data)
        self.vf2 = VentField(self.test_data, include_diagonals=True)

    def test_line1_horizontal(self):
        self.assertFalse(self.line1.is_horizontal)

    def test_line1_vertical(self):
        self.assertTrue(self.line1.is_vertical)

    def test_line1_points(self):
        self.assertEqual(
            self.line1_points,
            self.line1.points
        )

    def test_line2_points(self):
        self.assertEqual(
            self.line2_points,
            self.line2.points
        )

    def test_line3_points(self):
        self.assertEqual(
            self.line3_points,
            self.line3.points
        )

    def test_line4_points(self):
        self.assertEqual(
            self.line4_points,
            self.line4.points
        )

    def test_part1_01(self):
        self.assertEqual(
            self.part1_01_result,
            len(self.vf1.hotspots)
        )

    def test_part2_01(self):
        self.assertEqual(
            self.part2_01_result,
            len(self.vf2.hotspots)
        )


if __name__ == '__main__':
    unittest.main()

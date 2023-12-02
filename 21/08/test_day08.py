"""Tests for Advent of Code 2021 day 08"""

import unittest
from day08 import part1, part2, parse_input
from io import StringIO

test_data_str = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

test_results = [2, 3, 3, 1, 3, 4, 3, 1, 4, 2]

test_sum = 26

# check that the test data is correct!
assert(sum(test_results) == test_sum)

class TestDay08(unittest.TestCase):

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

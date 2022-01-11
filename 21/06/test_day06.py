"""Tests for Advent of Code 2021 day 06"""

import unittest
from day06 import evolve, evolve2, fishcounter, part1, part2, parse_input
from io import StringIO

test_data_str = """3,4,3,1,2"""

test_results_str = """After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8"""

evolution_test_results = [
    l.split(':')[1].strip() for l in test_results_str.split('\n')
]

test_result_80day = 5934
test_result_256day = 26984457539


def counts_as_string(counts):
    res = []
    for i in sorted(counts.keys()):
        if counts[i] != 0:
            res.append(f'{i}:{counts[i]}')
    return ','.join(res)


class TestDay06(unittest.TestCase):

    def setUp(self):
        fd = StringIO(test_data_str)

        self.test_data = parse_input(fd)
        self.evolution_results = evolution_test_results
        self.part1_01_result = test_result_80day
        self.part2_01_result = test_result_256day

    def test_evolution(self):
        for i in range(len(self.evolution_results)):
            evolve(self.test_data)
            with self.subTest(generation=i + 1):
                self.assertEqual(
                    self.evolution_results[i],
                    ','.join(map(str, self.test_data))
                )

    def test_evolution2(self):
        fishcounts = fishcounter(self.test_data)
        for i in range(len(self.evolution_results)):
            evolve2(fishcounts)
            with self.subTest(generation=i + 1):
                self.assertEqual(
                    counts_as_string(
                        fishcounter(
                            list(map(int, self.evolution_results[i].split(',')))
                        )
                    ),
                    counts_as_string(fishcounts)
                )

    def test_part1_01(self):
        self.assertEqual(part1(self.test_data), self.part1_01_result)

    def test_part2_01(self):
        self.assertEqual(part2(self.test_data), self.part2_01_result)


if __name__ == '__main__':
    unittest.main()

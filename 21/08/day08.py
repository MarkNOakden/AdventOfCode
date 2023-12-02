"""Advent of Code 2021 day 08"""


segments_to_digits = {
    frozenset('abcefg'): 0,
    frozenset('cf'): 1,
    frozenset('acdeg'): 2,
    frozenset('acdfg'): 3,
    frozenset('bcdf'): 4,
    frozenset('abdfg'): 5,
    frozenset('abdefg'): 6,
    frozenset('acf'): 7,
    frozenset('abcdefg'): 8,
    frozenset('abcdfg'): 9,
}

digits_to_segments = {v: k for k, v in segments_to_digits.items()}

class SevenSegmentDigit:

    def __init__(self, _mapping=None):
        if _mapping is None:
            self._mapping = {w: w for w in 'abcdefg'}
        else:
            self._mapping = _mapping
        self._matrix = None

    @property
    def matrix(self, signals):




class TestResult:

    def __init__(self, patterns, outputs):
        self.patterns = patterns
        self.outputs = outputs
        self._mapping = dict()

    def __str__(self):
        retval = ' '.join(''.join(p) for p in self.patterns) \
                 + ' | ' \
                 + ' '.join(''.join(d) for d in self.outputs)
        return retval

def part1(*args):
    pass


def part2(*args):
    pass


def parse_input(input_fd):
    pass


if __name__ == '__main__':
    with open('input.txt') as fd:
        parse_input(fd)

    print('Part1: ', part1())
    print('Part2: ', part2())

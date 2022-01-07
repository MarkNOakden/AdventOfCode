"""Advent of Code 2021 day 05"""

import re
from collections import Counter

parser_re = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')


def inclusive_range(a, b):
    """Helper function to return inclusive ranges between a pair of integers

    """
    if a <= b:
        step = 1
    else:
        step = -1
    return range(a, b + step, step)


class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def is_horizontal(self):
        return self.y1 == self.y2

    @property
    def is_vertical(self):
        return self.x1 == self.x2

    @property
    def points(self):
        if self.is_vertical:
            return [(self.x1, y) for y in inclusive_range(self.y1, self.y2)]
        elif self.is_horizontal:
            return [(x, self.y1) for x in inclusive_range(self.x1, self.x2)]
        else:
            return list(
                zip(
                    inclusive_range(self.x1, self.x2),
                    inclusive_range(self.y1, self.y2)
                )
            )

    def __repr__(self):
        return f'Line({self.x1}, {self.y1}, {self.x2}, {self.y2})'


class VentField:

    def __init__(self, input_list, include_diagonals=False):
        self.lines = [Line(*coords) for coords in input_list]
        self.include_diagonals = include_diagonals
        self._vent_density = Counter()

    @property
    def vent_density(self):
        if len(self._vent_density) != 0:
            return self._vent_density
        for line in self.lines:
            if (
                    (line.is_horizontal or line.is_vertical)
                    or self.include_diagonals
            ):
                self._vent_density.update(line.points)
        return self._vent_density

    @property
    def hotspots(self, threshold=1):
        return [i for i in self.vent_density.most_common() if i[1] > threshold]


def parse_input(input_fd):
    lines = input_fd.read().splitlines()
    return list(
        map(
            lambda x: list(
                map(int, parser_re.match(x).groups())
            ),
            lines
        )
    )


if __name__ == '__main__':
    with open('input.txt') as fd:
        data = parse_input(fd)

    vf1 = VentField(data)
    print('Part1: ', len(vf1.hotspots))

    vf2 = VentField(data, include_diagonals=True)
    print('Part2: ', len(vf2.hotspots))

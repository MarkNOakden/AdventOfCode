"""Advent of Code 2021 day 02"""


class P1Submarine:

    def __init__(self, prog):
        self.horizontal = 0
        self.vertical = 0
        self.program = prog

    def reset(self):
        self.horizontal = 0
        self.vertical = 0

    def run_program(self):
        self.reset()
        for command, dist in self.program:
            getattr(self, command)(dist)

    def position_product(self):
        return self.horizontal * self.vertical

    def forward(self, dist):
        self.horizontal += dist

    def up(self, dist):
        self.vertical -= dist

    def down(self, dist):
        self.vertical += dist


class P2Submarine(P1Submarine):

    def __init__(self, prog):
        super().__init__(prog)
        self.aim = 0

    def reset(self):
        super().reset()
        self.aim = 0

    def forward(self, dist):
        self.horizontal += dist
        self.vertical += self.aim * dist

    def up(self, dist):
        self.aim -= dist

    def down(self, dist):
        self.aim += dist


def part1(ip):
    sub = P1Submarine(ip)
    sub.run_program()

    return sub.position_product()


def part2(ip):
    sub = P2Submarine(ip)
    sub.run_program()

    return sub.position_product()


def parse_input(input_fd):
    lines = input_fd.read().splitlines()

    prog = [line.split(' ') for line in lines]
    prog = [(row[0], int(row[1])) for row in prog]

    return prog


if __name__ == '__main__':
    with open('input.txt') as input_fd:
        input_prog = parse_input(input_fd)

    print('Part1: ', part1(input_prog))
    print('Part2: ', part2(input_prog))

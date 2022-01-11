"""Advent of Code 2021 day 07"""


def fuel_cost(_crabs, pos):
    return sum(abs(crab - pos) for crab in _crabs)


def _calc(_crabs, fc_func):
    _sorted_crabs = sorted(_crabs)
    l = len(_sorted_crabs)
    if (l % 2) == 0:
        mid = l // 2
    else:
        mid = (l - 1) // 2
    pos = _sorted_crabs[mid]

    while True:
        score = fc_func(_crabs, pos)
        if (pos == 0) or (pos == (len(_sorted_crabs) - 1)):
            raise RuntimeError('ran out of crabs')
        left_score = fc_func(_crabs, pos - 1)
        right_score = fc_func(_crabs, pos + 1)
        if (left_score > score) and (right_score > score):
            return pos, score
        elif (left_score > score) and (right_score < score):
            pos += 1
        elif (left_score < score) and (right_score > score):
            pos -= 1


def fuel_cost2(_crabs, pos):
    return sum(
        (abs(crab - pos) * (abs(crab - pos) + 1)) // 2 for crab in _crabs)


def part1(_crabs):
    return _calc(_crabs, fuel_cost)


def part2(_crabs):
    return _calc(_crabs, fuel_cost2)


def parse_input(input_fd):
    line = input_fd.read()
    return list(map(int, line.split(',')))


if __name__ == '__main__':
    with open('input.txt') as fd:
        crabs = parse_input(fd)

    print('Part1: ', part1(crabs)[1])
    print('Part2: ', part2(crabs)[1])

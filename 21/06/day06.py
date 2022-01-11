"""Advent of Code 2021 day 06"""

from collections import defaultdict


# Part 1 - start with a naive, brute force evolution
def evolve(fish):
    # spawn new fish
    newfish = []
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            newfish.append(8)
        else:
            # decrement counters
            fish[i] -= 1
        # add newly spawned fish
    fish += newfish
    return len(fish)


# part 2 - too many generations for naive brute force: work with counts of fish
# per age value
def fishcounter(fish):
    counts = defaultdict(int)
    for i in fish:
        counts[i] += 1
    return counts


def evolve2(fishcounts):
    _tmp = fishcounts[0]
    for i in range(6):
        fishcounts[i] = fishcounts[i + 1]
    fishcounts[6] = _tmp + fishcounts[7]
    fishcounts[7] = fishcounts[8]
    fishcounts[8] = _tmp
    return sum(fishcounts.values())


def iterated_evolve(state, generations, evolver=evolve):
    for i in range(generations):
        res = evolver(state)
    return res


def part1(fish):
    return iterated_evolve(fish, 80)


def part2(fish):
    fishcounts = fishcounter(fish)
    return iterated_evolve(fishcounts, 256, evolve2)


def parse_input(input_fd):
    data = input_fd.readline()
    return list(map(int, data.strip().split(',')))


if __name__ == '__main__':
    with open('input.txt') as fd:
        fish = parse_input(fd)

    print('Part1: ', part1(fish.copy()))  # copy here so we can use `fish` in p2
    print('Part2: ', part2(fish))

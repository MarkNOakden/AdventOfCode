from typing import List, Iterable


def get_data() -> List[int]:
    with open('input.txt') as fd:
        numbers = list(map(int, fd.readlines()))
        return numbers


def fuel(module: int) -> int:
    return (module // 3) - 2


def counter_upper(fuel: Iterable[int]) -> int:
    return sum(fuel)


def part1(modules: List[int]) -> int:
    return counter_upper(map(fuel, modules))


def part2(modules: List[int]) -> int:
    return counter_upper(map(add_extra_fuel, modules))


def add_extra_fuel(f: int) -> int:
    total_fuel: int = 0
    f: int = fuel(f)
    while f >= 0:
        total_fuel += f
        #print('>> ', f, total_fuel)
        f = fuel(f)
    return total_fuel

def main() -> None:
    modules: List[int] = get_data()
    p1: int = part1(modules)
    print(f'Part 1 answer {p1}')
    p2: int = part2(modules)
    print(f'Part 2 answer {p2}')

def test() -> None:
    test_modules: List[int] = [14, 1969, 100756]
    m: int
    for m in test_modules:
        print(m, add_extra_fuel(m))


if __name__ == '__main__':
    main()
    #test()

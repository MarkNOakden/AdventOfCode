"""Advent of Code 2021 day 01"""

import pandas as pd
import numpy as np


def part1(df):
    _depths = df['depth']
    next_depths = df['depth'].shift(-1)
    return np.sum(next_depths > _depths)


def part2(df, window_length=3):
    ra_depths = df.rolling(window=window_length).sum()
    return part1(ra_depths)


if __name__ == '__main__':
    depths = pd.read_csv(
        'input.txt',
        header=None,
        names=['depth'],
        dtype=int,
    )

    print('Part1: ', part1(depths))
    print('Part2: ', part2(depths))

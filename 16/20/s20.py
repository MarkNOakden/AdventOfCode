#!/usr/bin/env python2
import pandas as pd
import numpy as np

def first_gap(r):
    i = 1
    ls, le = r[0]
    while r[i][0] <= le + 1:
        ls, le = r[i]
        i += 1
    return le + 1

if __name__ == '__main__':
    fwrules = np.loadtxt('input.txt', delimiter='-', dtype=np.uint32)
    fwrules.sort(axis=0)
    
    print 'Part1: first allowed IP is {}'.format(first_gap(fwrules))

    fwdf = pd.DataFrame(fwrules)
    fwdf['ipcount'] = fwdf[0] - fwdf[1].shift(1) - 1

    allowedIPCount = int(np.sum(fwdf[
        fwdf['ipcount'] > 0
        ]['ipcount'].dropna()))

    print 'Part2: number of allowed IPs is {}'.format(allowedIPCount)
    

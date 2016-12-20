#!/usr/bin/env python2
import pandas as pd
import numpy as np

MAXINT = 4294967295

def first_gap(r):
    i = 1
    ls, le = r[0]
    while r[i][0] <= le + 1:
        if r[i][1] > le:
            le = r[i][1]
        i += 1
    return le + 1

if __name__ == '__main__':
    fwrules = np.loadtxt('input.txt', delimiter='-', dtype=np.uint32)
    fwrules.sort(axis=0)
    
    print 'Part1: (via firstgap() function on numpy array)'
    print '       first allowed IP is {}'.format(first_gap(fwrules))

    fwdf = pd.DataFrame(fwrules, columns=['start', 'end'])
    fwdf['maxEnd'] = fwdf.cummax()['end']
    fwdf['ipcount'] = fwdf['start'] - fwdf['maxEnd'].shift(1) - 1
    fwdf.loc[fwdf['ipcount'] < 0, 'ipcount'] = 0
    fwdf['firstip'] = (fwdf[fwdf['ipcount'] > 0]['start']
                       - fwdf['ipcount'])
    fwdf = fwdf.fillna(0).astype(np.uint32)

    print 'Part1: (via pandas only)'
    print '       first allowed IP is {}'.format(
        fwdf[fwdf['firstip'] > 0]['firstip'].iloc[0])
        
    allowedIPCount = np.sum(fwdf['ipcount'])
    # just in case the last range in the input leaves addresses open
    # above it
    allowedIPCount += MAXINT - fwdf['maxEnd'].iloc[-1]

    print 'Part2: number of allowed IPs is {}'.format(allowedIPCount)
    

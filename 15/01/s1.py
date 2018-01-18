#!/usr/bin/env python2

import sys

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()

fd.close()

# Day 1 first part:-
# ( -> up
# ) -> down
# start at 0, where does he end up

# process it
def the_floor(s):
    UplusD = len(s)
    D = len(s.replace("(",""))
    return UplusD - 2*D

print the_floor(input_data)

# Day 1 second part
# which character position first caused him to enter the basement
# first char of input is #1
# basement is Floor -1

for i in range(1,len(input_data)):
    if the_floor(input_data[0:i]) == -1:
        print "first in the basement at position ",i
        break


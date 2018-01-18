#!/usr/bin/env python2

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()

fd.close()


presents = input_data.split()

def paper(present):
    (l, w, h)=sorted(map(int, present.split('x')))
    return 3*l*w + 2*l*h + 2*w*h


def ribbon(present):
    (l, w, h)=sorted(map(int, present.split('x')))
    return 2*(l+w) + l*w*h

#tests:-
print "test cases - dimensions, paper, ribbon"
print "2x3x4 ",paper('2x3x4'),ribbon('2x3x4')
print "4x3x2 ",paper('4x3x2'),ribbon('4x3x2')
print "1x1x10 ",paper('1x1x10'),ribbon('1x1x10')

print ""
print "paper", sum(map(paper,presents))
print "ribbon", sum(map(ribbon,presents))

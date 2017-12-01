#!/usr/bin/env python2

INITIAL_A = 182

a = INITIAL_A
b = 0
c = 0
d = 0


# cpy a d
d = a
# cpy 14 c
c = 14
#cpy 182 b
#A:
b = 182
# up until 07: jnz c -5
d += c * b

print 'at0:',a,b,c,d
#X:
while True:
    print 'at1:',a, b, c, d
    a = d
    #z:
    while a != 0:
        b = a
        a = 0
        c = 2
        if b != 0:
            b -= 1
            c -= 1
        else:
            b = 2
            #G:
            while True:
                if c == 0:
                    print b
                    break
                else:
                    b -= 1
                    c -= 1
    

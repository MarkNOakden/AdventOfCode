#!/usr/bin/env python2

mfcsam = {"children": 3, \
          "cats": 7, \
          "samoyeds": 2, \
          "pomeranians": 3, \
          "akitas": 0, \
          "vizslas": 0, \
          "goldfish": 5, \
          "trees": 3, \
          "cars": 2, \
          "perfumes": 1}

def f_equal(a, b):
    return a == b

def f_equal_t(t, a, b):
    return f_equal(a, b)

def f_le(a, b):
    return a <= b

def f_gt(a,b):
    return a > b

def f_ge(a,b):
    return a >= b

def f_lt(a, b):
    return a < b

def f_part2(t, a, b):
    if t == 'trees' or t == 'cats':
        return f_gt(a, b)
    elif t == 'pomeranians' or t == 'goldfish':
        return f_lt(a, b)
    else:
        return f_equal(a, b)

class Sue(object):
    def __init__(self, attrs):
        self.attrs = attrs

    def match(self, mfcsam, cmpfunc = f_equal_t):
        out = True
        for i in self.attrs:
            if not cmpfunc(i, self.attrs[i], mfcsam[i]):
                out = False
        return out

    def __str__(self):
        return str(self.attrs)

    def __repr__(self):
        return repr(self.attrs)

if __name__ == '__main__':
    # get the input
    fd = open("input.txt", 'r')
    raw_input_data = fd.read()
    fd.close()
    # parse it
    allSues = {}
    for l in raw_input_data.splitlines():
        sue, sep, data = l.partition(': ')
        attrs = {}
        for item in data.split(','):
            key, value = map(lambda x: x.strip(), item.split(':'))
            attrs[key] = int(value)
        allSues[sue] = Sue(attrs)
    #
    for t, func in [ ('part 1', f_equal_t), \
                     ('part 2', f_part2) ]:
        print t, [(x, allSues[x]) for x in allSues \
                  if allSues[x].match(mfcsam, func)]

    
    
    
    


#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    # Part 1 tests
        
    def test_1(self):
        self.assertEqual(score(test_mix, test_data), 62842880)
        
    def test_2(self):
        self.assertEqual(score(test_mix2, test_data), 0)
 
    def test_3(self):
        self.assertEqual(vscore(test_mix, test_data), [68, 80, 152, 76, 520])

    def test_4(self):
        self.assertEqual(vscore(test_mix2, test_data), [0, 0, 360, 180, 650])

    def test_5(self):
        self.assertEqual(maximise(test_data)[0], 62842880)


# test data
#Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
#Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
       
test_data = { 'Butterscotch': [ -1, -2,  6,  3,  8], \
              'Cinnamon':     [  2,  3, -2, -1,  3] }
test_mix = {'Butterscotch': 44, 'Cinnamon': 56}
test_mix2 = {'Butterscotch': 70, 'Cinnamon': 30}

# real data
#Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
#Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
#Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
#Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8

real_data = { 'Sprinkles':    [ 2,  0, -2,  0,  3], \
              'Butterscotch': [ 0,  5, -3,  0,  3], \
              'Chocolate':    [ 0,  0,  5, -1,  8], \
              'Candy':        [ 0, -1,  0,  5,  8] }


def score_pt1(mix, ingredients):
    sc = 1
    v = vscore(mix, ingredients)
    if 0 in v:
        return 0
    for i in v[0:-1]: # -1 because ignoring calories
        sc *= i
    return sc

def score_pt2(mix, ingredients):
    sc = 1
    v = vscore(mix, ingredients)
    if 0 in v:
        return 0
    if v[-1] != 500:
        return 0
    for i in v[0:-1]: # -1 because ignoring calories
        sc *= i
    return sc

def vscore(mix, ingredients):
    v = [0, 0, 0, 0, 0]
    for i in mix:
        v = [x + mix[i] * y for (x,y) in zip(v, ingredients[i])]
    v = [max(x, 0) for x in v]
    return v

# might be dumb...
def mkMix(items):
    for i in range(0, 101): # 0 to 100
        for j in range(0, 101 - i):
            for k in range(0, 101 - i - j):
                yield dict(zip(items, [i, j, k, 100 - (i+j+k)]))

def maximise(ingredients):
    m = 0
    bestMix = {}
    for mix in mkMix(ingredients.keys()):
        s = score(mix, ingredients)
        if s > m:
            m = s
            bestMix = mix
    return m, bestMix

if __name__ == '__main__':
    score = score_pt1
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    print 'part 1'
    foo=maximise(real_data)
    print 'score is ', foo[0]
    print 'recipe: ', foo[1]

    print 'part 2'
    score = score_pt2
    foo=maximise(real_data)
    print 'score is ', foo[0]
    print 'recipe: ', foo[1]

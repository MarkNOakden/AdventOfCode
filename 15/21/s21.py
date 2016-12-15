#!/usr/bin/env python2
import unittest
from itertools import combinations

# class TestIt(unittest.TestCase):
#     # Part 1 tests
        
#     def test_1(self):
#         self.assertEqual(dist('London', 'Dublin'), 464)
 
#     def test_2(self):
#         self.assertEqual(dist('Dublin', 'London'), 464)

#     def test_3(self):
#         self.assertEqual(shortestPath(locs_test)[0], 605)

#     def test_4(self):
#         self.assertEqual(longestPath(locs_test)[0], 982)
 
        
bossHP = 100
bossDamage = 8
bossArmor = 2

playerHP = 100
playerDamage = 0
playerArmor = 0

class Item(object):
    def __init__(self, l):
        self.name, self.cost, self.damage, self.armour = l

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return repr(self.name)

def choices(l, Nmin, Nmax):
    # generator returning two lists
    for i in range(Nmin, Nmax+1):
        for x in combinations(l, i):
            yield x



    
Weapons = []
#Weapons:    Cost  Damage  Armor
Weapons.append(Item(['Dagger',        8,     4,       0]))
Weapons.append(Item(['Shortsword',   10,     5,       0]))
Weapons.append(Item(['Warhammer',    25,     6,       0]))
Weapons.append(Item(['Longsword',    40,     7,       0]))
Weapons.append(Item(['Greataxe',     74,     8,       0]))

Armor = []
#Armor:      Cost  Damage  Armor
Armor.append(Item(['Leather',      13,     0,       1]))
Armor.append(Item(['Chainmail',    31,     0,       2]))
Armor.append(Item(['Splintmail',   53,     0,       3]))
Armor.append(Item(['Bandedmail',   75,     0,       4]))
Armor.append(Item(['Platemail',   102,     0,       5]))

Rings = []
#Rings:      Cost  Damage  Armor
Rings.append(Item(['Damage +1',    25,     1,       0]))
Rings.append(Item(['Damage +2',    50,     2,       0]))
Rings.append(Item(['Damage +3',   100,     3,       0]))
Rings.append(Item(['Defense +1',   20,     0,       1]))
Rings.append(Item(['Defense +2',   40,     0,       2]))
Rings.append(Item(['Defense +3',   80,     0,       3]))


if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    #unittest.TextTestRunner(verbosity=2).run(suite)

    mincost = None
    bestinv = []
    maxspend = None
    worstinv = []
    for w in choices(Weapons, 1, 1):
        for a in choices(Armor, 0, 1):
            for r in choices(Rings, 0, 2):
                inventory = list(w) + list(a) + list(r)
                cost = sum(x.cost for x in inventory)
                damage = sum(x.damage for x in inventory)
                ac = sum(x.armour for x in inventory)
                if max(1, (damage - bossArmor)) >= max(1, (bossDamage - ac)):
                    if mincost is None or cost < mincost:
                        mincost = cost
                        bestinv = inventory
                        #print 'better'
                        #print 'damage',damage,'ac',ac
                        #print 'inv',inventory
                        #print 'cost',cost
                if max(1, (damage - bossArmor)) < max(1, (bossDamage - ac)):
                    if maxspend is None or cost > maxspend:
                        maxspend = cost
                        worstinv = inventory
                        #print 'worse'
                        #print 'damage',damage,'ac',ac
                        #print 'inv',inventory
                        #print 'cost',cost
    
    
    print mincost, bestinv
    print maxspend, worstinv
    
    


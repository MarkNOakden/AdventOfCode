#!/usr/bin/env python2
import unittest
import copy
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


bossHP = 51
bossDamage = 9
debug = False

part2 = True

def dprint(depth, msg):
    if debug: print '..'*depth + ' <' + str(depth) + '> ' + msg

# spells available
# name, cost, turns, damage, heal, acbonus. recharge
# 0 turns ==> instant effect
spelllist = [ ['Magic Missile',  53, 0, 4, 0, 0,   0], \
              ['Drain',          73, 0, 2, 2, 0,   0], \
              ['Shield',        113, 6, 0, 0, 7,   0], \
              ['Poison',        173, 6, 3, 0, 0,   0], \
              ['Recharge',      229, 5, 0, 0, 0, 101] ]

allSpells = {}
for i in spelllist:
    name = i[0]
    props = {'cost':     i[1], \
             'turns':    i[2], \
             'damage':   i[3], \
             'heal':     i[4], \
             'acbonus':  i[5], \
             'recharge': i[6] }
    allSpells[name] = props

class ActiveSpell(object):

    def __init__(self, name):
        self.name = name
        self.timer = allSpells[name]['turns']

    def __str__(self):
        return 'ActiveSpell: ' + self.name + ' Timer is ' +  str(self.timer)

    __repr__ = __str__

class Node(object):
    # class-wide Node.minSpentMana variable
    minSpentMana = None
    # each node represents a player turn. the children are
    # the nodes corresponding to the different spells available
    # to the player at each turn
    def __init__(self, playerHP=50, mana=500, bossHP=51, \
                 active=None, turn='player', spentMana=0, history=None, depth=0):
        self.playerHP = playerHP
        self.turn = turn
        self.bossHP = bossHP
        self.mana = mana
        self.AC = 0
        self.spentMana = spentMana
        self.depth = depth
        self.next = []
        if active is None:
            self.active = []
        else:
            self.active = active
        if history is None:
            self.history = []
        else:
            self.history = history

    def doTurn(self):
        dprint(self.depth, '### ' + self.turn + ' Turn')
        dprint(self.depth, 'playerHP: ' + str(self.playerHP) + \
               ' mana: ' + str(self.mana) + ' bossHP: ' + str(self.bossHP))
        dprint(self.depth, 'spentMana: ' + str(self.spentMana) + \
               ' AC: ' + str(self.AC))
        dprint(self.depth, 'history: ' + str(self.history))
        dprint(self.depth, 'active: ' + str(self.active))
        if self.turn == 'player':
            self.doPlayerTurn()
        else:
            self.doBossTurn()
        
    def doPlayerTurn(self):

        ###############
        # Player Turn #
        ###############
        if part2:
            self.playerHP -= 1
            if self.bossWins():
                dprint(self.depth, 'boss wins')
                return
        self.AC = 0
        for sp in self.active:
            self.applyActiveEffect(sp)
        self.cleanActive() # delete spells whose timer is spent
        dprint(self.depth, 'After spell effects, playerHP=' + str(self.playerHP) \
               + ' mana is ' + str(self.mana) + ' AC ' + str(self.AC) \
               + ' bossHP ' + str(self.bossHP))
        if self.playerWins():
            if Node.minSpentMana is None or \
              self.spentMana < Node.minSpentMana:
                Node.minSpentMana = self.spentMana
            # boss is dead, return now
            dprint(self.depth, '>>>>>>>>player wins - mana ' + str(self.spentMana))
            dprint(self.depth, 'history' + str(self.history))
            dprint(self.depth, 'minSepntMana' + str(Node.minSpentMana))
            return
        avail = self.availableSpells()
        if len(avail) == 0:
            dprint(self.depth, 'player loses no spells available')
            return
        for sp in avail:
            aSpell = ActiveSpell(sp)
            cost = allSpells[sp]['cost']
            newhist = [x for x in self.history]
            newhist.append(sp)
            dprint(self.depth, 'player casts ' + sp)
            activeNew = copy.deepcopy(self.active)
            # if aSpell.timer == 0:
            #     # immediate spell - apply the effect now and
            #     # test if player wins
            #     self.applyImmediateEffect(aSpell)
            #     if self.playerWins():
            #         if Node.minSpentMana is None or \
            #           self.spentMana + cost < Node.minSpentMana:
            #             Node.minSpentMana = self.spentMana + cost
            #         # boss is dead, return now
            #         dprint(self.depth, '>>>>>>>>player wins - mana '+ str(self.spentMana + cost))
            #         dprint(self.depth, 'history ' + str(newhist))
            #         dprint(self.depth, 'minSepntMana ' + str(Node.minSpentMana))
            #         return
            # else:
            #     # multi-turn effect spell - append to active list
            #     #spawn a new node for Boss Turn
            #     activeNew.append(aSpell)
            activeNew.append(aSpell)
            theNode = Node(playerHP = self.playerHP, \
                                  mana = self.mana - cost, \
                                  bossHP = self.bossHP, \
                                  active = activeNew, \
                                  spentMana = self.spentMana + cost, \
                                  history = newhist, \
                                  turn = 'boss', \
                                  depth = self.depth + 1)
            self.next.append(theNode)
            theNode.doTurn()


    def doBossTurn(self):
        self.AC = 0
        for sp in self.active:
            self.applyActiveEffect(sp)
        self.cleanActive() # delete spells whose timer is spent
        dprint(self.depth, 'After spell effects, playerHP=' + str(self.playerHP) \
               + ' mana is ' + str(self.mana) + ' AC ' + str(self.AC) \
               + ' bossHP ' + str(self.bossHP))
        if self.playerWins():
            if Node.minSpentMana is None or \
              self.spentMana < Node.minSpentMana:
                Node.minSpentMana = self.spentMana
            # boss is dead, return now
            dprint(self.depth, '>>>>>>>>player wins - mana ' + str(self.spentMana))
            dprint(self.depth, 'history ' + str(self.history))
            dprint(self.depth, 'Node.minSpentMana ' + str(Node.minSpentMana))
            return
        dprint(self.depth, 'Boss does damage: ' + str(self.bossDamage()))
        self.playerHP -= self.bossDamage()
        dprint(self.depth, 'playerHP is now ' + str(self.playerHP))
        if self.playerHP <= 0:
            # boss wins - return now - no further nodes
            dprint(self.depth, 'boss wins: bossHP = ' + str(self.bossHP))
            return
        theNode = Node(playerHP = self.playerHP, \
                         mana = self.mana, \
                         bossHP = self.bossHP, \
                         active = copy.deepcopy(self.active), \
                         spentMana = self.spentMana, \
                         history = [x for x in self.history], \
                         turn = 'player', \
                         depth = self.depth + 1)
        self.next = [theNode]
        theNode.doTurn()
            
    def bossDamage(self):
        return max(1, bossDamage - self.AC)

    def availableSpells(self):
        dprint(self.depth, 'checking available spells. mana=' + str(self.mana))
        avail = []
        for i in allSpells:
            #dprint(self.depth, 'checking ' + i)
            if allSpells[i]['cost'] >= self.mana:
                #dprint(self.depth, ' |_ can\'t afford')
                # can't afford the spell
                continue
            elif Node.minSpentMana is not None and allSpells[i]['cost'] + self.spentMana > Node.minSpentMana:
                #dprint(self.depth, ' |_ #####bust minimum')
                # not worth checking already worse than the best already found
                continue
            elif i in [x.name for x in self.active]:
                #dprint(self.depth, ' |_ already active')
                # already active
                continue
            else:
                avail.append(i)
        return avail
        
    def applyActiveEffect(self, sp):
        idx = self.active.index(sp)
        self.active[idx].timer -= 1
        dprint(self.depth, 'applying ffect of ' + sp.name \
               + ' timer is now ' + str(self.active[idx].timer))
        # do the effects for each spell
        self.applyImmediateEffect(sp)

    def applyImmediateEffect(self, sp):
        s = allSpells[sp.name]
        self.mana += s['recharge']
        self.bossHP -= s['damage']
        self.playerHP += s['heal']
        self.AC += s['acbonus']

    def cleanActive(self):
        for i in self.active:
            if i.timer <= 0:
                dprint(self.depth, i.name + ' wears off')
        self.active = [x for x in self.active if x.timer > 0]

    def playerWins(self):
        return self.bossHP <= 0

    def bossWins(self):
        return self.playerHP <= 0

    def __str__(self):
        s = 'Node: playerHP=' + str(self.playerHP)
        s += ' mana=' + str(self.mana) + ' bossHP=' + str(self.bossHP)
        s += ' children=' + str(self.next)
        s += ' Node.minSpentMana=' + str(Node.minSpentMana)
        return s

    __repr__ = __str__

        
# need to apply some form of minimax to the following
# (when player wins, check spent mana against minimum spent mana
# - if mana spent was less than minimum, update minimum.
# when casting spells test if any spells already take one over the
# best minimum already found and don't consider those nodes)
    
# for each node (player turn + subsequent boss turn), do the following

# apply effects of all active spells
# test if boss HP <= 0
#   -> if True player wins
#      check on minimum mana solution found so far
#   
# decrease active spell timers
# delete any spells with counter <= 0
# determine available spells
#   -> if none available -> player loses
#
# apply boss damage
# test if player HP <= 0
#   -> if True player loses
#
# create child nodes (recursive call?) for each available spell to cast
# process each node - ignore any which already take the spent mana
# above the best so far found




if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    Tree = Node()
    Tree.doTurn()
    print 'minspent =', Node.minSpentMana
    
    
    


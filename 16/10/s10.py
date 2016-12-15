#!/usr/bin/env python2
import unittest, re

test_data = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
'''

with open('input.txt', 'r') as fd:
    input_data = fd.read()


class Output(object):
    def __init__(self, outputID):
        self.id = outputID
        self.chips = []

    def receiveChip(self, chip):
        self.chips.append(chip)

    def __str__(self):
        return 'Output {} - chips: {}'.format(
            self.id,
            self.chips)

    __repr__ = __str__


class Bot(object):
    def __init__(self, botID):
        self.id = botID
        self.chips = []
        self.low = None
        self.high = None
        self.watchFor = [17, 61]

    def receiveChip(self, chip):
        self.chips.append(chip)
        if len(self.chips) == 2:
            self.chips = sorted(self.chips)
            if self.chips == self.watchFor:
                print 'I compared {}: {}'.format(self.watchFor, self.id)
            self.low.receiveChip(self.chips[0])
            self.high.receiveChip(self.chips[1])
            self.chips = []
            

    def setLow(self, low):
        self.low = low

    def setHigh(self, high):
        self.high = high

    def __str__(self):
        return 'Bot {} - chips: {} low: {} high: {}'.format(
            self.id,
            self.chips,
            self.low,
            self.high)

    __repr__ = __str__

if __name__ == '__main__':

    bots = {}
    outputs = {}

    botres = 'bot ([0-9]+) gives low to (bot|output) ([0-9]+)'
    botres += ' and high to (bot|output) ([0-9]+)'

    botre = re.compile(botres)

    valres = 'value ([0-9]+) goes to bot ([0-9]+)'

    valre = re.compile(valres)
    
    # pass 1 set up bots and outputs
    for i in input_data.splitlines():
        if i.startswith('bot '):
            match = botre.match(i)
            
            botnum = int(match.group(1))
            lowType = match.group(2)
            low = int(match.group(3))
            highType = match.group(4)
            high = int(match.group(5))

            if lowType == 'bot':
                if low in bots:
                    lowObj = bots[low]
                else:
                    lowObj = Bot(low)
                    bots[low] = lowObj
            elif lowType == 'output':
                if low in outputs:
                    lowObj = outputs[low]
                else:
                    lowObj = Output(low)
                    outputs[low] = lowObj
            else:
                raise ValueError('type {} was neither \'bot\' nor \'output\''.format(lowType))
                
            if highType == 'bot':
                if high in bots:
                    highObj = bots[high]
                else:
                    highObj = Bot(high)
                    bots[high] = highObj
            elif highType == 'output':
                if high in outputs:
                    highObj = outputs[high]
                else:
                    highObj = Output(high)
                    outputs[high] = highObj
            else:
                raise ValueError('type {} was neither \'bot\' nor \'output\''.format(highType))
                
            if botnum in bots:
                thisBot = bots[botnum]
            else:
                thisBot = Bot(botnum)
                bots[botnum] = thisBot

            thisBot.setLow(lowObj)
            thisBot.setHigh(highObj)
            
    # pass 1 pass in values
    for i in input_data.splitlines():
        if i.startswith('value '):
            match = valre.match(i)
            value  = int(match.group(1))
            botnum = int(match.group(2))

            bots[botnum].receiveChip(value)

    prod = 1
    for i in range(3):
        print 'Output {}: {}'.format(i, outputs[i].chips[0])
        prod *= outputs[i].chips[0]

    print 'Product is {}'.format(prod)
    
            


    

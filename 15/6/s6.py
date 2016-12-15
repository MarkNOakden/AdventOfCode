#!/usr/bin/env python2

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

class lightArray(object):
    def __init__(self, width = 1000, height = 1000):
        self.l = [width * [0] for i in range(height)]

    def __str__(self):
        out = ''
        for i in self.l:
            for j in i:
                out += str(j)
            out += '\n'
        return out

    __repr__ = __str__

    def turnOn(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.l[x][y] = 1
    

    def turnOff(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.l[x][y] = 0
    

    def toggle(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.l[x][y] = 1 - self.l[x][y]
    
    def lightsLit(self):
        return sum([sum(i) for i in self.l])

class lightArray2(object):
    def __init__(self, width = 1000, height = 1000):
        self.l = [width * [0] for i in range(height)]

    def __str__(self):
        out = ''
        for i in self.l:
            for j in i:
                out += str(j)
            out += '\n'
        return out

    __repr__ = __str__

    def turnOn(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.l[x][y] += 1
    

    def turnOff(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if self.l[x][y] > 0:
                    self.l[x][y] -= 1
    

    def toggle(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.l[x][y] += 2
    
    def lightsLit(self):
        return sum([sum(i) for i in self.l])

    


if __name__ == '__main__':
    myDecorations = lightArray(1000, 1000)
    myDecorations2 = lightArray2(1000, 1000)

    for santaString in input_data.splitlines():
        rest, sep, x2y2 = santaString.partition(' through ')
        rest = rest.replace('turn ', '')
        operation, sep, x1y1 = rest.partition(' ')
        x1, y1 = map(int, x1y1.split(','))
        x2, y2 = map(int, x2y2.split(','))
        if operation == 'on':
            myDecorations.turnOn(x1, y1, x2, y2)
            myDecorations2.turnOn(x1, y1, x2, y2)
        elif operation == 'off':
            myDecorations.turnOff(x1, y1, x2, y2)
            myDecorations2.turnOff(x1, y1, x2, y2)
        elif operation == 'toggle':
            myDecorations.toggle(x1, y1, x2, y2)
            myDecorations2.toggle(x1, y1, x2, y2)
    print "Part 1: number of lights lit is ", \
        myDecorations.lightsLit()
    print "Part 2: total brightness is ", \
        myDecorations2.lightsLit()

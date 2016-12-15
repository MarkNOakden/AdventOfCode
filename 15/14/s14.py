#!/usr/bin/env python2

fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

class Reindeer(object):
    def __init__(self, speed, time, rest):
        self.speed = speed
        self.time = time
        self.rest = rest

    def distance(self, sec):
        whole_cycles = sec/(self.time + self.rest)
        remainder = sec - whole_cycles * (self.time + self.rest)
        additional = min(remainder, self.time)
        return self.speed * (whole_cycles * self.time + additional)

competitors = {}
for l in input_data.splitlines():
    name, sep, tail = l.partition(' can fly ')
    speed, sep, tail = tail.partition(' km/s for ')
    speed = int(speed)
    time, sep, tail = tail.partition(' seconds, but then must rest for ')
    time = int(time)
    rest = int(tail.split()[0])
    competitors[name] = Reindeer(speed, time, rest)

s = 0
for i in competitors:
    d = competitors[i].distance(2503)
    print i, d
    if d > s:
        s = d


print 'Part 1 answer: ', s


scores = {}
for i in competitors:
    scores[i] = 0

for i in range(2503):
    sec = i + 1

    roundResults = {}
    for j in competitors:
        d = competitors[j].distance(sec)
        if d in roundResults:
            roundResults[d].append(j)
        else:
            roundResults[d] = [j]

    highest = max(roundResults.keys())
    for j in roundResults[highest]:
        scores[j] += 1

for i in sorted(scores.items(), key=lambda(k, v): v):
    print i[0], i[1]


winner, score = sorted(scores.items(), key=lambda(k, v): v)[-1]

print ""
print "The winning score is " + str(score) + " by " + winner



    



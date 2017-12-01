#!/usr/bin/env python2
#
# a new attempt at day 19 part 2 from 2015 written 2016-12-16
# now that I know how to code a breadth first search
#
from collections import deque
import re

def getDepthByBFS(start):
    depth = 0
    queue = deque()
    queue.append((depth, start))
    visited = set(start)
    lastdepth = -1
    while queue:
        depth, node = queue.popleft()
        if depth > lastdepth:
            print depth
            lastdepth = depth
        if isFinalPos(node):
            return depth

        for childpos in getChildren(node):
            if posHash(childpos) not in visited:
                queue.append((depth + 1, childpos))
                visited.add(posHash(childpos))

def getDepthByDFS(start):
    depth = 0
    queue = list()
    queue.append((depth, start))
    maxdepth = 0
    nodes = 0
    while queue:
        depth, node = queue.pop()
        nodes += 1
        if depth > maxdepth:
            maxdepth = depth
        if nodes % 100000 == 0:
            print 'max depth: {}, nodes {}, stacklen {}'.format(
                maxdepth,
                nodes,
                len(queue))
        if isFinalPos(node):
            return depth

        for childpos in getChildren(node):
            queue.append((depth + 1, childpos))
                
    return None

def isFinalPos(node):
    return node == 'e'

def getChildren(node):
    children = []
    for match in subRE.finditer(node):
        matched = match.group(0)
        s, e = match.start(), match.end()
        candidate = node[:s] + subdict[matched] + node[e:]
        children.append(candidate)
    children.sort(key=lambda a: (-len(a),
                                 len(subRE.findall(candidate))))
    return children

def posHash(node):
    return node
    

if __name__ == '__main__':
    # get the input
    fd = open("input.txt", 'r')
    input_data = fd.read()
    fd.close()

    subs = []
    for l in input_data.splitlines():
        atomIn, sep, atomOut = l.partition(' => ')
        if sep == '':
            if atomIn != '':
                mol = atomIn
        else:
            subs.append((atomOut, atomIn))

    # favour longer substitutions
    subs.sort(key=lambda a: len(a[0]))

    pat = str('(' + '|'.join(a[0] for a in subs) + ')')
    subRE = re.compile(pat)
    
    subdict = dict(subs)

    #print getDepthByDFS(mol)
    depth = 0
    while mol != 'e':
        mol, n = subRE.subn(lambda m: subdict[m.group(0)], mol)
        depth += n

    print n

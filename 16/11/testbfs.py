#!/usr/bin/env python2
from collections import deque

def getDepthByBFS(start):
    depth = 0
    queue = deque()
    queue.append((depth, start))
    visited = set(start)

    while queue:
        depth, node = queue.popleft()
        print node

        if isFinalPos(node):
            return depth

        nextList = getChildren(node)
        if nextList is not None:
            for childpos in nextList:
                if childpos not in visited:
                    queue.append((depth + 1, childpos))
                    visited.add(childpos)
                
    return None

def getChildren(node):
    if node == 'a':
        return ['b', 'c']
    elif node == 'b':
        return ['d', 'e', 'f']
    elif node == 'c':
        return ['g']
    elif node == 'd':
        return ['h', 'i']
    else:
        return []

def isFinalPos(node):
    return node == 'i'

#          a
#      b         c
#   d   e  f    g
#  h  i

print getDepthByBFS('a')

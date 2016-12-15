#!/usr/bin/env python2
import unittest
# optimised version
class TestIt(unittest.TestCase):
    # Part 1 tests
      
    def test_1(self):
        self.assertEqual(QE([11, 9]), 99)

    def test_2(self):
        self.assertEqual(QE([10, 9, 1]), 90)

def minParcels(l, N):
    if sum(l) % N != 0:
        print 'can\'t divide into', N
        exit()
    target = sum(l) / N
    for i in range(len(l)):
        if sum(l[:i]) >= target: return i

def QE(l):
    qe = 1
    for i in l:
        qe *= i
    return qe

def groups(size, L):
    # all subgroups of L with length size
    for i in range(len(L)):
        out = []
        if size == 1:
            out.append(L[i])
            yield out
        else:
            newL = L[:i] + L[i+1:]
            for j in groups(size - 1, newL):
                out = [L[i]] + j
                yield out

def groups2(size, L):
    # all subgroups of L with length size
    for i in range(len(L)):
        out = []
        if size == 1:
            out.append(L[i])
            yield out
        else:
            newL = [j for j in L[:i] + L[i+1:] if j <= L[i]]
            for j in groups2(size - 1, newL):
                out = [L[i]] + j
                yield out


    
def groups_with_sum(size, L, N):
    for i in groups2(size, L):
        if sum(i) == N:
            yield i

def exists_group_with_sum(size, L, N):
    for i in groups2(size, L):
        if sum(i) == N:
            return 1
    return 0

def best_QE_all(L, part):
    Nbags = 2 + part
    MIN = minParcels(L, Nbags)
    MAX = len(L) / Nbags # round down
    TARGET = sum(L) / Nbags
    bestQE = {}
    bestbag0 = {}

    for N in range(MIN, MAX+1):
        print MIN, N, MAX
        bestQE[N] = None
        for bag0 in groups_with_sum(N, L, TARGET):
            QEbag0 = QE(bag0)
            newL = [x for x in L]
            for y in bag0:
                newL.remove(y)
            # just need to know now whether there is a sublist of newL
            # that sums to TARGET.  if so, check the QE of bag0
            subMAX = len(newL) / (Nbags - 1)
            for i in range(MIN, subMAX+1):
                print '  ',MIN, i, subMAX
                if part == 2:
                    foundpart = False
                    for bag1 in groups_with_sum(N, newL, TARGET):
                        if foundpart: break
                        newnewL = [x for x in newL]
                        for y in bag1:
                            newnewL.remove(y)
                        subsubMAX = len(newnewL) / (Nbags - 2)
                        for j in range(MIN, subsubMAX + 1):
                            #print '    ',MIN,j,subsubMAX
                            l = exists_group_with_sum(j, newnewL, TARGET)
                            if l != 0:
                                if bestQE[N] is None or QEbag0 < bestQE[N]:
                                    bestQE[N] = QEbag0
                                    bestbag0[N] = bag0
                                foundpart = True
                                break
                else:
                    l = exists_group_with_sum(i, newL, TARGET)
                    if l != 0:
                        if bestQE[N] is None or QEbag0 < bestQE[N]:
                            bestQE[N] = QEbag0
                            bestbag0[N] = bag0
        # if bestQE[N} is not None, we can return now!
        if bestQE[N] is not None:
                return bestQE, bestbag0
    return bestQE, bestbag0
                    
if __name__ == '__main__':
    # test input
    #fd = open("test.txt", 'r')
    #test_data = fd.read()
    #fd.close()

    test_data = range(1, 6)
    test_data += range(7, 12)
    test_data.sort()
    test_data.reverse()

    print best_QE_all(test_data, 1)
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    
    # get the input
    fd = open("input.txt", 'r')
    raw_input_data = fd.read()
    fd.close()

    input_data = [int(x) for x in raw_input_data.splitlines()]
    input_data.sort()
    input_data.reverse()

    print best_QE_all(input_data, 1)

    print best_QE_all(input_data, 2)
    
    

    
    
    


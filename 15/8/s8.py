#!/usr/bin/env python2
import unittest

class TestIt(unittest.TestCase):
    # Part 1 tests
        
    def test_1(self):
        self.assertEqual(total_wastage(test_data), 12)
        
    #def test_2(self):
    #    self.assertEqual(self.c.nodeValue('e', 0), '507')
        
    #def test_3(self):
    #    self.assertEqual(self.c.nodeValue('f', 0), '492')
        
    #def test_4(self):
    #    self.assertEqual(self.c.nodeValue('g', 0), '114')
        

# test input
fd = open("test.txt", 'r')
test_data = fd.read()
fd.close()

# get the input
fd = open("input.txt", 'r')
input_data = fd.read()
fd.close()

def wastage(escapedStr):
    return len(escapedStr) - len(inMemory(escapedStr))

def inMemory(escapedStr):
    #print "eS: /"+escapedStr+"/"
    # strip double quotes
    escapedStr = escapedStr[1:-1]
    #print "eS: without quotes length:",len(escapedStr)
    #walk the string so we don't do double substitutions
    inMemoryStr = ''
    workingOn = ''
    while escapedStr:
        workingOn += escapedStr[0]
        escapedStr = escapedStr[1:]
        translatedStr = translateStr(workingOn)
        if translatedStr is not None:
            inMemoryStr += translatedStr
            workingOn = ''
        elif not '\\' in workingOn:
            inMemoryStr += workingOn
            workingOn = ''
    return inMemoryStr

def translateStr(chunk):
    #print '  translateStr(\''+chunk+'\') len = '+str(len(chunk))
    if chunk == '\\\\': # two backslashes
        return '\\' # one backslash
    elif chunk == '\\"':
        return '"'
    elif chunk[0] == '\\' and len(chunk) == 4:
        hex = chunk[2:4]
        #print 'hex '+hex
        return '_'
    else:
        #print 'not matched yet: /'+chunk+'/'
        return None
    #
    
def total_wastage(data):
    w = 0
    for l in data.splitlines():
        w += wastage(l)
    return w

#for l in test_data.splitlines():
#    foo=inMemory(l)
#    print l+' ; '+str(len(l))+' ; /'+foo+'/ '+str(len(foo))
                      
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print "Part 1 - total wastage = "+str(total_wastage(input_data))
    


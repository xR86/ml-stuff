import sys
import re
import numpy as np
#import parser as ps

if len(sys.argv) > 1:
    #print sys.argv[1]
    f = open('input/'+sys.argv[1], 'r')
else:
    f = open('input.txt', 'r')

pattern = re.compile(r'(?P<a>(-?\d+))x(?P<b>([+-]\d+))y(?P<c>([+-]\d+))(\=)(?P<r>[0-9]+)')
#pattern = re.compile(r'(?P<a>(-?\d+/))x(?P<b>([+-]\d+/))y(?P<c>([+-]\d+/))(\=)(?P<r>[0-9]+)')

matrixA = np.array([])
matrixB = np.array([])
"""
for line in f:
    #line = f.readline()
    #newLine = ps.expr(line).compile()
    #match = pattern.match(line) #or findall
    match = re.search(pattern, line)#.groups()
    print match, type(match)
    print pattern, type(pattern)
    
    if match:
        a = int(match.group('a'))
        b = int(match.group('b'))
        c = int(match.group('c'))
        newRow = [a, b, c]
        matrixA = np.concatenate(matrixA, newRow)    
    
        r = int(match.group('r'))
        newRow = [r]
        matrixB = np.concatenate(matrixB, newRow)
    else:
        raise Exception('Pattern not matched')
"""

#print 'Here we have matrixA:\n', matrixA
matrixA = np.array([[2, 3, 6], [0, 4, 2], [1, 3, 5]])
matrixB = np.array([[2], [3], [1]])

print 'Here we have matrixA:\n', matrixA
print 'Here we have matrixB:\n', matrixB

detA = np.linalg.det(matrixA)

if detA == 0:
    print 'Determinant is 0. Program will stop'
    quit()

matrixAinv = np.linalg.inv(matrixA)
print '---', 'Inverse matrix is: '
print matrixAinv
checkInv = np.allclose(np.dot(matrixA, matrixAinv), np.eye(3))
print "Is matrixAinv ok ?", checkInv

#x = np.linalg.solve(a, b, c)

#Check that the solution is correct:
#np.allclose(np.dot(a, x), b)

#https://open.kattis.com/problems/r2

import sys
#for line in sys.stdin:
#with open('input.txt') as f:
    #data = f.read()
#lines = data.split('\n')

for line in sys.stdin:
    r2 = int()
    r1,s = map(int, line.strip().split(' '))
    r2 = ((s * 2) - r1)
    print(r2)
    exit(0)

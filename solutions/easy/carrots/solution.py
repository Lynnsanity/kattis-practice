#https://open.kattis.com/problems/carrots

#n is equal to the number of contestants

#p represents huffle-puff problems solved

import sys

for line in sys.stdin:
    np = line.split()
    n = int(np[0])
    p = int(np[1])
    sys.stdin.read()
    sys.stdin.read()
print(abs(p))

#shorter method learned
import sys
for line in sys.stdin:
    print(line.split(' ')[1].strip())
    exit(0)

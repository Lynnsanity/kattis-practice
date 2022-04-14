#https://open.kattis.com/problems/twostones

import sys

for line in sys.stdin:
    i = int(line)
    if (i%2) == 0:
        print("Bob")
    else:
        print("Alice")
exit(0)

#shorter method:

from sys import stdin; print("Bob" if ((int(list(stdin)[0]) % 2)==0) else "Alice")


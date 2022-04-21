#https://open.kattis.com/problems/triarea
#Computing area of triangle
import sys

for line in sys.stdin:
    hb = line.split()
    h = int(hb[0])
    b = int(hb[1])
    a = (h * b)/2
    print(a)

exit(0)


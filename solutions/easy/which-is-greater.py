#https://open.kattis.com/problems/whichisgreater
import sys

for line in sys.stdin:
    ab = line.split()
    a = int(ab[0])
    b = int(ab[1])
    sys.stdin.read()

if a > b: 
    print("1")
else:
    print("0")

exit(0)

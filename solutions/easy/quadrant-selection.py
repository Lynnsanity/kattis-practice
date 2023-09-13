#https://open.kattis.com/problems/quadrant
import sys

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
else:
    pass
if x < 0 and y > 0:
    print("2")
else:
    pass
if x < 0 and y < 0:
    print("3")
else:
    pass
if x > 0 and y < 0:
    print("4")
else:
    pass

exit(0)


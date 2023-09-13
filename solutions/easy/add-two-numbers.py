#https://open.kattis.com/problems/addtwonumbers
import sys
from sys import stdin

line = input()

a, b = line.split()

num1 = int(a)
num2 = int(b)

c = num1 + num2

sum = int(c)

print(sum)

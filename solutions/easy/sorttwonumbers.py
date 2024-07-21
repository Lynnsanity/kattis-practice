a, b = input().split()

a = int(a)
b = int(b)

list = []

list.append(a)
list.append(b)

list.sort()

print(' '.join(map(str, list)))

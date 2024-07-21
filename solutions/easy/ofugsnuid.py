n = int(input())

num_list = []
for x in range(n):
    x = int(input())
    num_list.append(x)

print('\n'.join(map(str, num_list[::-1])))


names = str(input())

name_list = names.split('-')

initial_list = []
for name in name_list:
    initial = name[0]
    initial_list.append(initial)

x = ''.join(initial_list)
print(x)

days = int(input())

degrees_on_days = input()

neg_degrees_list = []

counter = 0
for x in degrees_on_days.split():
    if int(x) < 0:
        neg_degrees_list.append(x)

for x in neg_degrees_list:
    if x:
        counter += 1

print(counter)

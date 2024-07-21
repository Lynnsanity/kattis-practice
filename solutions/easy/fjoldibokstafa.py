string = input()

counter = 0
for x in string:
    if x.isalpha():
        counter += 1
    else:
        continue

print(counter)

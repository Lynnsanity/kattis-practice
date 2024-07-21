rows, columns = input().split()

rows = int(rows)
columns = int(columns)

found_letters = []
for x in range(rows):
    line = input()
    for character in line:
        if character == ".":
            pass
        else:
            found_letters.append(character)
print(''.join(map(str, found_letters)))

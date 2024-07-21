number_of_lines = int(input())

counter = 1
for x in range(number_of_lines):
    word = str(input())
    if counter % 2 != 0:
        print(word)
    counter += 1

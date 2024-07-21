initial_word = input()
final_word = input()

counter = 1
for x, i in zip(initial_word, final_word):
    if x != i:
        counter += 1
print(counter)


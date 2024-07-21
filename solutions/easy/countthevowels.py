line = input()

vowels = ["a", "e", "i", "o", "u"]
counter = 0
for character in line:
    if character.lower() in vowels:
        counter += 1

print(counter)

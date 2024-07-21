string = input()


def checker(string):
    vowels_counter = 0
    vowels = ["a", "e", "i", "o", "u"]
    for x in string:
        if x in vowels:
            vowels_counter += 1
    return vowels_counter

def checker_with_y(string):
    vowels_counter_with_y = 0
    vowels_with_y = ["a", "e", "i", "o", "u", "y"]
    for x in string:
        if x in vowels_with_y:
            vowels_counter_with_y += 1
    return vowels_counter_with_y

print(checker(string), checker_with_y(string))



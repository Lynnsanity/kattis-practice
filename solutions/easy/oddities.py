test_cases = int(input())
for x in range(test_cases):
    x = int(input())
    if x == 0 or x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

beer = int(input())
lemonade = int(input())

if lemonade == 0 or beer == 0:
    print("0")
else:
    min_shandies = min(beer, lemonade) * 2
    print(min_shandies)


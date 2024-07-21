item_count = int(input())

my_items = []
for x in range(item_count):
    item = input()
    my_items.append(item)

phone = False
wallet = False
keys = False

for x in my_items:
    if x == "phone":
        phone = True
    if x == "wallet":
        wallet = True
    if x == "keys":
        keys = True

if phone and wallet and keys:
    print("ready")
else:
    if not keys:
        print("keys")
    if not phone:
        print("phone")
    if not wallet:
        print("wallet")



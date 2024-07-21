phone_number = input()

route = "555"

prefix = phone_number[:3]

if route in prefix:
    print("1")
else:
    print("0")

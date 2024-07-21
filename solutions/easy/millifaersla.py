monnei = int(input())
fjee = int(input())
dolladolla = int(input())

mylist = []
mylist.append(monnei)
mylist.append(fjee)
mylist.append(dolladolla)

sorted_numbers = sorted(mylist)

lowest_number = sorted_numbers[0]

if lowest_number == monnei:
    print("Monnei")
elif lowest_number == fjee:
    print("Fjee")
else:
    print("Dolladollabilljoll")



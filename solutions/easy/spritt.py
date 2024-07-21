classrooms, bottles = input().split()

classrooms = int(classrooms)
bottles = int(bottles)

bottle_count = 0
for x in range(classrooms):
    needed_bottles = int(input())
    bottle_count += needed_bottles

if bottle_count <= bottles:
    print("Jebb")
else:
    print("Neibb")



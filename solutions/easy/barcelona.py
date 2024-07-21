bags_and_position = str(input())

bag_line = str(input())

bags, position = bags_and_position.split()

new_bag_line = []

for x in bag_line.split(" "):
    new_bag_line.append(x)

for x in new_bag_line:
    if x == position:
        index_number = new_bag_line.index(x)
        actual_position = int(index_number) + 1
        if actual_position == 1:
            print("fyrst")
        elif actual_position == 2:
            print("naestfyrst")
        else:
            print(f"{actual_position} fyrst")
    else:
        pass






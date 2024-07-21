current_set = input()

current_set_list = []

for x in current_set.split(" "):
    current_set_list.append(x)

desired_set_list = ['1', '1', '2', '2', '2', '8']

required_set_list = []

for x in range(6):
    current_num = int(current_set_list[x])
    desired_num = int(desired_set_list[x])
    
    if current_num != desired_num:
        num_needed = desired_num - current_num
        required_set_list.append(num_needed)
    else:
        num_needed = 0
        required_set_list.append(num_needed)

print(' '.join(map(str, required_set_list)))

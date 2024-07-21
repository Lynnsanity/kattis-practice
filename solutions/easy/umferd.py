cells_per_lane = int(input())
num_lanes = int(input())

total_cells = cells_per_lane * num_lanes

dot_count = 0
for x in range(num_lanes):
    dot_hash = input()
    dot = dot_hash.strip("#")
    dot_count += int(dot.count('.'))

final_proportion = dot_count / total_cells
print(final_proportion)



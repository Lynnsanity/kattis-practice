option_one_sp_percentage = int(input())

option_two_sp_percentage = 100 - option_one_sp_percentage

option_one_ratio = 100 / option_one_sp_percentage
option_two_ratio = 100 / option_two_sp_percentage

print("{:.10f}".format(option_one_ratio))
print("{:.10f}".format(option_two_ratio))


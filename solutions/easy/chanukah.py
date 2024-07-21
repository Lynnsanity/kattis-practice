data_sets = int(input())

#x = 1
for x in range(data_sets):
    set_num_days = input()
    set_num, days = set_num_days.split()
    int_set_num = int(set_num)
    int_days = int(days)

    total_candles = 0
    for i in range(1, int_days + 1):
        candles_today = i + 1
        total_candles += candles_today

    print(f"{set_num} {total_candles}")

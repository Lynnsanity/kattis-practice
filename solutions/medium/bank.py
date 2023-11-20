# start the total cash at 0 because money will be counted as we go
total_cash = 0
# this is for the amount of money we can get, but it needs checks afterward
potential_cash = []
# customer dict containing leave times and their associating cash amounts
customer_dict = {}

# read the first line and get the people_in_queue and the time_remaining till bank closes
first_line = input().split()
people_in_queue = int(first_line[0])
time_remaining = int(first_line[1])

# a for loop for getting customer info
for _ in range(people_in_queue):
    # the whole input line is both the cash and time
    cash_and_time = input().split()
    # the customer cash is the first part of line
    customer_cash = int(cash_and_time[0])
    # the customers amount of time in which they'll leave is the second part of line
    customer_leave_time = int(cash_and_time[1])

    # if the customer leave time repeats, the customer cash will be appended to that time.
    customer_dict.setdefault(customer_leave_time, []).append(customer_cash)

# a reverse iterator, considers customers leaving closer to closing time
for time in range(time_remaining)[::-1]:
    # are there customers leaving at the current time? if so, go into the if statement
    if time in customer_dict.keys():
        # if there's more than one person leaving at the same time, it goes over each cash amount and puts it in a list called potential_cash
        for cash in customer_dict[time]:
            potential_cash.append(cash)
        # if there was a potential cash found then go into if statement
        if potential_cash:
            # add the max potential cash to total cash
            total_cash += max(potential_cash)
            # reset the potential_cash list so the next iteration can be fresh
            potential_cash.remove(max(potential_cash))

# total money we can get :D
print(total_cash)


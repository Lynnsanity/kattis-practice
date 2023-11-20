space = ' '
total_cash = 0
customers = []

with open('input.txt') as file:
    # make the entire first line a variable,
    # so then we can split components for variables we need
    first_line = file.readline().split()
    people_in_queue = int(first_line[0])
    time_remaining = int(first_line[1])
    print("Number of people in queue:", people_in_queue, "Time before closing:", time_remaining)
    # the first readline already upped the file line counter to 1,
    # so the values in here skip the first line
    for line in file:
        # split whatever line we're on (by default it'll split spaces)
        cash_and_time = line.split()
        # the first number is cash
        customer_cash = int(cash_and_time[0])
        # second number is minutes representing when people are gonna leave
        customer_leave_time = int(cash_and_time[1])
        # make a tuple so both customer cash and leave time can correspond with each other and attach it onto the list of customers
        customers.append((customer_cash, customer_leave_time))

# reverse the order of the customer list so that its starts with greater cash amounts
customers.sort(reverse=True)

# make sure we can serve the customer, and when we do decrease by time by 1 min.
for customer_cash, customer_leave_time in customers:
    if time_remaining >= customer_leave_time + 1:
        total_cash += customer_cash
        time_remaining -= 1

print(total_cash)

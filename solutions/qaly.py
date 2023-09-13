# the first input will give us the integer range we need for the for loop
period_of_life = int(input())
# start off with variable that stores the overall qaly
overall_qaly = 0.0
# for each line after the first input we need the quality_of_life_counter to add onto the overall_qaly_counter
for qaly_of_life_counter in range(period_of_life):
    # split the two values of qaly and years with that qaly
    qaly, years_with_quality = map(float, input().split())
    # multiply the two values together to make the counter value
    qaly_of_life_counter = qaly * years_with_quality
    # add the counter value to the overall qaly
    overall_qaly += qaly_of_life_counter

# once the for loop is over we should print the overall_qaly
## when its printed, print it over 3 decimal places
print("{:.3f}".format(overall_qaly))


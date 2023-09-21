import math

year_entered = 2022
improvements_while_frozen = input()
improvements_per_year = input()

years = int(improvements_while_frozen) / int(improvements_per_year)

current_year = year_entered + years

print(math.trunc(current_year))

from slide import slide
from random import randrange
from unique import unique_values

# Our first puzzle refers to the window problem, but I thought it could be a little fun to explore its utility in
# staffing a small business.  In the slide.py I check a window through the list of integers to find the set with the
# highest total.  Then I grab the indices of that window, because those are the vacation starts and ends for our lucky
# manager.

hours = []
for i in range(31):
    day = randrange(8)
    hours.append(day)

coverage, start_date, end_date = slide(hours, 5)
print("Congratulations on your vacation, it will have the most coverage at ", coverage, "hours, and you will be taking off March ", start_date, ' and returning ', end_date)

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.

a = [1, 2, 3, 4, 2, 1]
b = [1, 2, 3]

result_a = unique_values(a)
print("Result for array a is ", result_a)
result_b = unique_values(b)
print("Result for array b is ", result_b)

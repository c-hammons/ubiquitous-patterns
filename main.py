from slide import slide
from random import randrange

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

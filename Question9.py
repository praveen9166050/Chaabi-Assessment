# Q9.
# Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else returns False.

def dateDiff(from_date, to_date, difference):
    from datetime import date

    from_date = date(int('20' + from_date[:2]), int(from_date[3:5]), int(from_date[6:]))
    to_date = date(int('20' + to_date[:2]), int(to_date[3:5]), int(to_date[6:]))

    delta = to_date - from_date

    return delta.days == difference

from_date = '20-04-10'
to_date = '20-05-5'
difference = 25

print(dateDiff(from_date, to_date, difference))
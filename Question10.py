# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'

def function(d, n):
    from datetime import date, timedelta
    d = date(int('20' + d[:2]), int(d[3:5]), int(d[6:]))
    return d - timedelta(days=n)

d = '16-12-10'
n = 11

print(function(d, n))

""" timeTransformation
Given a certain string that contains a date in the US format 
"Month Day, Year HH:MM AM/PM", write a function that returns a string 
with the time in the following format: "YYYY-MM-DD HH:MM", with the time 
in 24h notation.

For example, the following input:
"February 2, 2008 1:23 PM"
should return:
"2008-02-02 13:23"

Note that the comma between the day and the year may or may not be present 
on the input. Note also that the month name and "AM/PM" may be provided in 
lowercase, uppercase or a mix of both. You may assume that the input contains 
a valid date and time.
"""

from datetime import datetime
def solution(S):
    dt = ''
    if S.find(',') != -1: dt = datetime.strptime(S, '%B %d, %Y %I:%M %p')
    else: dt = datetime.strptime(S, '%B %d %Y %I:%M %p')
    return str(dt)[:-3]


print(solution('February 2, 2008 1:23 PM')) #2008-02-02 13:23
print(solution('February 2 2008 1:23 PM')) #2008-02-02 13:23
print(solution('february 2 2008 1:23 PM')) #2008-02-02 13:23
print(solution('FEBRUARY 2 2008 1:23 pM')) #2008-02-02 13:23
print(solution('January 1 1900 3:37 PM')) #1900-01-01 15:37
print(solution('december 31 2200 3:37 pm')) #2200-12-31 15:37
print(solution('January 1 1800 3:37 PM')) #1800-01-01 15:37
print(solution('december 31 2400 12:00 am')) #2400-12-31 00:00



""" frenchWeeksConvertion 
The French Revolutionary Calendar was a calendar created and implemented 
during the French Revolution, and used by the French government for about 
12 years from late 1793 to 1805. The Republic used a decimal time system 
where: 

1 Minute = 100 Seconds 
1 Hour = 100 Minutes
1 Day = 10 Hours 
1 Week = 10 Days

Given a number of normal weeks (real number), create a function which 
returns the corresponding number of French Revolutionary weeks (real number).
"""

def frenchWeeks(weeks):
    return weeks * (10/7)
     
    
print(frenchWeeks(9)) # 12.857142857142858
print(frenchWeeks(7)) # 10
print(frenchWeeks(1)) # 1.4285714285714286
print(frenchWeeks(0)) # 0.0
print(frenchWeeks(3.74)) # 5.342857142857143
print(frenchWeeks(-1)) # -1.4285714285714286



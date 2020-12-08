
""" trueFalseCount
Given an array that contains a large number of boolean values (either True 
or False), create the most efficient function possible that returns True 
in case the majority of the values are True, or otherwise returns False. 
The input array contains only Boolean values.
"""

def trueFalse(arr):
    return True if sum(arr) > len(arr)/2 else False


print(trueFalse([False, False, True, True]))  # False
print(trueFalse([True, False, True, True]))  # True

""" mergeArraysUniqueValues
Write an algorithm that will take two arrays of numbers and merge only the unique values 
(that appear in one array but not in both arrays) into a final sorted array (without repeats). 
"""

def merge(a, b):
    set_a, set_b = set(a), set(b)
    return sorted(list(set_a ^ set_b))


print(merge([1,2,3,4], [1,4,7,8])) #[2, 3, 7, 8]


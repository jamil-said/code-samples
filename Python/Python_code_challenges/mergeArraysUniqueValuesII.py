""" mergeArraysUniqueValuesII
Write an algorithm that will take two arrays of numbers and merge only the unique values 
(unique both in each array as well as both arrays) into a final sorted array. 
"""

def merge(a, b):
    res = set()
    set_a = set()
    sum_arr = a + b
    for i in sum_arr:
        if i in set_a:
            if i in res:
                res.remove(i)
        else:
            set_a.add(i)
            res.add(i)
    return sorted(list(res))


print(merge([1,2,2,3,4], [1,4,4,6,7,8])) #[3, 6, 7, 8]


"""
Get the sum of two arrays...actually the sum of all their elements.
P.S. Each array includes only integer numbers. Output is a number too.
"""

def array_plus_array(arr1,arr2):
    new_arr = zip(arr1, arr2)
    arr3 = [sum(i) for i in new_arr]
    return sum(arr3)


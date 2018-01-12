"""
Get the number n to return the reversed sequence from n to 1.
Example : n=5 >> [5,4,3,2,1]
"""

def reverse_seq(n):
    n_array = []
    i = 0
    for i in range(n, 0, -1):
        n_array.append(i)
    return n_array

def peak(arr):
    i = 0
    for i in range(i, len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
        i = i  + 1
            
    return -1

"""
Test.it("Basic tests")
Test.assert_equals(peak([1,2,3,5,3,2,1]),3)
Test.assert_equals(peak([1,12,3,3,6,3,1]),2)
Test.assert_equals(peak([10,20,30,40]),-1)
"""

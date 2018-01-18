def cantor(nested_list):
    i = 0
    new_list = []
    size = len(nested_list[0])
    for i in range(i, size):
        if nested_list[i][i] == 0:
            new_list.append(1)
        else:
            new_list.append(0)
            
    return new_list


"""Test

example1 = [[0,0],
            [1,1]]
            
Test.assert_equals(cantor(example1), [1,0])  

example2 = [[1,1],
            [0,0]]
            
Test.assert_equals(cantor(example2), [0,1]) 

example3 = [[0,1],
            [1,0]]
            
Test.assert_equals(cantor(example3), [1,1]) 
            
example4 = [[0,0,0],
            [1,1,1],
            [0,1,0]]

Test.assert_equals(cantor(example4), [1,0,1])

example5 = [[1,0,0],
            [0,1,0],
            [0,0,1]]

Test.assert_equals(cantor(example5), [0,0,0])

"""



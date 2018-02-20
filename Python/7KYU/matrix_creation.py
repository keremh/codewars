def get_matrix(n):
    matrix = [[0]*n for i in range(n)]
    for a in range(len(matrix)):
        matrix[a][a] = 1
        
    return matrix

"""
Test.assert_equals(get_matrix(0), [])
Test.assert_equals(get_matrix(1), [[1]])
Test.assert_equals(get_matrix(2), [[1, 0], [0, 1]])
Test.assert_equals(get_matrix(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
"""

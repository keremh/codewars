def solve(a,b):
    result = []    
    for j in range(len(b)):
        counter = 0
        for i in range(len(a)):
            if b[j] == a[i]:
                counter += 1
        result.append(counter)                
    return result


"""
Test.assert_equals(solve(['abc', 'abc','xyz','abcd','cde'], ['abc', 'cde', 'uap']), [2, 1, 0])
Test.assert_equals(solve(['abc', 'xyz','abc', 'xyz','cde'], ['abc', 'cde', 'xyz']), [2, 1, 2])
Test.assert_equals(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']), [2, 0, 1])
"""

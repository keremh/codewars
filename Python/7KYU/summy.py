def summy(string_of_ints):
    temp_list = string_of_ints.split()
    result = [ int(x) for x in temp_list ]
    return sum(result)


"""
test.assert_equals(summy("1 2 3"), 6)
test.assert_equals(summy("1 2 3 4"), 10)
test.assert_equals(summy("1 2 3 4 5"), 15)
test.assert_equals(summy("10 10"), 20)
test.assert_equals(summy("0 0"), 0)

"""

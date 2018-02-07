def sumDigits(number):
    number = abs(number)
    n = 0
    while number:
        n += number % 10
        number //= 10
    return n

"""
test.assert_equals(sumDigits(10), 1)
test.assert_equals(sumDigits(99), 18)
test.assert_equals(sumDigits(-32), 5)
"""

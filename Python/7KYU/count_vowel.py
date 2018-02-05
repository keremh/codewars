def count_vowels(s = ''):
    if type(s) == str:
        s = s.lower()
        count = 0
        vowels = ['a','e','i','o','u']
        for a in s:
            if a in vowels:
                count += 1
        return count
    else:
        return None

"""

Test.assert_equals(count_vowels("abcdefg"),2)
Test.assert_equals(count_vowels("asdfdsafdsafds"), 3)

"""

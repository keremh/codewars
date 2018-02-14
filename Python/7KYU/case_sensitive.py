def case_sensitive(s):
    upper_list = []
    result = []
    for a in s:
        if a.isupper():
            upper_list.append(a)
        else:
            continue
    if len(upper_list) == 0:
        result.append(True)
        result.append(upper_list)
        return result
    else:
        result.append(False)
        result.append(upper_list)
        return result
        
"""
test.assert_equals(case_sensitive('asd'), [True, []])
test.assert_equals(case_sensitive('cellS'), [False, ['S']])
test.assert_equals(case_sensitive('z'), [True, []])
test.assert_equals(case_sensitive(''), [True, []])

"""

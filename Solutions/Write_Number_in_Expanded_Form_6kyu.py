"""
Write Number in Expanded Form (6 kyu)

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    strn = str(num)
    result = ''
    for i in range(len(strn)):
        if int(strn[i]) != 0:
            result += strn[i] + '0'*(len(strn) - i - 1)
            if (i != len(strn) - 1) and (int(strn[i+1:]) != 0):
                result += ' + '
    return result
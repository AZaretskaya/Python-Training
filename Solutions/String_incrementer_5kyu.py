"""
String incrementer (5 kyu)

Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""

def increment_string(strng):
    if strng == '' or not strng[-1].isdigit():
        return strng + '1'
    if int(strng[-1]) < 9:
        return strng[:-1] + str(int(strng[-1]) + 1)
    if strng[-1] == '9':
        i = -1
        while strng[i] == '9':
            i -= 1
        if strng[i].isdigit():
            return strng[:i] + str(int(strng[i]) + 1) + '0' * (-i - 1)
        else:
            return strng[:i + 1] + '1' + '0' * (-i - 1)
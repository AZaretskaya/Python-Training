"""
Length and two values (7 kyu)

Given an integer n and two other values, build an array of size n filled with these two values alternating.
Examples

5, true, false     -->  [true, false, true, false, true]
10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
0, "one", "two"    -->  []

"""

def alternate(n, first_value, second_value):
    result = []
    if n % 2 == 0:
        for i in range(n // 2):
            result.append(first_value)
            result.append(second_value)
    else:
        for i in range((n-1) // 2):
            result.append(first_value)
            result.append(second_value)
        result.append(first_value)
    return result

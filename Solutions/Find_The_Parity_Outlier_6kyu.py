"""
Find The Parity Outlier (6 kyu)

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
"""

def find_outlier(integers):
    condition = [integers[0] % 2, integers[1] % 2, integers[-1] % 2]
    even_odd = (0, 1)[sum(condition) < 2]
    for num in integers:
        if num % 2 == even_odd:
            return num
"""
Sum of a sequence (7 kyu)

Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step (inclusive).

If begin value is greater than the end, function should returns 0

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)
"""

def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        num = begin_number
        total = 0
        while num <= end_number:
            total +=num
            num += step
    return total

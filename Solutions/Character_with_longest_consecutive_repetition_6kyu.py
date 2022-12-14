"""
Character with longest consecutive repetition (6 kyu)

For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)

where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

('', 0)
"""

def longest_repetition(chars):
    c = ''
    l = 0
    s_prev = c
    for s in chars:
        if s != s_prev:
            sl = 1
        else:
            sl += 1
        if l < sl:
            l = sl
            c = s
        s_prev = s
    return (c, l)
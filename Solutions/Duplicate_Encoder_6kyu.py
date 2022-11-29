"""
Duplicate Encoder (6 kyu)

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""

def duplicate_encode(word):
    result = ''
    for c in word.lower():
        if word.lower().count(c.lower()) == 1:
            result += '('
        else:
            result += ')'
    return result

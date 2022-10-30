"""
Rot13 (5 kyu)

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
"""

def rot13(message):
    res = ''
    for c in message:
        if not c.isalpha():
            res += c
        else:
            if c.islower():
                res += chr(ord(c) + 13 if ord('a') + 26 - ord(c) > 13 else ord(c) - 13)
            elif c.isupper():
                res += chr(ord(c) + 13 if ord('A') + 26 - ord(c) > 13 else ord(c) - 13)
    return res
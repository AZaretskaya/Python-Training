"""
Detect Pangram (6 kyu)

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(s):
    text = ''
    for c in s:
        if c.isalpha():
            text += c.lower()
    for n in range(ord('a'), ord('a') + 26):
        if chr(n) not in text:
            return False
    return True
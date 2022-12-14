"""
Highest Scoring Word (6 kyu)

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""

def high(x):
    word_list = x.split()
    score = []
    for word in word_list:
        word_score = 0
        for c in word:
            word_score += ord(c) - ord('a') + 1
        score.append(word_score)
    return word_list[score.index(max(score))]
"""
Interactive Dictionary (7 kyu)

In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:

>>> d = Dictionary()

>>> d.newentry('Apple', 'A fruit that grows on trees')

>>> print(d.look('Apple'))
A fruit that grows on trees

>>> print(d.look('Banana'))
Can't find entry for Banana
"""

class Dictionary():
    def __init__(self):
        self.d = {}
    
    def newentry(self, word, definition):
        self.d[word] = definition
        
    def look(self, key):
        if key in self.d.keys():
            return self.d[key]
        else:
            return f"Can't find entry for {key}"
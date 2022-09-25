"""
Baby Shark Lyrics (7 kyu)

Create a function, as short as possible, that returns this lyrics.
Your code should be less than 300 characters. Watch out for the three points at the end of the song.

Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…

Good Luck!
"""

def baby_shark_lyrics():
    w=['Baby','Mommy','Daddy','Grandma','Grandpa']
    l='\n'
    r=''
    for i in w:
        r+=(f'{i} shark, ' + 'doo ' * 5 + 'doo' + l) * 3 + f'{i} shark!' + l
    r+=("Let's go hunt, " + 'doo ' * 5 + 'doo' + l) * 3 + "Let's go hunt!" + l + 'Run away,…'
    return r
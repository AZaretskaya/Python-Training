"""
Who has the most money? (6 kyu)

ou're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

Notes:

    Each student will have a unique name
    There will always be a clear winner: either one person has the most, or everyone has the same amount
    If there is only one student, then that student has the most money
"""

def most_money(students):
    richest = students[0]
    the_same = True
    for st in students:
        if len(students) == 1:
            return students[0].name
        if 5 * st.fives + 10 * st.tens + 20 * st.twenties != \
            5 * richest.fives + 10 * richest.tens + 20 * richest.twenties:
            the_same = False
        if 5 * st.fives + 10 * st.tens + 20 * st.twenties > \
            5 * richest.fives + 10 * richest.tens + 20 * richest.twenties:
            richest = st
    return 'all' if the_same else richest.name
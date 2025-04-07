# iterators_generators.py

import random

# Custom iterator for students
class StudentIterator:
    def __init__(self, student_list):
        self.students = student_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            result = self.students[self.index]
            self.index += 1
            return result
        raise StopIteration

# Generator for random marks
def generate_random_marks(n):
    for _ in range(n):
        yield random.randint(60, 100)

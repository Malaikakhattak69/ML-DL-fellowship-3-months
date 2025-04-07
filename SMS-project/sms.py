# sms.py

class Student:
    def __init__(self, name, age, roll_no, marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = marks  # List of marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"{self.roll_no} - {self.name} (Age: {self.age}) | Marks: {self.marks}"

# Inheritance: Graduate student with thesis
class GraduateStudent(Student):
    def __init__(self, name, age, roll_no, marks, thesis):
        super().__init__(name, age, roll_no, marks)
        self.thesis = thesis

    def __str__(self):
        return f"{super().__str__()} | Thesis: {self.thesis}"

# file_utils.py

from sms import Student

def save_students(filename, students):
    with open(filename, 'w') as f:
        for s in students:
            marks_str = ",".join(map(str, s.marks))
            f.write(f"{s.name}|{s.age}|{s.roll_no}|{marks_str}\n")

def load_students(filename):
    students = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                name, age, roll_no, marks = line.strip().split('|')
                marks_list = list(map(int, marks.split(',')))
                students.append(Student(name, int(age), roll_no, marks_list))
    except FileNotFoundError:
        print("No file found. Starting with empty list.")
    return students

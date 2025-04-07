# main.py

from sms import Student, GraduateStudent
from file_utils import save_students, load_students
from iterators_generators import StudentIterator, generate_random_marks
from student_utils.arithmetic import calculate_percentage, classify_grade
from student_utils.performance import performance_by_average

filename = "students.txt"
students = load_students(filename)

def add_student():
    name = input("Name: ")
    age = int(input("Age: "))
    roll = input("Roll No: ")
    marks = list(generate_random_marks(3))  # 3 subjects
    student = Student(name, age, roll, marks)
    students.append(student)
    print("Student Added.")

def view_students():
    if not students:
        print("No students found.")
        return
    print("\n--- All Students ---")
    for student in StudentIterator(students):
        avg = student.calculate_average()
        print(student)
        print(f"Average: {avg:.2f}, Performance: {performance_by_average(avg)}\n")

def save_and_exit():
    save_students(filename, students)
    print("Data saved. Goodbye!")

def menu():
    while True:
        print("\n📘 Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save & Exit")

        choice = input("Choose (1-3): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            save_and_exit()
            break
        else:
            print("Invalid input.")

menu()

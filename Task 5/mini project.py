# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 19:32:41 2025

@author: 97154
"""

# Simple Solutions for Week 1 Mini-Project: Python Basics

# Question 1: User Data Collector
def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            break
        print("Invalid email! Try again.")
    fav_num = input("Enter your favorite number: ")
    print(f"Name: {name}, Age: {age}, Email: {email}, Favorite Number: {fav_num}")

# Question 2: Even or Odd?
def check_even_odd():
    num = int(input("Enter a number: "))
    print(f"{num} is Even." if num % 2 == 0 else f"{num} is Odd.")

# Question 3: Temperature Converter
def convert_temperature():
    temp = float(input("Enter temperature: "))
    scale = input("Enter scale (C/F): ")
    if scale.upper() == "C":
        print(f"Fahrenheit: {(temp * 9/5) + 32}")
    elif scale.upper() == "F":
        print(f"Celsius: {(temp - 32) * 5/9}")
    else:
        print("Invalid scale")

# Question 4: Finding Min & Max
def find_max_min():
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(5)]
    print(f"Max: {max(numbers)}, Min: {min(numbers)}")

# Question 5: Student Data Manager
def student_data_manager():
    students = {}
    for _ in range(3):
        name = input("Enter student name: ")
        age = input("Enter age: ")
        grade = input("Enter grade: ")
        students[name] = (age, grade)
    print("Student Data:", students)

# Question 6: Inventory Management
def inventory_manager():
    inventory = {"Apples": 10, "Bananas": 5, "Oranges": 8}
    print("Current Inventory:", inventory)
    for _ in range(3):
        item = input("Enter item: ")
        quantity = int(input("Enter quantity (+/-): "))
        inventory[item] = max(0, inventory.get(item, 0) + quantity)
    print("Updated Inventory:", inventory)

# Run all functions
if __name__ == "__main__":
    collect_user_data()
    check_even_odd()
    convert_temperature()
    find_max_min()
    student_data_manager()
    inventory_manager()

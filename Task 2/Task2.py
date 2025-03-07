# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 10:55:04 2025

@author: 97154
"""

# Task 2: Simple Statistical Functions in Python

# Mean Calculation
def mean(numbers):
    return sum(numbers) / len(numbers)

# Median Calculation
def median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]

# Mode Calculation
def mode(numbers):
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    max_count = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_count]
    return modes[0] if len(modes) == 1 else modes

# Variance Calculation
def variance(numbers):
    m = mean(numbers)
    return sum((x - m) ** 2 for x in numbers) / len(numbers)

# Standard Deviation Calculation
def standard_deviation(numbers):
    return variance(numbers) ** 0.5

# Euclidean Distance Calculation
def euclidean_distance(x, y):
    if isinstance(x, list) and isinstance(y, list):
        return sum((a - b) ** 2 for a, b in zip(x, y)) ** 0.5
    return abs(x - y)

# Sigmoid Function
def sigmoid(x):
    return 1 / (1 + 2.71828 ** -x)

# Example Usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Mean:", mean(numbers))
print("Median:", median(numbers))
print("Mode:", mode(numbers))
print("Variance:", variance(numbers))
print("Standard Deviation:", standard_deviation(numbers))
print("Euclidean Distance (single values):", euclidean_distance(3, 7))
print("Euclidean Distance (lists):", euclidean_distance([1, 2, 3], [4, 5, 6]))
print("Sigmoid Function:", sigmoid(2))


# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 11:18:56 2025

@author: 97154
"""

# Task 3: Implementing Machine Learning Functions in Python (No Libraries)

# Mean Squared Error (MSE)
def mse(actual, predicted):
    return sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)

# Root Mean Squared Error (RMSE)
def rmse(actual, predicted):
    return mse(actual, predicted) ** 0.5

# Cosine Similarity
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = sum(a ** 2 for a in vec1) ** 0.5
    magnitude2 = sum(b ** 2 for b in vec2) ** 0.5
    return dot_product / (magnitude1 * magnitude2) if magnitude1 and magnitude2 else 0

# Linear Regression (Simple - One Feature)
def linear_regression(x, y):
    n = len(x)
    mean_x, mean_y = sum(x) / n, sum(y) / n
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
    slope = numerator / denominator if denominator else 0
    intercept = mean_y - slope * mean_x
    return slope, intercept

# Softmax Function
def softmax(values):
    exp_values = [2.71828 ** v for v in values]
    total = sum(exp_values)
    return [ev / total for ev in exp_values]

# Example Usage
actual = [1, 2, 3, 4, 5]
predicted = [1.1, 1.9, 3.2, 3.8, 5.1]
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
values = [1.0, 2.0, 3.0]

print("MSE:", mse(actual, predicted))
print("RMSE:", rmse(actual, predicted))
print("Cosine Similarity:", cosine_similarity(vec1, vec2))
slope, intercept = linear_regression(x, y)
print("Linear Regression (Slope, Intercept):", (slope, intercept))
print("Softmax:", softmax(values))

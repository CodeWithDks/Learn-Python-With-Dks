"""Problem 1 — Warm up 🟢

Write a program that asks the user for their name and age. Then print:"""
"Hello [name]! In 10 years, you will be [age+10] years old."

# Solution:

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}! In 10 years, you will be {user_age+10} years old.")

"""Problem 2 — Think a little 🟡

Ask the user to enter two numbers. Print their sum, difference, product, 
and the result of dividing the first by the second. Handle the case where the second number is 0."""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2

if num2 != 0:
    divide = num1 / num2
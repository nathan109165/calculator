"""
Filename: simple_calculator.py
Author: <Farlow, Nathan>
Created: <08/28/2025>
Instructor: Holtslander
"""

print('Welcome to simple calculator! This will calculate the sum, difference, product, and quotient of any two numbers you input.')
input('\nPress enter to continue.')
num1 = input('Please enter your first number without commas. Must be an integer, not a decimal.\n')
num2 = input('Please enter your second number without commas. Must be an integer, not a decimal.\n')
num1 = int(num1)
num2 = int(num2)
print(f'\n{num1} plus {num2} is equal to', num1 + num2)
print(f'{num1} minus {num2} is equal to', num1 - num2)
print(f'{num1} times {num2} is equal to', num1 * num2)
print(f'{num1} divided by {num2} is equal to', num1 / num2, '\n\nThank you for using simple calculator!')
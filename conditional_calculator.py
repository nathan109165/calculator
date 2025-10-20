# num = input('Enter a number.\n')
# num = int(num)
# if num % 5 == 0:
#     print(f'{num} is divisible by 5.')
# if num % 2 == 0:
#     print(f'{num} is an even number.')
# else:
#     print(f'{num} is an odd number.')
# print('\nDone.')

"""
Filename: conditional_calculator.py
Author: <Farlow, Nathan>
Created: <09/09/2025>
Instructor: Holtslander
"""

print('Welcome to conditional calculator! This will calculate the sum, difference, product, and quotient of any two numbers you input depending on your operator.')
input('\nPress enter to continue.')
num1 = input('Please enter your first number without commas. Must be an integer, not a decimal.\n')
op = input('Please enter your operator.\n'
           '"+" is for addition\n'
           '"-" is for subtraction\n'
           '"*" is for multiplication\n'
           '"/" is for division\n'
           "Anything else will do all four. And don't just type 'add' if you want to use addition. Make sure you use the + symbol.")
num2 = input('Please enter your second number without commas. Must be an integer, not a decimal.\n')

num1 = int(num1)
num2 = int(num2)
if op == '+':
    print(f'\n{num1} plus {num2} is equal to', num1 + num2)
elif op == '-':
    print(f'{num1} minus {num2} is equal to', num1 - num2)
elif op == '*':
    print(f'{num1} times {num2} is equal to', num1 * num2)
elif op == '/':
    print(f'{num1} divided by {num2} is equal to', num1 / num2)
else:
    print(f'\n{num1} plus {num2} is equal to', num1 + num2)
    print(f'{num1} minus {num2} is equal to', num1 - num2)
    print(f'{num1} times {num2} is equal to', num1 * num2)
    print(f'{num1} divided by {num2} is equal to', num1 / num2)

print('\nThank you for using conditional calculator!')
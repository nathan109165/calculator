"""
Filename: Warm-Up_7_Circle_Calculator.py
Author: <Farlow, Nathan>
Created: <12/04/2025>
Instructor: Holtslander
"""

import math

def circle_calculator():
    """
    Calculates the area and circumference of a circle.
    Asks the user to enter the radius of the circle.
    Uses the formulas
    A = pi*r**2
    C = 2*pi*r
    :return: None
    """
    ### YOUR CODE GOES HERE ###
    r = float(input('I give you area and circumference, you give me radius in floating-point expression. Good deal.\n'))
    d = r*2
    a = math.pi*r**2
    c = math.pi*d
    print(f'Here is what you bought with the radius of {r}:\nThe area is equal to {a} and the circumference is equal to {c}.')
    


### YOU SHOULD NOT NEED TO CHANGE ANYTHING HERE ###
if __name__ == '__main__':
    circle_calculator()

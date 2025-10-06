'''
Write a function computing the perimeter of a circle given its radius.

Your function should be named circle_perimeter(radius), 
where the radius parameter is the radius of a circle.

Your function should return the perimeter of a circle of the given radius.
'''

# Type your code here:

import math

def circle_perimeter(radius):
    pi = math.pi
    c_p = pi * radius * 2
    return (c_p)

# You don't need to modify the following part
# it allows you to test your code before submitting it:

if __name__ == "__main__":
    print(circle_perimeter(1))
"""
Given an integer n perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 print Not Weird
If n is even and in the inclusive range of 6 to 20 print Weird
If n is even and greater than 20 print Not Weird

# A single line containing a positive integer,N .
"""
N = int(input())
x = 1
if x == 1:
    try:
        if N % 2 == 0:
            if N in range(2, 5) :
                print('Not Weird')
            elif N in range(6, 20):
                print('weird')
            elif N > 20 :
                print('Not Weird')
            else:
                pass

        else:
            print('Weird')

    except ValueError:
        print('Please Enter A Valid Number')
else:
    pass    
x =-1

"""
# Hacker Rank Code
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
"""
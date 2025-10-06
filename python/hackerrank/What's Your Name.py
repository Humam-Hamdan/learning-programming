# Task:
"""
You are given the firstname and lastname of a person on two different lines.
Your task is to read them and print the following: 
"Hello firstname lastname! You just delved into python."
The first line contains the first name, and the second line contains the last name. 
The length of the first and last name ≤ 10.
"""
# My Code:
'''
a = str(input())
b = str(input())


def print_full_name(a, b):
    print('Hello {}! You just delved into python'.format(a + b))


if __name__ == '__main__':
    print_full_name(a, b)
'''
# 2nd Try:


def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

'''
Write a script that prints every even numbers between 1 and 100 inclusive, one per line.
'''
for i in range(1, 101, 1):
    if i % 2 == 0:
        print(i)

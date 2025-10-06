
def is_leap(year):
    leap = False
    
    # Write your logic here
    year >= 1900 and year <= 10^5
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        leap = True
        print('T')
    else:
        leap = False
        print('F')

    return leap
year = int(input())
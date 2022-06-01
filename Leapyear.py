def is_leap(year):
    leap = 'False'

    # Write your logic here
    if (year % 400 == 0) and (year % 100 == 0):
        leap = 'True'
    elif (year % 4 == 0) and (year % 100 != 0) :
        leap = 'True'
    else:
        leap = 'False'
    return leap

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))

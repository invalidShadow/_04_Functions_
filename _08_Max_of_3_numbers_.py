# P08. REQ : Maximum of three numbers  #


def max_of_three(x, y, z):

    if x > y and x > z:
        print(f'{x} is the greatest of the three numbers')
    elif y > x and y > z:
        print(f'{y} is the greatest of the three numbers')
    else:
        print(f'{z} is the greatest of the three numbers')


a, b, c = [int(x) for x in input('Please enter 3 numbers: ').split()]

max_of_three(a, b, c)

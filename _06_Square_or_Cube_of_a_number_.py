# P06. REQ : Cube/Square of the given number  #


def power(x, y):

    res = 0
    if y == 'square':
        res = x * x
    elif y == 'cube':
        res = x * x * x
    else:
        print('Enter a valid choice!')

    print(f'The {y} of the number {x} = {res}')


a = int(input('Please enter a number, a = '))

b = input('square or cube?: ')

power(a, b)


# Using lambda function #

rslt = lambda m, n: m * m if n == 'square' else m * m * m

print(f'The {b} of the number is {rslt(a, b)}')

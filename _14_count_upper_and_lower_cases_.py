# P14. REQ : Count the upper and lower case characters in a given string  #


def count_case(msg):

    case = {'Upper': 0, 'Lower': 0}

    for char in msg:
        if char.isupper():
            case['Upper'] += 1
        else:
            case['Lower'] += 1

    print(f'The number of upper and lower case characters in the give string is {case}')


s = input('Enter a string: ')

count_case(s)

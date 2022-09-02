# P12. REQ : Reverse of a string  #


def reverse(s):

    rev = ""
    for i in s:
        rev = i + rev
    return rev


str1 = input('Enter a string: ')

print(f'Reverse of the entered string is {reverse(str1)}')

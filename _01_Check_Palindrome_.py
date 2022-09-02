# P01. REQ : Check if the given input is a palindrome  #

s = input('Enter a string: ')


def check_palindrome(string):
    if string == string[::-1]:
        print(f'\n{string} is a palindrome!')

    else:
        print(f'\nSorry, {string} is not a palindrome...')


check_palindrome(s)


# Using lambda Function #

is_pali = lambda msg: f'{msg} is a palindrome' if msg == msg[::-1] else f'{msg} is not a palindrome'

print(is_pali(s))

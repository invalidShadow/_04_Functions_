# P13. REQ : Check if the value is in the given range  #


def is_present(x, l, h):

    for i in range(l, h+1):
        if x == i:
            print(f'{x} is present in the range of {l} and {h}')
            break
    else:
        print(f'{x} is not present in the given range!')


n = int(input('Enter a number: '))

a = int(input('Enter the lower limit: '))

b = int(input('Enter the upper limit: '))

is_present(n, a, b)

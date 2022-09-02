# P05. REQ : Type conversion  #


def convert(x, y):

    if type(x) != y:
        x = y(x)
    else:
        print('The data is already of the desired type')
    return x


a = list(input('Enter the elements of the data structure: ').split())

print(convert(a, list))

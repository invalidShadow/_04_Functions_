# P11. REQ : Multiplication of list elements  #


def list_prod(l):

    product = l[0]

    for i in range(1, len(l)):
        product *= l[i]

    print(f'Sum of elements of the given list is {product}')


lst1 = list(map(int, input('Enter the elements of the list: ').split()))

list_prod(lst1)

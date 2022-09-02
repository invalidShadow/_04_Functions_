# P10. REQ : Sum of a list  #


def list_sum(l):

    sum_l = 0

    for i in range(len(l)):
        sum_l += l[i]

    print(f'Sum of elements of the given list is {sum_l}')


lst1 = list(map(int, input('Enter the elements of the list: ').split()))

list_sum(lst1)

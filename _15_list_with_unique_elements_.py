# P15. REQ : Return a new list with unique elements  #


def unique_list(l):

    unq_lst = []

    for ele in l:
        if ele not in unq_lst:
            unq_lst.append(ele)

    print(f'New list with unique elements is: {unq_lst}')


lst = list(map(int, input('Enter the elements of the list: ').split()))

unique_list(lst)

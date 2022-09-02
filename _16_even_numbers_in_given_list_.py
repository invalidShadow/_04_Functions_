# P15. REQ : Print even numbers in a given list  #


lst = list(map(int, input('Enter the elements of the list: ').split()))

even_list = list(filter(lambda x: (x % 2 == 0), lst))

print(f'New list with the even numbers is {even_list}')

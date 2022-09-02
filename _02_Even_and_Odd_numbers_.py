# P02. REQ : Print even and odd numbers  #

x = int(input('Enter the lower limit: '))

y = int(input('Enter the upper limit: '))


def even_odd(m, n):
    even = []

    odd = []

    if m < n:
        for i in range(m, n+1):
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

    print(f'List of even numbers between {m} and {n} are: {even}')

    print(f'List of odd numbers between {m} and {n} are: {odd}')


even_odd(x, y)

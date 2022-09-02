# P07. REQ : Table of the given number  #


print('*'*20, 'Table of a number', '*'*20, '\n')


def table(m, n):

    table_ = []
    for i in range(1, n+1):
        table_.append(m * i)
    return table_


a = int(input('Please enter a number, a = '))

b = int(input('Enter the multiple till you want the table, b = '))

print(f'The table of {a} till the {b}th multiple is: {table(a, b)}')

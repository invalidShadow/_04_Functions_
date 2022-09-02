# P09. REQ : Fibonacci series  #


def fibonacci(x, y, n):
    fibonacci_list = []

    if 0 <= x < y:
        for i in range(n):
            fibonacci_list.append(x + y)
            x = y
            y = fibonacci_list[i]

        print(f'The fibonacci series for the given input is {fibonacci_list}')
    else:
        print('Please enter valid values!')


a = int(input('Enter the first value: '))

b = int(input('Enter the second value: '))

c = int(input('Enter the number of values in the Fibonacci series: '))


fibonacci(a, b, c)

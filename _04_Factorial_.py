# P04. REQ : Factorial of a given number  #


print('*'*20, 'Factorial of a number', '*'*20, '\n')


def factorial(n):
    if n < 0:
        print('Please enter a positive number')

    elif n == 0 or n == 1:
        print(f'Factorial of {n} = 1')

    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        print(f'Factorial of {n} is {fact}\n')


a = int(input('Please enter a number, a = '))

factorial(a)

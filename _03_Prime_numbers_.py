# P03. REQ : Print prime numbers  #

x = int(input('Enter the lower limit: '))

y = int(input('Enter the upper limit: '))


def prime(m, n):
    prime_no = []

    for i in range(m, n+1):
        if i <= 1:
            continue
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_no.append(i)

    print(f'The prime numbers between {m} and {n} are {prime_no}')


prime(x, y)

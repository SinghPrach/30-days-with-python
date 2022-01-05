n = int(input('Enter the total number of terms for the Fibonacci series= '))  # enter any natural number

n1, n2 = 0, 1
count = 0

print('Fibonacci series for', n, 'terms is given below.')

while count < n:
    print(n1)
    nt = n1 + n2
    n1 = n2
    n2 = nt
    count = count + 1

# Finding HCF of any two numbers


def compute_HCF(x, y):
    if x > y:
        for i in range(y, x):
            if (x % i) == 0 and (y % i) == 0:
                print('The HCF of', x, 'and', y, 'is', i)
                break
            else:
                print('The HCF does not exist of', x, 'and', y)
                break
    else:
        for i in range(x, y):
            if (x % i) == 0 and (y % i) == 0:
                print('The HCF of', x, 'and', y, 'is', i)
                break
            else:
                print('The HCF does not exist of', x, 'and', y)
                break


n1 = int(input('Enter any number= '))
n2 = int(input('Enter any number= '))
compute_HCF(n1, n2)

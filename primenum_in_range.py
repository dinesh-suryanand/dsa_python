from math import sqrt

a = 0
b = 17

lis = []

def is_prime(n):
    prime_flag = 0
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        lis.append(n)

def range_prime(a,b):
    if a < 1 and b < 1 :
        return " not possible"
    if a < 1:
        a = 2
    for i in range(a,b):
        is_prime(i)
    return lis

print(range_prime(a,b))
from math import isqrt

def primes_less_than(n):
    if n<= 2:
        return []
    is_prime = [True] * n # list of n True values 
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


print(primes_less_than(100))

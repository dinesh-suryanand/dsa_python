n = 13420

def sum_of_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_of_digits(n//10)
def product_of_digits(n):
    if n%10 == n:
        return n
    return n%10 * product_of_digits(n//10)

print(product_of_digits(n))
"""
        To understand recursion
"""
def print_nums(n):
    if n ==0 :
        return
    print(n)
    print_nums(n-1)


def print_nums_rev(n):
    if n == 0:
        return
    print_nums_rev(n-1)
    print(n)


def print_both(n):
    if n ==0 :
        return
    print(n)
    print_both(n-1)
    print(n)

print(print_both(5))
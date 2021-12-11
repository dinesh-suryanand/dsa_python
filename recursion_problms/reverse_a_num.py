n = 749842

sum = 0

def rev1(n):
    if n == 0:
        return
    rem =n%10
    sum *= 10
    rev1(n/10)

print(rev1(n))

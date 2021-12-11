import math
n = 24

lst = []
for i in range(1, math.isqrt(n)+1):
    if n%i == 0:
        if n%i == i:
            lst.append(i)
        lst.append(i)
        lst.append(n//i)

lst.sort()
print(lst)

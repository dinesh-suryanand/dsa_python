n = 40
p = 4

def bssqrt(n,p):
    s=0
    e=n
    root = 0.0
    while (s<=e):
        m = s + (e-s)/2
        if(m*m == n):
            return m
        elif m*m > n:
            e = m-1
        else:
            s = m+1
    incr = 0.1
    for i in range(p):
        while root*root < n:
            root += incr
        root -= incr
        incr /= 10
    return root

print(f'{bssqrt(n,p):.4f}')
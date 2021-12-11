def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

print(gcd(8,98))

def lcm(a,b):
    return a*b / gcd(a,b)

print(f"the lcm is {int(lcm(2,3))}")
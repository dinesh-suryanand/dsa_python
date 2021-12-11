def funn(n):
    if n ==0 :
        return
    print(n)
    funn(n-1)



def funrev(n):
    if n == 0:
        return
    funrev(n-1)
    print(n)


def funboth(n):
    if n ==0 :
        return
    print(n)
    funboth(n-1)
    print(n)

print(funboth(5))
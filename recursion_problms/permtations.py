def permutations(p, up):
    if len(up) == 0:
        print(p)
        return
    ch = up[0]
    for i in range(len(p)+1):
        f = p[0:i]
        s = p[i:len(p)]
        permutations(f + ch + s , up[1:])

permutations("","abc")



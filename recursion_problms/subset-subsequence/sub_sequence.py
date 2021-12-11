def subseq(p, up):
    if len(up) == 0:
        print(p)
        return
    ch = up[0]
    subseq(p+ch , up[1:])
    subseq(p , up[1:])

# subseq("","abc")

l =[]
def subseq_list(p, up):
    if len(up) == 0:
        l.append(p)
        return
    ch = up[0]
    subseq_list(p+ch , up[1:])
    subseq_list(p ,up[1:])
    return l

print(subseq_list("","abc"))

def subseq_list_ascii(p, up):
    if len(up) == 0:
        l.append(p)
        return
    ch = up[0]
    subseq_list_ascii(p+ch , up[1:])
    subseq_list_ascii(p ,up[1:])
    subseq_list_ascii(p+int(ch+0),up[1:])
    return l

print(subseq("","acd"))
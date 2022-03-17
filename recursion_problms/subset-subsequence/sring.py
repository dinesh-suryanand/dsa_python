string1 = "baccad" # never name string as str    ----> beacuse of str() function


def remov(stri):
    ans = ""
    for i in stri: 
        if i == 'a' or i == 'A':
            continue
        ans += str(i)
    return ans
print(remov(string1))



word = 'baccad'


# without recursion
def rem_word(txt):
    txt.lower()
    s = ''
    for i in txt:
        if i == 'a':
            continue
        s += str(i)
    return s


#using recursion
def skip(processed, unprocessed): # most important method ,, p ,up.....
    if len(unprocessed) == 0:
        print(processed)
        return
    ch = unprocessed[0]
    if ch == "a":
        skip(processed, unprocessed[1:])
    else:
        skip(processed + ch, unprocessed[1:])


def skip(up):  
    if len(up) == 0:
        return ""
    ch = up[0]
    if ch == "a":
        return skip(up[1:])
    else:
        return ch + skip(up[1:])


# print(rem_word(word)) #without recursion
print(skip(word))

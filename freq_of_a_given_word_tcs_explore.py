
s = input()

word = input().lower()

print(len(s.split()))

s = ''.join(s.split()).lower()
res =s.count(word)
print(res)
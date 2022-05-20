def lcs(S1, S2, m, n):
  
    if m == 0 or n == 0:
       return 0
    elif S1[m-1] == S2[n-1]:
       return 1 + lcs(S1, S2, m-1, n-1)
    else:
       return max(lcs(S1, S2, m, n-1), lcs(S1, S2, m-1, n))

S1 = str(input())
S2 = str(input())
print (lcs(S1, S2, len(S1), len(S2)))
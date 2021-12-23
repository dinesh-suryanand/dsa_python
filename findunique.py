arr = [1,1,1,1,2,2,2,2,6,4,4,4,4,7,7,7,7]
unique = 0

for i in arr:
    unique ^= i  # a simple xor is enough if the repeated numbers are even times
    
print(unique)
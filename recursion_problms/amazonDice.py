#getting all the possibility to form a taget number using dice
# here the target element is 4
#using processed unprocessed only

def get_combinations(p,taget):
    if taget==0:
        print(p)
        return
    for i in range(1,7):
        if i <= taget:
            get_combinations(p+i,taget-i)
    


#didn't get the answer



#copied from gfg
# A Python program to print all
# permutations using library function
from itertools import permutations
 
# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])
 
# Print the obtained permutations
for i in list(perm):
    print (i)
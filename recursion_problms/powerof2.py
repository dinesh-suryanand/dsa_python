"""
    for understanding recursion we are finding powers of 2 , 3, any number i.e sqrt(2) sqrt(3) sqrt(anynum)...
"""

def isPowerofTwo(n):

    #base case
    if n == 1:
        return True

    elif n<=0 or n%2!=0:
        return False
    return isPowerofTwo(n/2)

#we can see what power of 3 is by using counter
def isPowerofThree(n,counter):
    #base case
    if n == 1:
        print(counter , end=" - ")
        return True
    elif n<=0 or n%3!=0:
        return False
    return isPowerofThree(n/3,counter+1)





print(isPowerofTwo(33)) #returns false
print(isPowerofTwo(1024)) #returns true

print(isPowerofThree(27,0)) #prints ans and returns true
print(isPowerofThree(43046721,counter=0)) #prints the pow value and returns true
print(isPowerofThree(234,0)) #returns false

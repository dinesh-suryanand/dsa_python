# * * * *
# * * *
# * *
# *

def triangel(row,col):
    if row ==0:
        return
    if col<row:
        print("*" ,end=' ')
        triangel(row,col+1)
    else:
        print()
        triangel(row-1,0)

triangel(4,0)

def triangle(row ,col):
    if row ==0:
        return
    if col<row:
        
        triangle(row,col+1)
        print("*" ,end=' ')
    else:
        triangle(row-1,0) 
        print()

triangle(4,0)
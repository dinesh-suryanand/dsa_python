import random2
def randomNo():
  rn = randint(0, 4)
  return rn

def populateStatus():
  status = {}
  for x in range (0,4):
    status [x]={}
    for y in range (0,4):
        status[x][y] = randomNo()

print(populateStatus())
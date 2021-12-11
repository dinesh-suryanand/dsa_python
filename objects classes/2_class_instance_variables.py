# #class variables are defined out side the initializer (__inti__) 
# #instance variable are defined inside the initializer

# class Player:
#     teamName = 'Liverpool'              # class variable
#     def __init__(self,name) -> None:
#         self.name  = name               # creating instance variables

# p1 = Player('Mark')
# p2 = Player('Steve')

# print("Name :",p1.name)
# print("Team Name:",p1.teamName)
# print("---------"*6)
# print("Name :",p2.name)
# print("Team Name:",p2.teamName)



# #---------------------------------------------------------------------------
# print("-- ######## --    "*4)
# class Player:
#     teamName = 'Liverpool'              # class variable
#     def __init__(self,name) -> None:
#         self.name  = name               # creating instance variables
#         self.formerTeam = []

# p1 = Player('Mark')
# p2 = Player('Steve')

# p1 = Player('Mark')
# p1.formerTeam.append('barcelona')
# p2 = Player('Steve')
# p2.formerTeam.append('chelesa')

# print("Name :",p1.name)
# print("Team Name:",p1.teamName)
# print(p1.formerTeam)
# print("---------"*6)
# print("Name :",p2.name)
# print("Team Name:",p2.teamName)
# print(p2.formerTeam)

#---------------------------------------------------------------------------
#using class variables smartly

print("-- ######## --    "*5)
class Player:
    teamName = 'Liverpool'              # class variable
    teamMembers = []
    
    def __init__(self,name) -> None:
        self.name  = name               # creating instance variables
        self.formerTeam = []
        self.teamMembers.append(self.name)


p1 = Player('Mark')
p2 = Player('Steve')

print("Name :",p1.name)
print("Team Members:",p1.teamMembers)

print("---------"*6)
print("Name",p2.name)
print("Team Members:",p2.teamMembers)

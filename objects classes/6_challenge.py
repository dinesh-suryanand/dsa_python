class Student:
    def __init__(self,name,phy,che,bio) -> None:
        self.name = name
        self.phy = phy
        self.che = che
        self.che = bio
    
    def totalObtained(self):
        return (self.phy + self.che + self.bio)

    def percentage(self):
        return ((self.totalObtained()/300)*100)

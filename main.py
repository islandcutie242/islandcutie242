class Robot:
    # creating a custom constructor
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    
    def introduce_self(self):
        print("Hello my name is "+ self.name)
    
# r1 = Robot()
# r1.name = "Tim"
# r1.color = "silver"
# r1.weight = 40

#r2 = Robot()
#r2.name = "Sara"
# r2.color = "bronze"
# r2.weight = 34

r1 = Robot("Tim","silver", 56)
r2 = Robot("Sara","bronze", 34)

r2.introduce_self()
#INHERITANCE OOP
class Parent():                                     #Super Class
    def __init__(self, LastName, EyeColor):         #Constructor
        print("Parent Constructor Called")
        self.LastName  = LastName
        self. EyeColor = EyeColor

    def ShowINFO(self):                             #First Method
        print("Last Name Is: " + self.LastName)
        print("Eye Color Is: " + self.EyeColor)

class Child(Parent):                                #Sub Class Inherit From Super Class [Parent]
    def __init__(self, LastName, EyeColor, NumOfToys):
        print("Child Constructor Called")
        Parent.__init__(self, LastName, EyeColor)   #Constructor Of Super Class
        self.NumOfToys = NumOfToys

    def ShowINFO(self):                             #Same Name Of First Method [Over Riding]
        print("Last Name Is: " + self.LastName)
        print("Eye Color Is: " + self.EyeColor)
        print("Number Of Toys Is: " + str(self.NumOfToys))

DAD = Parent("Gamal", "Brown")
DAD.ShowINFO()

SON = Child("Mohamed", "Black" , 5)
SON.ShowINFO()

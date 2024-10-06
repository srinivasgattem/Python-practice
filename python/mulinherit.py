class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name of employee is {self.name}") 
class dance:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the type of dance:{self.dance}")   
class danceremployees(dance,employee):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name 
emp1=danceremployees("srinivas","hip-pop") 
emp1.show()                        
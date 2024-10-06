class employee:
    def __init__(self,name, id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"name of employee is {self.name} and his id no is {self.id} ")
    def __str__(self):
            return f"the name of the employee is {self.name} and her id no is {self.id}" 
    def __call__(self):
        print("hello employees")       
class programmer(employee):
    def showskills(self):
     print(f"employee with id no {self.id} is having java skills")     

e1=programmer("srinivas",1692)
e1.showdetails()
e1.showskills()
e1()
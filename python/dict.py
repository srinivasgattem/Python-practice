class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.occupation="software developer"
class programmer(person):
         def __init__(self, name, age, lang):
          super().__init__(name,age)
          self.lang=lang
                
p = programmer("srinivas","24","python") 
print(p.name)
print(p.age)
print(p.lang)
#print(p.__dict__) 
#print(dir(p))  
#print(help(p))
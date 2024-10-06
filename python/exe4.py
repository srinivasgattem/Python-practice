class library:
    def __init__(self):
       self.noofbooks=0
       self.books=[]
    def addbook(self,book):
       self.books.append(book)
       self.noofbooks=len(self.books)
    def showdetails(self):
     print(f"the library has {self.noofbooks} books.the books are{self.books}")
        
l1=library()
l1.addbook("bhagavath gita")
l1.addbook("ramayanam")
l1.addbook("harrypotter") 
l1.showdetails()   
             
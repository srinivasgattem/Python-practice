class person:
    name="srinivas"
    enrollment_num="A2305221692"
    department="computer science"
    def info(self):
        print(f"{self.name} belongs to {self.department} department")
    
e=person()
print(e.name)
e.info()


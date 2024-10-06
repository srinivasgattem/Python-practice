def greet(fx):
    def mfx(*args,**kwargs):
     print("hello sir")    
     fx(*args,**kwargs)
    print("good morning")
    return mfx

@greet
def hello():
      print("hello world")
@greet
def add(a,b):
 print(a+b)

hello()
add(2,3)
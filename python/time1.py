import time
def usingfor():
    for i in range(5000):
        print(i)
def usingwhile():
    i=0
    while i<5000:
        i=i+1  
        print(i)
init=time.time()     
usingfor()  
t1=time.time()-init
init=time.time() 
usingwhile()
print(time.time()-init)
print(t1)     
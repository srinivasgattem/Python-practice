num=input("enter the number :")
try:
     print(f"multiplication of {num} is:")
     for i in range(10):
         print(f"{num} * {i} = {int(num)*i}") 
except:
    print("enter only numbers")  
    print("invalid input")       
    
finally:
    print("i will get executed even if error occurs or doesnt")    
    
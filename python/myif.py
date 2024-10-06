num=int(input("enter the number"))
print("given number is ", num)
if(num<0):
    print("given number is negative")
elif(num>0):
    if(num<=10):
     print("given number is between 1 to 10")
    elif(num>10 and num<=20):
      print("given number is between 11 to 20")
    else:
        print('given number is greter than 20')
        
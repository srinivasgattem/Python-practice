#def sum_of_binary_digits(n):
 #   binary_representation=bin(n)[2:]
    
  #  sum_of_digits=sum(int(digit)for digit in binary_representation)
   # return sum_of_digits  
#n=1111
#result=sum_of_binary_digits(n)
#print(result)
x= int(input())
binary=bin(x)[2:]
amount=0
for b in binary:
    if b=='1':
        amount+=1
print(amount)        
    
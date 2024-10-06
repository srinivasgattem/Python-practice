def count_magical_numbers(n):
    count=0
    for i in range(1,n+1):
        if i%3==0 or i%5==0:
            count+=1
    return count
n=int(input("enter a number:"))
result=count_magical_numbers(n)
print(f"number of magical numbers between 1 and {n} is :{result}")        
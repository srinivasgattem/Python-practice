def missing_number(n,arr):
    hash=[0]*(n+1)
    for num in arr:
       hash[num]+=1
    for i in range(1,n+1):
        if hash[i]==0:
            return i
    return -1
arr=[1,2,3,5,7,4,6,8,9,10]
n=10
print(missing_number(n,arr))        
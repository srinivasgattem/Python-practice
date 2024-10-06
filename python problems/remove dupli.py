def remove_duplicates(arr,n):
    if n==0 or n==1:
        return n
    arr.sort();
    temp=list(range(n))
    j=0
    temp[j]=arr[0]  
    j+=1
    for i in range (1,n):
        if arr[i]!=arr[i-1]:
            temp[j]=arr[i]
            j+=1
    for i in range(0,j):
        arr[i]=temp[i]
    return j        
arr=[1,2,2,3,4,4,4,5,5,6,7]
n=len(arr)
remove_duplicates(arr,n)
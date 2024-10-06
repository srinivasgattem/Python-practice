def evenoddsum(arr,n):
    even=0
    odd=0
    for i in range(n):
        if i %2==0:
            even+=arr[i]
        else:
            odd+=arr[i]
    print("even index positions sum",even)
    print("odd index positions sum",odd)   
arr=[1,2,3,4,5,6]
n=len(arr)
evenoddsum(arr,n)            
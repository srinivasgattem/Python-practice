def largest(arr,n):
    mx=arr[0]
    for i in range (1,n):
        if arr[i]>mx:
            mx=arr[i]
    return mx
if __name__=='__main__':
 arr=[10000,324,45,90,98]
 n=len(arr)
ans=largest(arr,n)
print("largest element in the array is:",ans)
            
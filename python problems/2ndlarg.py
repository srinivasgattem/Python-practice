def secondlargest(arr,arr_size):
    arr.sort(reverse=True)
    if arr_size<2:
        return None
    else:
        return print("second largest element is",arr[1])
   # for i in range(1,arr_size):
    #    if (arr[i]!=arr[0]):
     #       print("the second largest element is:",arr[i])
      #      return
    pri#nt("there is no second element found")  
arr=[12,35,1,10,34,1] 
n=len(arr)
secondlargest(arr,n)  
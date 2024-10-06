def merge_arrays(arr1,arr2):
    i=0
    j=0
    merged_array=[]
    while i<len(arr1) and j<len(arr2):
        if(arr1[i]<arr2[j]):
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while j<len(arr2):
        merged_array.append(arr2[j])
        j+=1
    return merged_array
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge=merge_arrays(arr1,arr2)
print("merged array is:",merge)                         
def intersection(arr1,arr2):
    set1=set(arr1)
    set2=set(arr2)
    result=[]
    for num in set2:
        if num in set1:
            result.append(num)
    return result        
    #intersection=set1.intersection(set2)
    #return intersection
arr1=[1,2,3,4,5]
arr2=[4,5,6,7,8]
print("intersection of two arrays is :",intersection(arr1,arr2))
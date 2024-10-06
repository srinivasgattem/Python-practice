def removeduplicates(arr):
    unique_element=[]
    for element in arr:
        if element not in unique_element:
            unique_element.append(element)
    return unique_element
arr=[1,1,2,3,3,4,5,6,6,6,7]
print("after removing duplicates from array:",removeduplicates(arr))       
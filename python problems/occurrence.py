def count_occurrences(arr):
    occurrences_dict={}
    for element in arr:
        if element in occurrences_dict:
            occurrences_dict[element]+=1
        else:
            occurrences_dict[element]=1
    return occurrences_dict
arr=[1,1,2,2,2,3,4,5,5,5,5,6,6,7,7,7,7,7,7]       
occurrences =count_occurrences(arr)
for element,count in occurrences.items():
    print(f"element {element} occurs {count} times")     
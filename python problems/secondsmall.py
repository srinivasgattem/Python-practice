def second_smallest_element(arr):
    unique_elements=list(set(arr))
    unique_elements.sort()
    if len(unique_elements)<2:
        return None
    else:
        return unique_elements[1]
arr=[8,3,4,6,2]
second_smallest=second_smallest_element(arr)
if second_smallest:
    print(second_smallest)
else:
    print("there is no second smallest element")        
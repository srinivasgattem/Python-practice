def longest_decreasing_subarray(arr):
    if len(arr)==0:
        return 0
    cur_len=1
    max_len=1
    for i in range (1,len(arr)):
        if arr[i]<arr[i-1]:
            cur_len+=1
        else:
            max_len=max(max_len,cur_len)
            cur_len=1
    max_len=max(max_len,cur_len)
    return max_len
arr=[4,8,7,3,4,2,1] 
result=longest_decreasing_subarray(arr)
print(f"longest decreasing subarray is:{result}")                
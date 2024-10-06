def second_highest_count(B):
    highest=B[-1]
    for i in range(len(B)-2,-1,-1):
        if B[i]!=highest:
            second_highest=B[i]
            break
    else:
        return 0
    count=B.count(second_highest)
    return count
B=[1,2,3,4,4,5,5,5]
print(second_highest_count(B))        
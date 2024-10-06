def longestuniquesubstr(s):
    n=len(s)
    res=0
    for i in range (n):
        visited=[False]*256
        for j in range(i,n):
            if visited[ord(s[j])]==True:
                break
            else:
                res=max(res,j-i+1)
                visited[ord(s[j])]=True
    return res
if __name__=="__main__":
    s="geeksforgeeks" 
    print(longestuniquesubstr(s))           
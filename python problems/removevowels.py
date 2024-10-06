def modify_str(s):
    vowels='aeiouAEIOU'
    modified_str=s[0]
    for i in range(1,len(s)-1):
        if s[i]  in vowels and s[i-1]  not in vowels and s[i+1] not in vowels:
            continue
        modified_str+=s[i]
    modified_str+=s[-1]
    return modified_str
s=input("enter a string ")
result=modify_str(s)
print("modified string after removing vowels is:"+result)    
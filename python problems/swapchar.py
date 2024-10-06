def swap(user_input,str1,str2):
    result=' '
    if user_input!=0:
        result=user_input.replace(str1,'*').replace(str2,str1).replace('*',str2)
        return result
    return 'NULL'
user_input=input()
str1,str2=map(str,input().split())
print(swap(user_input,str1,str2))
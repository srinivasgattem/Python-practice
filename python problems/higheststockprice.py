def highest_stock_price(sto):
    n=len(sto)
    res=[0]*n
    stack=[]
    for i in range (n):
        while stack and sto[i]>sto[stack[-1]]:
            prev_day=stack.pop()
            res[prev_day]=i-prev_day
        stack.append(i)
    return res
#n=int(input())
sto = [73, 74, 75, 71, 69, 72, 76, 73]
res = highest_stock_price(sto)
#sto=list(map(int,input.split()))
#result=highest_stock_price(sto)
print(" ".join(map(str,res)))        
            
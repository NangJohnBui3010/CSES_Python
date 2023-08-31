a = str(input())
res = 1
c = 1
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        c+=1
        res = max(res,c)
    else:
        c = 1
print(res)
    

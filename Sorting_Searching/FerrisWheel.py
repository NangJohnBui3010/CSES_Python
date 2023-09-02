n,x = map(int,input().split())
arr = list(sorted(map(int,input().split())))
i = 0; j = n-1; ctr = 0
while(i<=j):
    if arr[i] + arr[j] <= x:
        ctr+=1; i+=1; j-=1
    else:
        ctr+=1; j-=1
print(ctr)
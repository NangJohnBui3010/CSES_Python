def Increase(n,arr):
    ctr = 0
    if n == 1:
        return 0
    for i in range(1,n):
        diff = arr[i-1] - arr[i]
        if diff > 0:
            arr[i] += diff
            ctr += diff
    return ctr
        
n = int(input())
arr = list(map(int, input().split()))
print(Increase(n,arr))

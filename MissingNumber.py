def findMissingNumber(n,arr,dict):
    for x in arr:
        dict[x] = 1
    for x in dict.keys():
        if dict[x] == 0:
            return x

dict = {}
n = int(input())
for i in range(1,n+1):
    dict[i] = 0
arr = list(map(int, input().split()))
print(findMissingNumber(n,arr,dict))

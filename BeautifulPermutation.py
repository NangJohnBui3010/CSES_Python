odd = []; even = []
n = int(input())
if (1<n<=3):
    print("NO SOLUTION")
else:
    for x in range(1,n+1):
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    for i in even:
        print(i,end = " ")
    for i in odd:
        print(i,end = " ")
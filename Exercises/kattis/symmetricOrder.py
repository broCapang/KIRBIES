import math


n=1
a=0
n=int(input())
while(n!=0):
    a+=1
    size=n
    ans = ["" for _ in range(n)]

    for i in range(math.floor(n/2)):
        ans[i] = input()
        ans[size-1] = input()
        size-=1
    
    if(n%2!=0):
        ans[math.floor(n/2)]=input()
    print("SET",a)

    for items in ans:
        print(items)

    n=int(input())


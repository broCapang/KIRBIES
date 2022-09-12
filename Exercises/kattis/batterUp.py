n = int(input())

x = list(map(int,input().split()))
bro=0.0
for i in x:
    if i<0:
        n-=1
        continue
    bro+=i

print(bro/n)
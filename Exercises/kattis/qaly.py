T = int(input())
ans=0.0
for _ in range(T):
    a,b = list(map(float,input().split()))   
    ans+=a*b
print(ans)

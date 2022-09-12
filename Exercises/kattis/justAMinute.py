n = int(input())
sumS = 0
sumM = 0
for _ in range(n):
    min, sec = list(map(int,input().split()))
    sumM+=min*60
    sumS+=sec

if(sumM >= sumS):
    print("measurement error")
else:
    print(float(sumS/sumM))
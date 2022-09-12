
n = int(input())
x = list(map(int,input().split()))

x.sort()

daysUntilParty = 2
daysRemain = 0
i = 0

for days in range(n-1,-1,-1):
    x[days] -= n-i
    daysUntilParty+=1
    i+=1

for days in range(n-1,-1,-1):
    if(x[days] > daysRemain):
        daysRemain=x[days]

daysUntilParty+=daysRemain
print(daysUntilParty)


    

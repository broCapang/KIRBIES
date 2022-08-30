volume = 7

n = int(input())

for i in range(n):
    o = input()
    if("Skru op!" in o):
        if(volume==10):
            continue
        else:
            volume+=1
    elif("Skru ned!" in o):
        if(volume==0):
            continue
        else:
            volume-=1
print(volume)


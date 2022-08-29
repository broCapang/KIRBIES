# do T 

T=int(input())
for case in range(T):
    N = int(input())
    iB = 0
    busRange = list(map(int,input().split()))
    bus = [[0 for i in range(2)] for j in range(N)]


    for a in range(N):
        for b in range(2):
            bus[a][b]=busRange[iB]
            iB+=1
    iB=0
    P = int(input())
    ans = [0 for i in range(P)]

    for a in range(P):
        C=int(input())
        for b in range(N):
            # print(C in range(bus[a][0],bus[a][1]+1))
            if(C in range(bus[b][0],bus[b][1]+1)):
                ans[a]+=1

    print('Case #{}:'.format(case+1), end=" ")
    for item in ans:
        print(item, end=" ")
    print()
    if(case<T-1):
        input()



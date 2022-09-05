
R, C, Zr, Zc = list(map(int,input().split()))

ans = [["" for _ in range(C)] for _ in range(R)]
ans2 = [["" for _ in range(C*Zc)] for _ in range(R*Zr)]


for i in range(R):
    word = input()
    ans[i] = list(word)
z=0
for i in range(R):
    
    for j in range(Zr):
        
        for k in range(C):
            
            for l in range(Zc):
                print(ans[i][k],end="")
        print()

                
                



    





    





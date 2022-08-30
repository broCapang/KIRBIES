N, B = input().split()
dominant = dict()
nonDominant = dict()
number = ["A","K","Q","J","T","9","8","7"]
dominant["A"]=11
nonDominant["A"]=11
dominant["K"]=4
nonDominant["K"]=4
dominant["Q"]=3
nonDominant["Q"]=3
dominant["J"]=20
nonDominant["J"]=2
dominant["T"]=10
nonDominant["T"]=10
dominant["9"]=14
nonDominant["9"]=0
dominant["8"]=0
nonDominant["8"]=0
dominant["7"]=0
nonDominant["7"]=0

ans = 0
for n in range(4*int(N)):
    P = input()
    if(P[1]==B):
        
        for item in number:
            if(item==P[0]):
                ans+=dominant[P[0]]
            
    
    else:
        
        for item in number:
            if(item==P[0]):
                ans+=nonDominant[P[0]]

print(ans)
            


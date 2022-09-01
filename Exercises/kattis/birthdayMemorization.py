
#  TODO : BIRTHDATE AS SET NAME AND RANK AS DICT 



n = int(input())

birthdate = set()
name = dict()
rank = dict()



for i in range(n):
    bro = input().split()
    if(bro[2] not in birthdate):
        birthdate.add(bro[2])
        name[bro[2]]=bro[0]
        rank[bro[2]]=bro[1]
    elif(int(rank[bro[2]])<int(bro[1])):
        name[bro[2]]=bro[0]
        rank[bro[2]]=bro[1]
    
print(len(birthdate))
ans=""
for i in birthdate:
    ans+=(name[i])
    ans+=(" ")

ans= ans.split()
ans.sort()
print("\n".join(ans))


    
    


    
    



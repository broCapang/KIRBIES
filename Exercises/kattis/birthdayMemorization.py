
#  TODO : BIRTHDATE AS SET NAME AND RANK AS DICT 



n = int(input())

birthdate = ["" for i in range(n)]
name = ["" for i in range(n)] 
rank = [0 for i in range(n)] 
value = dict()
max = -1

dateToRem = ""


for i in range(n):
    bro = input().split()
    name[i] = bro[0]
    rank[i] = int(bro[1])
    birthdate[i] = bro[2]
    if(max<int(rank[i])):
        max = rank[i]
        dateToRem = bro[2]
    

for i in range(n):
    if(dateToRem != birthdate[i]):
        continue
    else:
        print(name[i])
    


    
    



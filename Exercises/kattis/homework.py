bro = input()

if(';' in bro):
    bro = bro.split(';')
ans = 0
if(type(bro)==list):
    for i in bro:
        if('-' in i):
            i = i.split('-')
            ans+= (int(i[1])-int(i[0]))+1
        else:
            ans+=1

if(type(bro) == str):
    if('-' in bro):
        bro = bro.split('-')
        ans+= (int(bro[1])-int(bro[0]))+1
    else:
        ans+=1
print(ans)

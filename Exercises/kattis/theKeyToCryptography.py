a= input()
key = input()
p=0
ans=''
for i in range(len(a)):
    c= ord(a[i])-65
    if (i<len(key)):
        d= ord(key[i])-65
    else:
        d= ord(ans[p])-65
        p+=1
    ans+=chr(((c-d)%26)+65)
print(ans,end='')



a = input()
a = list(a)

ans = ""
i=0
while i<len(a):
    if(a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u'):
        ans+=a[i]
        del a[i+1:i+3]
    else:
        ans += a[i]
    i+=1

print(ans)

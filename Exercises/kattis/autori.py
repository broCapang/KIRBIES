p = input()
ans=""

if("-" in p):
    p = p.split("-")
    for i in range(len(p)):
        characters = list(p[i])
        ans+=characters[0]
    print(ans)

else:
    print(p[0])


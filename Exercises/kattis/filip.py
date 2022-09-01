def out(a):
    for m in range(3):
        print(a[2-m],end="")

x, y = input().split()
x = x[::-1]
y = y[::-1]
print(x,y)


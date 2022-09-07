N = int(input())
M = int(input())

a=M//N
b=M%N
for i in range(b):
    for i in range(a+1):
        print("*",end="") 
    print()
for i in range(N-b):
    for i in range(a):
        print("*",end="") 
    print()
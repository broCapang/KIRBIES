a = ["A","B","C"]
b = ["B","A","B","C"]
c = ["C","C","A","A","B","B"]

n = int(input())

ans = input()
value = dict()
A = 0
B = 0
C = 0
for i in range(len(ans)):
    if(a[i%3] == ans[i]):
        A+=1
    if(b[i%4] == ans[i]):
        B+=1
    if(c[i%6] == ans[i]):
        C+=1
maximum = max(A,B,C)
print(maximum)
if(A == maximum):
    print("Adrian")
if(B == maximum):
    print("Bruno")
if(C == maximum):
    print("Goran")


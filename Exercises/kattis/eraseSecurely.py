n = int(input())

a = input()

b=list(a)
if n%2!=0:
    for i in range(len(b)):
        if(b[i]=="0"):
            b[i]="1"
        else:
            b[i]="0"

c=input()
if c == "".join(b):
    print("Deletion succeeded")
else:
    print("Deletion failed")

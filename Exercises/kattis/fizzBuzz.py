x, y, z = list(map(int,input().split()))

for n in range(1,z+1):
    if(n%x==0 and n%y==0):
        print("FizzBuzz")
    elif(n%x==0):
        print("Fizz")
    elif(n%y==0):
        print("Buzz")
    else:
        print(n)

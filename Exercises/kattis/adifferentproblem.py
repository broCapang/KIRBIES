from sys import stdin

for line in stdin:
    if line == '': # If empty string is read then stop the loop
        break
    x,y=map(int, line.split())
    print(abs(x-y))
    


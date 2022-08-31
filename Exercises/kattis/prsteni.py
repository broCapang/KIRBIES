from fractions import Fraction
n = int(input())

rings = list(map(int, input().split()))

for i in range(len(rings)-1):
    if('/' in str(Fraction(rings[0],rings[i+1]))):
        print(Fraction(rings[0],rings[i+1]))
    else:
        print("{}/1".format(Fraction(rings[0],rings[i+1])))
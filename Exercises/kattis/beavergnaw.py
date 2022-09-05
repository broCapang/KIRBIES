import math

D,V = list(map(float,input().split()))


R=float(D/2.0)

while(D != 0 or V!=0):
    wood=(math.pi*pow(R,2)*D)-V
    bigCones = math.pi*pow(R,2)*(D/3)
    shape = wood - bigCones
    cylinder = shape * 1.5
    print(pow((cylinder/(2*math.pi)),(1.0/3))*2)
    D,V = list(map(float,input().split()))
    R=D/2




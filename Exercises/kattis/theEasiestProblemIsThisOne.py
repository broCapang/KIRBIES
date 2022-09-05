
def sumDigit(digit):
    sum = 0
    while(digit>0):
        sum = sum + digit%10
        digit = digit//10
    return sum


def main():

    N = int(input())

    while(N!=0):
        sumN = sumDigit(N)
        for p in range(11,100001):
            if(sumDigit(p*N) == sumN):
                print(p)
                break
        N = int(input())

main()


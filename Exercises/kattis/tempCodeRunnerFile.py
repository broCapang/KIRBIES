import random
import string


n = int(input())

alphabets = list(string.ascii_lowercase)
vowels = ['a','e','i','o','u']
consonants = list(set(alphabets)-set(vowels))

for _ in range(n):
    length = random.randint(3,20)
    v,c = 0,0
    bro = ""
    for _ in range(length):
        if(random.randint(0,1)==1):
            if(v<2):
                v+=1
                c=0
                bro+=(random.choice(consonants))
            else:
                c+=1
                v=0
                bro+=(random.choice(vowels))
        else:
            if(v<2):
                v+=1
                c=0
                bro+=(random.choice(consonants))
            else:
                c+=1
                v=0
                bro+=(random.choice(vowels))
            
    print(bro)


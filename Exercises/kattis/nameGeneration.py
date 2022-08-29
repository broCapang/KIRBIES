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
        a=random.randint(0,1)
        if(length==3):
            if(a==1):
                bro+=(random.choice(consonants))
            else:
                bro+=(random.choice(vowels))
        else:
            if(a==1):
                if(v<2):
                    v+=1
                    c=0
                    bro+=(random.choice(consonants))
                else:
                    c+=1
                    v=0
                    bro+=(random.choice(vowels))
            else:
                if(c<1):
                    c+=1
                    v=0
                    bro+=(random.choice(vowels))
                    
                else:
                    v+=1
                    c=0
                    bro+=(random.choice(consonants))

    if(length==len(bro)):
        print(bro)
    else:
        for _ in range(length-len(bro)):
            a=random.randint(0,1)
            if(length==3):
                if(a==1):
                    bro+=(random.choice(consonants))
                else:
                    bro+=(random.choice(vowels))
            else:
                if(a==1):
                    if(v<2):
                        v+=1
                        c=0
                        bro+=(random.choice(consonants))
                    else:
                        c+=1
                        v=0
                        bro+=(random.choice(vowels))
                else:
                    if(c<1):
                        c+=1
                        v=0
                        bro+=(random.choice(vowels))
                        
                    else:
                        v+=1
                        c=0
                        bro+=(random.choice(consonants))
        print(bro)

    


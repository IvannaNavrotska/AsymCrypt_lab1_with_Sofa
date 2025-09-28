import random

def x11(k):
    x=[]
    for _ in range(10):
        x.append(random.randint(0, 1))

    if 1 not in x:
        x[random.randint(0, 10)]=1

    for t in range(10, k+10):
        
        x.append(x[t-11]^x[t-9])

    return x

def y9(k):
    y=[]
    for _ in range(8):
        y.append(random.randint(0, 1))

    if 1 not in y:
        y[random.randint(0, 8)]=1

    for t in range(0, k):
        
        y.append(y[t]^y[t+1]^y[t+3]^y[t+4])

    return y

def s10(k):
    s=[]
    for _ in range(10):
        s.append(random.randint(0, 1))

    if 1 not in s:
        s[random.randint(0, 10)]=1

    for t in range(0, k):
        
        s.append(s[t]^s[t+3])

    return s



def jiffi():
    k=random.randint(1000, pow(2, 20)-1)
    x=x11(k)
    y=y9(k)
    s=s10(k)
    z=[]
    for i in range(k):
        if s[i]==1:
            z.append(x[i])
        else:
            z.append(y[i])

    return z



c=int("".join(str(x) for x in jiffi()), 2)
print(hex(c)) #Ну дуже багато циферок виходить, прям рілі багато
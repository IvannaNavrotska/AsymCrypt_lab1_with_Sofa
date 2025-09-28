import random

def l89():
    x=[]
    for _ in range(89):
        x.append(random.randint(0, 1))

    if 1 not in x:
        x[random.randint(0, 89)]=1
    
    k=random.randint(1000, pow(2, 20)-1)

    for t in range(89, k+89):
        
        x.append(x[t-38]^x[t-89])


    return x

c=int("".join(str(x) for x in l89()), 2)
print(hex(c)) #Ну дуже багато циферок виходить, прям рілі багато
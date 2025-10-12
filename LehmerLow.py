import math
import random


def lehmerlow(a:int, c:int, m:int, x0:int):
    n=125
    m=pow(2, 32)
    a=pow(2, 16)+1
    c=119
    x0=random.randint(1, m-1)
    x=x0
    if math.gcd(c, m)!=1:
        return 0
    for _ in range(n):
        x=(a*x+c)%m

    k=x.bit_length()

    
    return x&0xFF




m=pow(2, 32)
a=pow(2, 16)+1
c=119
x0=random.randint(1, 1000)
#print(lehmerlow(a, c, m, x0))


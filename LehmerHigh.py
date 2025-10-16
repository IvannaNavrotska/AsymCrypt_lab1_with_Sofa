import math
import random


def lehmerhigh(a:int, c:int, m:int, x0:int, k):
    if k%8!=0:
        return 0
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
    arr=[]
    for _ in range(int(k/8)):
        n=x.bit_length()
        b=(x>>24)
        arr.append(b)
        x=(a*x+c)%m

    '''n=x.bit_length()
    if n>32:
        print(n)
    x=(x>>24)'''
    

    return arr




m=pow(2, 32)
a=pow(2, 16)+1
c=119
k=1000
x0=random.randint(1, m-1)
#print(lehmerhigh(a, c, m, x0, k))
#print(a, m, c, x0)

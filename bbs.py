import random

def bbs(p, q, k):
    if (k%32!=0):
        return 0
    n=p*q
    r=random.randint(2, n-1)
    x=[]
    arr=[]
    for _ in range(int(k/32)):
     x=[]
     for _ in range(32):
        f=r%2
        x.append(f)
        r=pow(r, 2, n)
     arr.extend(x)
    

    return arr

p = int(0xD5BBB96D30086EC484EBA3D7F9CAEB07)
q = int(0x425D2B9BFDB25B9CF6C416CC6E37B59C1F)


#print(bbs(p, q, 1000000)) 

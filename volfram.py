import random
import time
def volfram(r:int):
    x=[]
    k=32
    l=0xFFFFFFFF
    for _ in range(k):
        x.append(r%2)
        r=(r <<1)^(r |(r>>1))
        r=r&l
    return x








g = random.randint(1, pow(2, 32))
#c=int("".join(str(x) for x in volfram(g)), 2)
#print(int(c), g, volfram(g))

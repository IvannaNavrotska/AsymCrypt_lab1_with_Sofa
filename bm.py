import random

def proverka_x(t, p):
    if t<((p-1)/2):
        return 1
    else:
        return 0
    
def bm(a, p, k):
    t=random.randint(0, p-1)
    dlinna=32-1
    arr=[]
    for _ in range(int(k/32)):
        x=[]
        x.append(proverka_x(t, p))
        for _ in range(dlinna):
            t=pow(a, t, p)
            x.append(proverka_x(t, p))
        arr.append(x)
    return arr

p=int(0xCEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3)
a=int(0x5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356)
#print(bm(a, p, 1000000))
    

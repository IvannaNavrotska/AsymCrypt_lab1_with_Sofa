import random


    
def bm_bayts(a, p):
    # на виході список з чисел до 255 включно
    t=random.randint(0, p-1)
    x=[]
    k=int((256*t)//(p-1))
    x.append(k)
    dlinna=32-1


    for _ in range(dlinna):
        t=pow(a, t, p)
        k=int((256*t)//(p-1))
        x.append(k)
    return x

p=int(0xCEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3)
a=int(0x5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356)
#print(bm_bayts(a, p))

    

import random

def test1(y): #рівноімовірність знаків

    #H0 - всі байти рівноімовірні

    m = len(y)
    nj = m/256

    for_vj = {}
    for i in y:
        for_vj[i] = for_vj.get(i, 0) + 1

    xi_2 = 0
    
    for j in range(256):
        vj = for_vj.get(j, 0)
        xi_2 += (vj - nj)**2 / nj

    alpha = 0.05
    l = 255
    z = 1.645   
    xi2_lim = ((2*l)**(1/2))*z + l

    if xi_2 <= xi2_lim:
        return print("Гіпотеза H0 вірна, знаки рівноімовірнісні")
    else:
        return print("Гіпотеза H0 хибна, знаки нерівноімовірнісні")

 
y = [random.randint(0, 255) for i in range(10000)]
test1(y)  

y = [0 if random.random() < 0.2 else random.randint(1, 255) for i in range(10000)]
test1(y)  


import random

def test3(y): #однорідність послідовності

    #H0 - послідовність однорідна

    r = 10
    m = len(y)
    m_ = m // r
    n = m_ * r

    r_ = [y[i*m_:(i+1)*m_] for i in range(r)]

    vij = [[0]*r for k in range(256)]  
    vi = [0]*256                    
    aj = [0]*r                   

    for j, r_i in enumerate(r_):
        aj[j] = len(r_i)
        for b in r_i:
            vij[b][j] += 1
            vi[b] += 1
   

    sum_ = 0
    for i in range(256):
        for j in range(r):
            if vi[i] > 0 and aj[j] > 0:
                sum_ += (vij[i][j] ** 2) / (vi[i] * aj[j])
    xi_2 = n * (sum_ - 1)

    alpha = 0.05
    l = 255*(r-1)
    z = 1.645   
    xi2_lim = ((2*l)**(1/2))*z + l

    if xi_2 <= xi2_lim:
        return print("Гіпотеза H0 вірна, послідовність однорідна")
    else:
        return print("Гіпотеза H0 хибна, послідовність неоднорідна")


y = [random.randint(0, 255) for i in range(5000)]
test3(y)

y = [random.randint(0, 255) for i in range(2500)] + \
           [random.randint(0, 50) for i in range(2500)]
test3(y)




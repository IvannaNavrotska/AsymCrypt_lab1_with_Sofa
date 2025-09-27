import random

def test2(y): #незалежність сусідніх знаків

    #H0 - байти незалежні між собою

    m = len(y)
    n = m // 2

    y1_y2 = [(y[2*i], y[2*i+1]) for i in range(n)]

    vij = [[0]*256 for k in range(256)]
    vi = [0]*256
    aj = [0]*256

    for b1,b2 in y1_y2:
        vij[b1][b2] += 1
        vi[b1] += 1
        aj[b2] += 1

    sum_ = 0
    for i in range(256):
        for j in range(256):
            if vi[i] > 0 and aj[j] > 0:
                sum_ += (vij[i][j] ** 2) / (vi[i] * aj[j])
    xi_2 = n * (sum_ - 1)

    alpha = 0.05
    l = 255**2
    z = 1.645   
    xi2_lim = ((2*l)**(1/2))*z + l

    if xi_2 <= xi2_lim:
        return print("Гіпотеза H0 вірна, пари незалежні")
    else:
        return print("Гіпотеза H0 хибна, пари залежні")

y = [random.randint(0, 255) for i in range(10000)]
test2(y)

y = []
for i in range(5000):
    b = random.randint(0, 255)
    y.extend([b, b])  
test2(y)
   

"""
a = 0.01  z = 2.99
a = 0.05  z = 1.64
a = 0.1   z = 1.28
"""

import random
from sequences import *

def test1(y, z): #рівноімовірність знаків

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

    l = 255  
    xi2_lim = ((2*l)**(1/2))*z + l

    return xi_2, xi2_lim


def test2(y, z): #незалежність сусідніх знаків

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

    l = 255**2  
    xi2_lim = ((2*l)**(1/2))*z + l

    return xi_2, xi2_lim

def test3(y, z): #однорідність послідовності

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

    l = 255*(r-1) 
    xi2_lim = ((2*l)**(1/2))*z + l

    return xi_2, xi2_lim

    
def tests(alpha, seq=None, file=None):
    
    if file:                
        with open(file, 'rb') as f:
            data = list(f.read())
    else:                               
        if isinstance(seq, (bytes, bytearray)):
            data = list(seq)                  
        elif isinstance(seq, str):
            data = list(bytes.fromhex(seq))   
        else:
            data = list(seq) 

    if alpha == 0.01:
        z = 2.99
    elif alpha == 0.05:
        z = 1.64
    elif alpha == 0.1:
        z = 1.28

        
    print(f'Довжина послідовності: {len(data)}')
    print(f'Значення альфа: alpha = {alpha}\n')

    
    print('Виконується тест 1: перевірка рівноімовірності знаків')
    xi_2, xi2_lim = test1(data, z)
    print(f'xi_2 = {xi_2}, xi2_lim = {xi2_lim}')
    if xi_2 <= xi2_lim:
        print("Гіпотеза H0 вірна, знаки рівноімовірнісні\n")
    else:
        print("Гіпотеза H0 хибна, знаки нерівноімовірнісні\n")

        
    print('Виконується тест 2: перевірка незалежності сусідніх знаків')
    xi_2, xi2_lim = test2(data, z)
    print(f'xi_2 = {xi_2}, xi2_lim = {xi2_lim}')
    if xi_2 <= xi2_lim:
        print("Гіпотеза H0 вірна, пари незалежні\n")
    else:
        print("Гіпотеза H0 хибна, пари залежні\n")

  
    print('Виконується тест 3: перевірка однорідності послідовності')
    xi_2, xi2_lim = test3(data, z)
    print(f'xi_2 = {xi_2}, xi2_lim = {xi2_lim}')
    if xi_2 <= xi2_lim:
        print("Гіпотеза H0 вірна, послідовність однорідна\n")
    else:
        print("Гіпотеза H0 хибна, послідовність неоднорідна\n")

print('Тестування вбудованого генератора')
tests(0.01, sequence_from_vbud())

print('Тестування генератора LehmerLow')
tests(0.01, sequence_from_lehmerlow())

print('Тестування генератора LehmerHigh')
tests(0.01, sequence_from_lehmerhigh())


print('Тестування генератора L20')
tests(0.01, sequence_from_l20())

print('Тестування генератора L89')
tests(0.01, sequence_from_l89())

print('Тестування генератора Geffe')
tests(0.01, sequence_from_geffe())

print('Тестування генератора «Бібліотекар»')
tests(0.01, sequence_from_bibliotekar())

print('Тестування генератора Вольфрама')
tests(0.01, sequence_from_wolfram())

print('Тестування генератора Блюма-Мікалі BM')
tests(0.01, sequence_from_bm())

print('Тестування генератора BM_bytes')
tests(0.01, sequence_from_bm_bytes())

print('Тестування генератора BBS')
tests(0.01, sequence_from_bbs())

print('Тестування генератора BBS_bytes')
tests(0.01, sequence_from_bbs_bytes())

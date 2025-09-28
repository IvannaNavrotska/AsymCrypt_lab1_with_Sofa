import random
import math
from vud import vbud
from LehmerLow import lehmerlow
from LehmerHigh import lehmerhigh
from l20 import l20
from l89 import l89
from jifigeneratooring import jiffi
from bibliotecar import bibliot
from volfram import volfram
from bm import bm
from bmbayts import bm_bayts
from bbs import bbs
from bbs_bayt import bbs_bytes

#вбудований генератор вашої мови програмування
def sequence_from_vbud():
    vbud_seq = []

    while len(vbud_seq) != 125000:
        elt = vbud(0, 255)
        vbud_seq.append(elt)
    return vbud_seq


#генератор LehmerLow
def sequence_from_lehmerlow():

    lehmerlow_seq = []
    
    m=pow(2, 32)
    a=pow(2, 16)+1
    c=119
    x0=random.randint(1, 1000)
    
    while len(lehmerlow_seq) != 125000:
        elt = lehmerlow(a, c, m, x0)
        lehmerlow_seq.append(elt)
        
    return lehmerlow_seq


#генератор LehmerHigh
def sequence_from_lehmerhigh():

    lehmerhigh_seq = []
    
    m=pow(2, 32)
    a=pow(2, 16)+1
    c=119
    x0=random.randint(1, 1000)
    
    while len(lehmerhigh_seq) != 125000:
        elt = lehmerhigh(a, c, m, x0)
        lehmerhigh_seq.append(elt)
        
    return lehmerhigh_seq


#генератор L20
def sequence_from_l20():

    c = int("".join(str(x) for x in l20()),2)
    hex_str = str(hex(c))
    c_ = hex_str[2:]
    c_bytes = bytes.fromhex(c_)

    l20_seq = list(c_bytes)

    return l20_seq


#генератор L89
def sequence_from_l89():

    c = int("".join(str(x) for x in l89()),2)
    hex_str = str(hex(c))
    c_ = hex_str[2:]
    c_bytes = bytes.fromhex(c_)

    l89_seq = list(c_bytes)

    return l89_seq


#генератор Джиффі (Geffe)
def sequence_from_geffe():

    c=int("".join(str(x) for x in jiffi()), 2)
    hex_str = str(hex(c))
    c_ = hex_str[2:]
    c_bytes = bytes.fromhex(c_)

    geffe_seq = list(c_bytes)

    return geffe_seq


#генератор «Бібліотекар»
def sequence_from_bibliotekar():

    bibliotekar_seq = list(bibliot())

    return bibliotekar_seq


#генератор Вольфрама
def sequence_from_wolfram():

    
    wolfram_seq = []
    for _ in range(125000):   
        g = random.randint(1, pow(2, 32))             
        bits = volfram(g)               
        g = int("".join(str(b) for b in bits), 2)
        byte = int("".join(str(b) for b in bits[:8]), 2)
        wolfram_seq.append(byte)
        
    return wolfram_seq

#генератор Блюма-Мікалі BM
def sequence_from_bm():

    p=int(0xCEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3)
    a=int(0x5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356)
    
    bits = []
    total_bits = 125000 * 8

    while len(bits) < total_bits:
        bits.extend(bm(a, p))

    bm_seq = []
    for i in range(0, total_bits, 8):
        byte_bits = bits[i:i+8]
        v = int("".join(str(b) for b in byte_bits), 2)
        bm_seq.append(v)

    return bm_seq

#генератор BM_bytes (байтова модифікація генератору Блюма-Мікалі)
def sequence_from_bm_bytes():

    p=int(0xCEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3)
    a=int(0x5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356)
    
    bm_bytes_seq = []
    while len(bm_bytes_seq) < 125000:
        b = bm_bayts(a, p)
        bm_bytes_seq.extend(b)
        
    return bm_bytes_seq


#генератор BBS
def sequence_from_bbs():

    p = int(0xD5BBB96D30086EC484EBA3D7F9CAEB07)
    q = int(0x425D2B9BFDB25B9CF6C416CC6E37B59C1F)
    
    bits = []
    while len(bits) < 1000000:
        bits.extend(bbs(p, q))
    bits = bits[:1000000]

    bbs_seq = [int("".join(str(b) for b in bits[i:i+8]), 2) 
                 for i in range(0, len(bits), 8)]
    return bbs_seq


#генератор BBS_bytes (байтова модифікація генератору BBS)
def sequence_from_bbs_bytes():

    p = int(0xD5BBB96D30086EC484EBA3D7F9CAEB07)
    q = int(0x425D2B9BFDB25B9CF6C416CC6E37B59C1F)
    
    bbs_bytes_seq = []
    while len(bbs_bytes_seq) < 125000:
        b = bbs_bytes(p, q)
        bbs_bytes_seq.extend(b)
        
    return bbs_bytes_seq

import random

def bibliot():
    with open ("input.txt", "r", encoding="utf-8") as file:
        text=file.read()

    k=len(text)
    s=random.randint(0, k-100)
    bay=text[s:s+100]
    bay=bay.encode("utf-8")
    return bay


d=bibliot()
print(d)
bd=int.from_bytes(d, "big")
print(bd)

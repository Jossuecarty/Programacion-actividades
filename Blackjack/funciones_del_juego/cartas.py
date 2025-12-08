import random

PALOS = ["♠", "♥", "♦", "♣"]
NUMEROS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def crear_mazo():
    mazo = []
    for n in NUMEROS:
        for p in PALOS:
            mazo.append(n + p)
    random.shuffle(mazo)
    return mazo

def sacar_carta(mazo):
    return mazo.pop()

def sumar_mano(mano):
    total = 0
    ases = 0
    for carta in mano:
        num = carta[:-1]
        if num.isdigit():
            total += int(num)
        elif num in ("J","Q","K"):
            total += 10
        else:
            total += 11
            ases += 1
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1
    return total

def misma_carta(c1, c2):
    return c1[:-1] == c2[:-1]

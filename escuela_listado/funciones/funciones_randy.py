import random
ids= set()
def generar_id():
    while True:
        aid= random.randint(10000,99999)
        if aid not in ids:
            ids.add(aid)
            return aid

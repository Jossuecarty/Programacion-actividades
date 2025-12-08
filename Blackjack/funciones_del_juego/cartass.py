import os
import shutil

#esto es nomas para renombrar las cartas a valores que ya tenia del codigo, porque se llamaban ace_of_clubs y yo ocupaba A(y el simbolo)


# Carpeta donde están los PNG originales, tambien tienes que redireccionar a tu dispositivo la direccion de la carpeta
carpeta_origen = r"C:\Users\jossu\Desktop\cards\png"

# Carpeta destino en tu proyecto,tambien tienes que redireccionar a tu dispositivo la direccion de la carpeta
carpeta_destino = r"C:\Users\jossu\Desktop\BlackJack\Blackjack\funciones_del_juego\imageness\cartas"
os.makedirs(carpeta_destino, exist_ok=True)

# Mapear nombres de palos
mapa_palos = {
    "hearts": "♥",
    "diamonds": "♦",
    "clubs": "♣",
    "spades": "♠"
}

# Mapear valores
mapa_valores = {
    "ace": "A",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "10",
    "jack": "J",
    "queen": "Q",
    "king": "K"
}

# Iterar archivos
for archivo in os.listdir(carpeta_origen):
    if archivo.endswith(".png"):
        nombre, ext = os.path.splitext(archivo)
        if "_of_" in nombre:
            valor_raw, palo_raw = nombre.split("_of_")
            valor = mapa_valores.get(valor_raw.lower())
            palo = mapa_palos.get(palo_raw.lower())
            if valor and palo:
                nuevo_nombre = f"{valor}{palo}.png"
                shutil.copy(os.path.join(carpeta_origen, archivo),
                            os.path.join(carpeta_destino, nuevo_nombre))
                print(f"{archivo} -> {nuevo_nombre}")

print("¡Todas las cartas copiadas y renombradas!")

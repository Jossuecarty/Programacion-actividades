import os
import sys
import ctypes
#Crear una funcion para centrar la ventana.

def centrar_ventana(ventana,ancho,alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = int( (pantalla_ancho/2) - (ancho/2) )#Determina el centro de la pantalla horizantalmente
    y = int((pantalla_alto/2) - (alto/2) ) #Determina el centro de la pantalla verticalmente
    return ventana.geometry(f"{ancho}x{alto}+{x}+{y}") #WxH+X+Y

def resolver_ruta(ruta_relativa):
    if hasattr(sys,"_MEIPASS"):
        #Es un exe y buscar una carpeta temporal oculta
        return os.path.join(sys._MEIPAS,ruta_relativa)
    
    #Ejecutamos el archivo de python en desarrollo
    return os.path.join(os.path.abspath("."),ruta_relativa)

def cargar_fuente_memoria(ruta_fuente):
    path_fuente = resolver_ruta(ruta_fuente)

    #Llamar api de windows 
    gdi32 = ctypes.windll.gdi32
    ret = gdi32.AddFontResourceExW(path_fuente, 0x10, 0)

    if ret == 0:
        print(f"Error cargando la fuente: {ruta_fuente}")
    else:
        print(f"Fuente cargada correctamente")

import tkinter as tk
from tkinter import font, messagebox
from config import TITULO, COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_PANEL_PRINCIPAL
from util_ventana import centrar_ventana, cargar_fuente_memoria
from util_imagenes import leer_imagen
import pygame
import os

# y este es el main principal que agarra todos los codigos, y ya de ahi ejecuta donde esta el otro main



# Funciones de hover
def bind_hover_events(button):
    button.bind("<Enter>", lambda event: on_enter(event, button))
    button.bind("<Leave>", lambda event: on_leave(event, button))

def on_enter(event, button):
    button.config(bg="#0099CC")

def on_leave(event, button):
    button.config(bg=COLOR_MENU_LATERAL)

# Toggle del panel lateral
def toggle_panel():
    if menu_lateral.winfo_ismapped():
        menu_lateral.pack_forget()
    else:
        menu_lateral.pack(side=tk.LEFT, fill="y")

# Limpiar panel principal
def limpiar_panel(panel):
    for widget in panel.winfo_children():
        widget.destroy()

# Mostrar inicio
def mostrar_inicio():
    limpiar_panel(panel_principal)

    # Título del área
    titulo = tk.Label(panel_principal, text="Juegos del Casino", 
                      font=("Roboto", 20), bg=COLOR_PANEL_PRINCIPAL, fg="white")
    titulo.pack(pady=20)

    # Botón de Blackjack
    btn_blackjack = tk.Button(
        panel_principal,
        text="♠ Blackjack",
        font=("Roboto", 20),
        bg="#145A32",
        fg="white",
        width=15,
        height=2,
        command=abrir_blackjack
    )
    btn_blackjack.pack(pady=20)

# Salir de la app
def salir():
    root.destroy()

# Inicializar fuentes
cargar_fuente_memoria("./fuentes/Font Awesome 7 Brands-Regular-400.otf")
cargar_fuente_memoria("./fuentes/Font Awesome 7 Free-Regular-400.otf")
cargar_fuente_memoria("./fuentes/Font Awesome 7 Free-Solid-900.otf")

# Inicializar pygame 
pygame.init()

# Ventana principal
root = tk.Tk()
root.title(TITULO)

# Ícono
carpeta_base = os.path.dirname(os.path.abspath(__file__))
rutaIcono = os.path.join(carpeta_base, "imagenes", "BlackJack-logo.png")
icon = tk.PhotoImage(file=rutaIcono)
root.iconphoto(False, icon)

# Tamaño y centrado
centrar_ventana(root, 1024, 600)

# Barra superior
barra_superior = tk.Frame(root, height=50, bg=COLOR_BARRA_SUPERIOR)
barra_superior.pack(side=tk.TOP, fill="both")

# Menú lateral
menu_lateral = tk.Frame(root, width=150, bg=COLOR_MENU_LATERAL)
menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

# Panel principal
panel_principal = tk.Frame(root, bg=COLOR_PANEL_PRINCIPAL)
panel_principal.pack(side=tk.RIGHT, fill="both", expand=True)

# Fuente Font Awesome
fontawesome = font.Font(family="Font Awesome 7 Free", size=18)

#funciones de los juegos, aqui no va a funcionar en diferentes dispostivos porque tiene una ruta de mi computadora,a no ser que modifique esa ruta la de su dispositivo
def abrir_blackjack():
    ruta_juego = r"C:\Users\jossu\Desktop\BlackJack\Blackjack\main.py"
    os.system(f'python "{ruta_juego}"')

#barra superior
#boton del menu
btn_menu = tk.Button(
    barra_superior,
    text="\uf0c9",
    font=fontawesome,
    bg=COLOR_BARRA_SUPERIOR,
    fg="#f2f2f2",
    bd=0,
    command=toggle_panel
)
btn_menu.pack(padx=10, pady=10, side=tk.LEFT)

# Título
label = tk.Label(
    barra_superior,
    text="CASINO",
    font="Roboto 24",
    bg=COLOR_BARRA_SUPERIOR,
    fg="#f2f2f2"
)
label.pack(padx=10, pady=10, side=tk.LEFT)

# imagen del perfil
ruta_base = os.path.dirname(__file__)
ruta_perfil = os.path.join(ruta_base, "imagenes", "profile.png")
imagen_perfil = leer_imagen(ruta_perfil, (100, 100))
label_perfil = tk.Label(menu_lateral, bg=COLOR_MENU_LATERAL, image=imagen_perfil)
label_perfil.pack(side=tk.TOP, pady=20)

#menu lateral
#inicio y salir
btn_inicio = tk.Button(
    menu_lateral, text="\uf015 Inicio",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome, anchor="w",
    command=mostrar_inicio
)
btn_inicio.pack(side=tk.TOP, pady=5)

btn_salir = tk.Button(
    menu_lateral, text="\uf2f6 Salir",
    bg=COLOR_MENU_LATERAL, fg="#f2f2f2",
    bd=0, width=12, font=fontawesome, anchor="w",
    command=salir
)
btn_salir.pack(side=tk.BOTTOM, pady=10)


bind_hover_events(btn_inicio)
bind_hover_events(btn_salir)

# Mostrar pantalla inicial
mostrar_inicio()

#se ejecuta el comando
root.mainloop()

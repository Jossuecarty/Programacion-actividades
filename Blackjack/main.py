import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import os
from funciones_del_juego.cartas import crear_mazo, sumar_mano, sacar_carta, misma_carta
from funciones_del_juego.funciones_crupier import turno_crupier
from funciones_del_juego.funciones_jugador import jugar_mano, jugar_turno

#ESTE MAIN ES DONDE ESTA EL CODIGO DEL JUEGO FUNCIONAL, (sin la interfaz del casino, esa esta en el otro main)


#aqui no va a funcionar en diferentes dispostivos porque tiene una ruta de mi computadora,a no ser que modifique esa ruta la de su dispositivo, es una carpeta de cartas sacada de github
CARPETA_CARTAS = r"C:\Users\jossu\Desktop\BlackJack\Blackjack\funciones_del_juego\imageness\cartas"

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("1200x700")
        self.dinero = 100
        self.apuesta = 0
        self.manos = []
        self.apuestas = []
        self.mano_idx = 0
        self.mazo = []
        self.jugar_turno = lambda opcion: jugar_turno(self, opcion)
        self.crupier = []
        self.doblado = []
        self.puede_pedir = []

        # Cache de imágenes para que se puedan ver
        self.cartas_imagenes = {}
        self.cargar_imagenes()

        # Fondo
        self.root.configure(bg="#2E2E2E")

        # Informacion y botones
        self.info_label = tk.Label(root, text=f"Dinero: ${self.dinero}", font=("Arial", 16), bg="#2E2E2E", fg="white")
        self.info_label.pack(pady=10)
        self.apuesta_btn = tk.Button(root, text="Apostar", font=("Arial", 14), command=self.pedir_apuesta)
        self.apuesta_btn.pack(pady=5)

        # Mesa
        self.mesa_frame = tk.Frame(root, bg="#2E2E2E")
        self.mesa_frame.pack(pady=10, fill="both", expand=True)
        self.crupier_frame = tk.Frame(self.mesa_frame, bg="#2E2E2E")
        self.crupier_frame.pack(pady=5)
        self.jugador_frame = tk.Frame(self.mesa_frame, bg="#2E2E2E")
        self.jugador_frame.pack(pady=5)

        # Botones de acción
        self.botones_frame = tk.Frame(root, bg="#2E2E2E")
        self.botones_frame.pack(pady=10)
        self.botones = {}
        for opcion, texto in [("h","Hit"),("s","Stand"),("x","Double"),("r","Surrender"),("d","Split")]:
            btn = tk.Button(self.botones_frame, text=texto, font=("Arial",12),
                            command=lambda o=opcion: self.jugar_turno(o))
            btn.pack(side="left", padx=5)
            self.botones[opcion] = btn
        self.activar_botones(False)

    # Carga imágenes
    def cargar_imagenes(self):
        for archivo in os.listdir(CARPETA_CARTAS):
            if archivo.endswith(".png"):
                path = os.path.join(CARPETA_CARTAS, archivo)
                img = Image.open(path).resize((80,120))
                self.cartas_imagenes[archivo[:-4]] = ImageTk.PhotoImage(img)

    def activar_botones(self, activar):
        for btn in self.botones.values():
            btn["state"] = "normal" if activar else "disabled"

    def pedir_apuesta(self):
        if self.dinero <= 0:
            messagebox.showinfo("Fin del juego", "¡Te quedaste sin dinero! El juego terminará.")
            self.root.destroy()
            return

        ap = simpledialog.askinteger("Apuesta", f"Tienes ${self.dinero}. Ingresa tu apuesta (min 1):",
                                     minvalue=1, maxvalue=self.dinero)
        if ap is None:
            return
        self.apuesta = ap
        self.iniciar_mano()

    def iniciar_mano(self):
        self.dinero -= self.apuesta
        self.mazo = crear_mazo()
        self.crupier = [sacar_carta(self.mazo), sacar_carta(self.mazo)]
        jugador = [sacar_carta(self.mazo), sacar_carta(self.mazo)]
        self.manos = [jugador]
        self.apuestas = [self.apuesta]
        self.mano_idx = 0
        self.doblado = [False]
        self.puede_pedir = [True]
        self.mostrar_mesa()
        self.actualizar_botones()
        self.apuesta_btn["state"] = "disabled"

    def mostrar_mesa(self):
        for w in self.crupier_frame.winfo_children(): w.destroy()
        for w in self.jugador_frame.winfo_children(): w.destroy()

        # Crupier muestra solo una carta si es tu turno aun 
        if self.mano_idx < len(self.manos):
            tk.Label(self.crupier_frame, text=f"Crupier: {sumar_mano([self.crupier[0]])}", font=("Arial",12,"bold"), bg="#2E2E2E", fg="white").pack(side="left")
        else:
            tk.Label(self.crupier_frame, text=f"Crupier: {sumar_mano(self.crupier)}", font=("Arial",12,"bold"), bg="#2E2E2E", fg="white").pack(side="left")

        for i,carta in enumerate(self.crupier):
            if i==1 and self.mano_idx < len(self.manos):
                tk.Label(self.crupier_frame, text="🂠", font=("Arial",18), bg="#2E2E2E", fg="white").pack(side="left", padx=3)
            else:
                img = self.cartas_imagenes.get(carta)
                if img:
                    tk.Label(self.crupier_frame, image=img, bg="#2E2E2E").pack(side="left", padx=3)
                else:
                    tk.Label(self.crupier_frame, text=carta, font=("Arial",18), bg="#2E2E2E", fg="white").pack(side="left", padx=3)

        # Jugador
        for idx, mano in enumerate(self.manos):
            frame = tk.Frame(self.jugador_frame, bd=2, relief="solid", padx=5, pady=5, bg="#1E8449")
            frame.pack(pady=5)
            tk.Label(frame, text=f"Mano {idx+1} | Apuesta: ${self.apuestas[idx]} | Total: {sumar_mano(mano)}",
                     font=("Arial",12), bg="#1E8449", fg="white").pack()
            for carta in mano:
                img = self.cartas_imagenes.get(carta)
                if img:
                    tk.Label(frame,image=img,bg="#1E8449").pack(side="left", padx=3)
                else:
                    tk.Label(frame,text=carta,font=("Arial",18),bg="#1E8449",fg="white").pack(side="left", padx=3)
        self.info_label["text"] = f"Dinero: ${self.dinero}"

    def actualizar_botones(self):
        self.activar_botones(False)
        if self.mano_idx >= len(self.manos):
            return
        mano = self.manos[self.mano_idx]
        apuesta = self.apuestas[self.mano_idx]
        self.botones["h"]["state"]="normal"
        self.botones["s"]["state"]="normal"
        if len(mano)==2 and self.dinero>=apuesta: self.botones["x"]["state"]="normal"
        if len(mano)==2: self.botones["r"]["state"]="normal"
        if len(mano)==2 and misma_carta(mano[0],mano[1]) and self.dinero>=apuesta: self.botones["d"]["state"]="normal"

        jugar_mano()

    def turno_crupier(self):
        # Juega el crupier
        turno_crupier(self.mazo, self.crupier)
        total_crupier = sumar_mano(self.crupier)

        # Mostrar mesa final
        self.mostrar_mesa()

        # Determinar resultados
        mensaje = ""
        for idx, (m, ap) in enumerate(zip(self.manos, self.apuestas)):
            total_j = sumar_mano(m)
            if total_j > 21:
                mensaje += f"Mano {idx+1}: Te pasaste.\n"
            elif total_crupier > 21 or total_j > total_crupier:
                self.dinero += ap * 2
                mensaje += f"Mano {idx+1}: Ganaste ${ap}\n"
            elif total_j == total_crupier:
                self.dinero += ap
                mensaje += f"Mano {idx+1}: Empate.\n"
            else:
                mensaje += f"Mano {idx+1}: Perdiste ${ap}\n"

        messagebox.showinfo("Resultados", mensaje)
        self.info_label["text"] = f"Dinero: ${self.dinero}"

        if self.dinero <= 0:
            messagebox.showinfo("Fin del juego", "¡Te quedaste sin dinero! El juego terminará.")
            self.root.destroy()
            return

        # Reiniciar variables de la ronda
        self.manos = []
        self.apuestas = []
        self.mano_idx = 0
        self.crupier = []
        self.mazo = []
        self.doblado = []
        self.puede_pedir = []

        # Reactivar botón de apostar
        self.apuesta_btn["state"] = "normal"

        # Desactivar botones de acción
        self.activar_botones(False)

if __name__=="__main__":
    root=tk.Tk()
    app=BlackjackGUI(root)
    root.mainloop()

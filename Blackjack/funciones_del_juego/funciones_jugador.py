from funciones_del_juego.cartas import *
from funciones_del_juego.mesa import mostrar_mesa
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import os
#esto es antes de realizar el codigo para tkinteer, osea la primera presentacion del codigo


def jugar_mano(mazo, mano, crupier, apuesta, dinero, permitir_split=True, opcion=None):

    if opcion == "h":
        mano.append(sacar_carta(mazo))
        if sumar_mano(mano) > 21:
            return "pierde", apuesta, None
        return "sigue", apuesta, None

    elif opcion == "s":
        return "sigue", apuesta, None

    elif opcion == "x":
        # VALIDACIÓN DEFINITIVA
        if len(mano) != 2:
            return "invalido", apuesta, None
        if dinero < apuesta:
            return "invalido", apuesta, None

        apuesta *= 2
        mano.append(sacar_carta(mazo))
        if sumar_mano(mano) > 21:
            return "pierde", apuesta, None
        return "sigue", apuesta, None

    elif opcion == "r":
        if len(mano) != 2:
            return "invalido", apuesta, None
        return "rendirse", apuesta // 2, None

    elif opcion == "d":
        # VALIDACIÓN DEFINITIVA
        if not permitir_split:
            return "invalido", apuesta, None
        if len(mano) != 2:
            return "invalido", apuesta, None
        if not misma_carta(mano[0], mano[1]):
            return "invalido", apuesta, None
        if dinero < apuesta:  # NO TE ALCANZA PARA LA SEGUNDA APUESTA
            return "invalido", apuesta, None

        c1, c2 = mano
        mano1 = [c1, sacar_carta(mazo)]
        mano2 = [c2, sacar_carta(mazo)]
        return "split", apuesta, (mano1, mano2)

    return "invalido", apuesta, None



def jugar_turno(self, opcion):
    mano = self.manos[self.mano_idx]
    apuesta_actual = self.apuestas[self.mano_idx]

    # HIT jalar carta
    if opcion == "h":
        mano.append(sacar_carta(self.mazo))
        if sumar_mano(mano) > 21:
            messagebox.showinfo("Pierde", f"Te pasaste. Pierdes ${apuesta_actual}")
            self.puede_pedir[self.mano_idx] = False
            self.mano_idx += 1
        self.mostrar_mesa()
        self.actualizar_botones()
        if self.mano_idx >= len(self.manos):
            self.root.after(100, self.turno_crupier)
        return

    # STAND pasar turno
    if opcion == "s":
        self.puede_pedir[self.mano_idx] = False
        self.mano_idx += 1
        self.mostrar_mesa()
        self.actualizar_botones()
        if self.mano_idx >= len(self.manos):
            self.root.after(100, self.turno_crupier)
        return

    # DOUBLE
    if opcion == "x":
        if len(mano) != 2 or self.dinero < apuesta_actual:
            return
        self.dinero -= apuesta_actual
        self.apuestas[self.mano_idx] *= 2
        mano.append(sacar_carta(self.mazo))
        self.puede_pedir[self.mano_idx] = False
        self.mano_idx += 1
        self.mostrar_mesa()
        self.actualizar_botones()
        if self.mano_idx >= len(self.manos):
            self.root.after(100, self.turno_crupier)
        return

    # SURRENDER
    if opcion == "r":
        perdida = apuesta_actual // 2
        self.dinero -= perdida
        self.puede_pedir[self.mano_idx] = False
        self.mano_idx += 1
        self.mostrar_mesa()
        self.actualizar_botones()
        if self.mano_idx >= len(self.manos):
            self.root.after(100, self.turno_crupier)
        return

    # SPLIT
    if opcion == "d":
        if len(mano) != 2 or not misma_carta(mano[0], mano[1]) or self.dinero < apuesta_actual:
            return
        self.dinero -= apuesta_actual
        c1, c2 = mano
        mano1 = [c1, sacar_carta(self.mazo)]
        mano2 = [c2, sacar_carta(self.mazo)]
        self.manos[self.mano_idx] = mano1
        self.apuestas[self.mano_idx] = apuesta_actual
        self.manos.insert(self.mano_idx + 1, mano2)
        self.apuestas.insert(self.mano_idx + 1, apuesta_actual)
        self.doblado.insert(self.mano_idx, False)
        self.doblado.insert(self.mano_idx + 1, False)
        self.puede_pedir.insert(self.mano_idx, True)
        self.puede_pedir.insert(self.mano_idx + 1, True)
        self.mostrar_mesa()
        self.actualizar_botones()
        return

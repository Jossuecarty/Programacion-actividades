from funciones_del_juego.cartas import sacar_carta, sumar_mano

def turno_crupier(mazo, mano_crupier):
    while sumar_mano(mano_crupier) < 17:
        mano_crupier.append(sacar_carta(mazo))

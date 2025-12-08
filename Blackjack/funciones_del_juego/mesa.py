from funciones_del_juego.cartas import sumar_mano
#tambien fue el prototipo


def mostrar_mesa(crupier, manos_jugador, apuestas, mano_actual_idx=None, ocultar_crupier=True):
    print("\n--- MESA ---")
    if ocultar_crupier:
        print(f"Crupier: {crupier[0]}, [carta oculta]")
    else:
        print(f"Crupier: {', '.join(crupier)} (= {sumar_mano(crupier)})")

    for i, mano in enumerate(manos_jugador):
        total = sumar_mano(mano)
        activo = " <---" if mano_actual_idx == i else ""
        print(f"Mano {i+1}: {mano} (={total}) | Apuesta ${apuestas[i]}{activo}")

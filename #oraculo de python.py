#oraculo

from datetime import date

def la_prediccion(nombre, number,elemento):
                match number:
                    case 1:
                        return f'{nombre}, tu conexión con el elemento {digito} te traerá gran sabiduría. ¡Es un buen momento para aprender algo nuevo!"'
                    case 2:
                      return f"veo que el elemento {elemento}, guía tu camino, {nombre}. La fortuna sonríe a los valientes, ¡atrévete a tomar ese riesgo que tienes en mente!"
                    case 3:
                     return f"{nombre}, el elemento {elemento} ilumina tu creatividad. ¡No dudes en iniciar ese proyecto que tienes en mente!"
                    case 4:
                        return f"El elemento {elemento} protege tu energía, {nombre}. ¡Hoy es un día ideal para reflexionar y cuidar de ti mismo!"
def iniciar_oraculo():
    while True:
        nombre = (input("ingrese su nombre: "))
        ano=int(input("ingrese su ano de nacimiento: "))
        number=int(input("elija un numero del 1 al 4: "))
        
        anos_totales= date.today().year
        edad= anos_totales - ano

        print ("tu edad actual es:", edad)
        digito= ano % 10
        if digito in (0,1):
              elemento= "metal"
        elif digito in (2,3):
               elemento= "agua"
        elif digito in (4,5):
                elemento= "madera"
        elif digito in (6,7):
                elemento= "fuego"        
        elif digito in (8,9):
            elemento= "tierra"
            print(f"su signo es {elemento}")

           
            
        mensaje= la_prediccion(nombre, number ,elemento)
        print(mensaje)
            
        
        repetir= input("desea intentarlo otra vez? (s/n): ")
        if repetir.lower() !="s":
            break



iniciar_oraculo()
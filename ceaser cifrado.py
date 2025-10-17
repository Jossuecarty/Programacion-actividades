def cifrar_mensaje(mensaje,clave):
        resultado=""
        for caracter in mensaje:
                if caracter.isupper():
                        nuevo= chr((ord(caracter)-ord('A')+ clave)% 26 + ord ('A'))
                        resultado +=nuevo
                elif caracter.islower():
                        nuevo= chr((ord(caracter)-ord('a')+ clave)% 26 + ord ('a'))
                        resultado +=nuevo
                elif caracter.isdigit():
                        resultado+= caracter
                elif caracter ==" ":
                        resultado += "_"
                else:
                    if clave % 2==0:
                        resultado +="@"
                    else:
                         resultado+= "#"
                    return resultado
def main():
            while True:
                print("1. Cifrar mensaje")
                print("2. Descifrar mensaje")
                print("3. Salir del programa")
                opcion= input("selecciones una uopcion (1-3)")

                match opcion:
                    case "1":
                          mensaje= input ("ingrese el mensaje a cifrar")
                          clave=int(input("ingrese la clave(numeor entero)"))
                          cifrado= cifrar_mensaje(mensaje, clave)
                          print("mensaje cifrado:",cifrado)
                    case"2":
                          mensaje= input ("ingrese el mensaje a descifrar")
                          clave=int(input("ingrese la clave(numeor entero)"))
                          cifrado= cifrar_mensaje(mensaje, -clave)
                          print("mensaje cifrado:",cifrado) 
                    case "3":
                              print("presiono salir y salio")
                              break
                    case _:
                              print("no se puede ")







main()                          
                                             

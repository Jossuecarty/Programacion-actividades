
def agregar_alumno(curso):
    alumno=input("dime el nombre del alumno: ")
    if alumno in curso["alumnos"]:
        print("alumno ya registrado")
    else:
        curso["alumnos"].append(alumno)
        print("se ha agregado correctamente")

def buscar_alumno():
    buscar=input("nombre a buscar: ")
    encontrado=False
    for curso in cursos:
        if buscar in curso["alumnos"]:
            print(f"{buscar} esta en {curso['nombre']}")
            encontrado=True
            break
    if not encontrado:
                print("alumno no registrado")


def dar_de_baja_a_alumno(curso):
    idAlumno=input("el nombre del alumno que quieres que se de de baja: ")
    if idAlumno in curso["alumnos"]:
        curso["alumnos"].remove (idAlumno)
        print(f"se elimino el alumno {idAlumno} correctamente")
    else:
        print("no se encontro el alumno")


def mostrar_lista(curso):
    print(f"----{curso['nombre']}----")
    if curso["alumnos"]:
        for alumno in curso["alumnos"]:
            print(f"-{alumno}")
    else:
        print("no hay alumnos registrados")


cursos=[]
while True:
    while True:
    
        nombre_curso=input("cual es el nombre de su curso: ").strip()
        existe=False
        for c in cursos:
            if c ["nombre"].lower()==nombre_curso.lower():
                existe=True
                break
        if existe:
            print("error, ya existe un curso con este nombre")
            continue
        else:
            break
    curso={"nombre": nombre_curso, "alumnos":[]}
    cursos.append(curso)
    
    while True:
        try:
            op2=int(input("""
1.-agregar alumno
2.-dar baja alumno
3.-mostrar lista de alumnos
4.-buscar un alumno                                            
5.-salir                      
"""))
            if op2 <1 or op2>5:
                print("error: debes de poner un numero entre 1 y 5")
                continue
        except ValueError:
            print("error: debes escribir un numero valido")
            continue

        match op2:
                case 1:
                    agregar_alumno(curso)
                case 2:
                    dar_de_baja_a_alumno(curso)
                
                case 3:
                    mostrar_lista(curso)
                
                case 4:
                    buscar_alumno()
                
                case 5:
                    print("su curso quedo asi")
                    mostrar_lista(curso)
                    break
            
    while True:
        n=input("desea aniadir otro curso? (si/no): ").lower()
        if n in ["si","no"]:
            break
        else:
            print("error: debe de poner si o no como indicacion")

    if n == "no":
        print("\nresumen de todos los cursos creados:")
        for c in cursos:
            mostrar_lista(c)
            print(f'{c["nombre"]} tiene {len(c["alumnos"])} alumnos')
        print("----programa finalizado----")
        break
                

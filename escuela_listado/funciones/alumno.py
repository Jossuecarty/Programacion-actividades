from funciones.funciones_randy import generar_id


def agregar_alumno(curso):
    alumno=input("dime el nombre del alumno: ")
    for a in curso["alumnos"]:
        if a["nombre"].lower() == alumno.lower():
            print("Alumno ya registrado")
            return
    id_alumno=generar_id()
    print(f"el id del alumno es {id_alumno}")
    curso["alumnos"].append({"nombre": alumno, "id": id_alumno})
    print("Se ha agregado correctamente")


def buscar_alumno(cursos):
    buscar=input("nombre a buscar: ")
    for curso in cursos:
        for a in curso['alumnos']:
            if a['nombre'].lower()== buscar.lower():
                print(f"{buscar} esta en {curso['nombre']} 5con id {a['id']}")
                return
    print("alumno no registrado")

def dar_de_baja_a_alumno(curso):
    idAlumno = int(input("ID del alumno que quieres dar de baja: "))
    for a in curso["alumnos"]:
        if a["id"] == idAlumno:
            curso["alumnos"].remove(a)
            print(f"Se eliminó el alumno {a['nombre']} correctamente")
            return
    print("No se encontró el alumno.")

def mostrar_lista(curso):
    print(f"----{curso['nombre']}----")
    if curso["alumnos"]:
        for alumno in curso["alumnos"]:
            print(f"-{alumno['nombre']} con id {alumno['id']}")
    else:
        print("no hay alumnos registrados")

def instructor(curso):
    nombre=input("cual es su nombre? ")
    while True:    
        eda=input("cual es su edad? ")
        if eda.isdigit():
            eda = int(eda)
            break
        else:
            print("debe de agregar un numero valido")
    curso["instructor"] = {"nombre": nombre, "edad": eda}
    print(f"El instructor {nombre} ha sido agregado al curso {curso['nombre']}")



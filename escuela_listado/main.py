import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "funciones"))

from funciones.alumno import agregar_alumno, dar_de_baja_a_alumno, mostrar_lista, buscar_alumno, instructor
from funciones.funciones_randy import generar_id
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
    id_curso= generar_id()
    print(f"el id de su curso es {id_curso}")
    curso={"nombre": nombre_curso, "alumnos":[]}
    cursos.append(curso)
    
    instructor(curso)
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
                    buscar_alumno(cursos)
                
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
            print(f'{c["nombre"]} tiene {len(c["alumnos"])} alumnos, con id del curso {id_curso}')
            if "instructor" in c:
                inst=c["instructor"]
                print(f"instructor: {inst['nombre']} {inst['edad']} years")
        print("----programa finalizado----")
        break




    #capaz cambiar instructor,aula. alumno ,edad, nombre, semestre, carrera'
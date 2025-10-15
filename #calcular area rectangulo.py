#calcular area rectangulo
def calcular_area_rectangulo(base,altura):
    area=base*altura
    return area
base=float(input("ingrese la base del rectangulo: "))
altura=float(input("ingrese la altura del rectangulo: "))
area= calcular_area_rectangulo(base, altura)
print("el area del rectangulo es:", area)
info_tienda=("cuidado con el prieto")
inventario={
    "juego 1":{"nombre":"minecraft",
         "stock":100,
         "edad recomendada":"+7 years"},
    "juego 2":{       
        "nombre":"GTAVI",
         "stock":67,
        "edad recomendada":"+7 years"},
    "juego 3":{
        "nombre":"PVZ2",
          "stock":10000,
         "edad recomendada":"+5 years"
        }
    }
precios={    
    "minecraft": 25,
    "GTAVI": 200,
    "PVZ2": 50
}
for clave, datos in inventario.items():
    nombre=datos["nombre"]
    precio=precios[nombre]
    print(f"{nombre} cuesta {precio}")
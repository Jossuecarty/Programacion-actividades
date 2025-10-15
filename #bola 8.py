#bola 8
import random
respuestas= ["sí definitivamente", "respuesta confusa inténtalo de nuevo", "mi respuesta es no", "buenas perspectivas", "pregunta de nuevo más tarde", "sin duda", "las perspectivas no son buenas", "concéntrate y pregunta otra vez", "lo más probable", "muy dudoso", "como yo lo veo sí", "no cuentes con ello", "mejor no decirte ahora", "puedes confiar en ello", "mis fuentes dicen que no", "las señales apuntan a que sí", "es cierto", "no puedo predecirlo ahora", "sí", "las perspectivas son inciertas"]
def bola_8():
    while True:
        
        
        pregunta=(input("proporcioname tu pregunta: "))
        print(random.choice(respuestas))

bola_8()        
#Funcion para probar generadores

def vdGenerador(*Lista):
    for elemento in Lista:
        contador2 = len(elemento)
        i=0
        while i < contador2:
            print(elemento[i])
            i += 1
        yield elemento

generador = vdGenerador("Hola","Mundo","Generador","Ciclos")

print(next(generador))


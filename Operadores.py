####
#   Autor: Victor Delgado (VD)
#   Archivo: Operadores.py
#   Versión: v0.1
#   Descripción:
#       Se generan funciones para probar los diferentes operadores y funciones
####

#Funcion para probar operadores aritmeticos
def vdOperadoresAritmeticos(a,b):
    print("\nFunción de Operadores: (%s,%s)" %(a,b))

    #Operador Suma (+)
    print("Suma: %s+%s=%s (%s)" %(a,b,a+b,type(a+b)))

    #Operador Resta (-)
    print("Resta: %s-%s=%s (%s)" %(a,b,a-b,type(a-b)))

    #Operador Multiplicación
    print("Multiplicación: %s*%s=%s (%s)" %(a,b,a*b,type(a*b)))

    #Operador División
    print("División: %s+%s=%s (%s)" %(a,b,a/b,type(a/b)))

    #Operador Potencia
    print("Potencia: %s**%s=%s (%s)" %(a,b,a**b,type(a**b)))

    #Operador Módulo
    print("Módulo: %s" %a,"%","%s=%s (%s)" %(b,a%b,type(a%b)))

    #Operador División Entera
    print("División Entera: %s" %a,"//","%s=%s (%s)" %(b,a//b,type(a//b)))

    return 0

#Funcion para probar operadores aritmeticos
def vdOperadoresComparacion(a,b):
    print("\nFunción de Comparación: (%s,%s)" %(a,b))
    
    #Operador Igual que (==)
    if a==b:
        print("%s es igual que (==) %s" %(a,b))

    #Operador Diferente que (!=)
    if a!=b:
        print("%s es diferente que (!=) %s" %(a,b))

    #Operador Mayor que (>)
    if a>b:
        print("%s es mayor que (>) %s" %(a,b))

    #Operador Menor que (<)
    if a<b:
        print("%s es menor que (<) %s" %(a,b))

    #Operador Mayor o Igual que (>=)
    if a>=b:
        print("%s es mayor o igual que (>=) %s" %(a,b))

    #Operador Menor o Igual que (<=)
    if a<=b:
        print("%s es menor o igual que (<=) %s" %(a,b))

    return 0

def vdOperadoresLogicos(a,b):
    print("\nFunción de Operadores Lógicos: (%s,%s)" %(a,b))
    
    #Operador AND (and)
    if (a>0 and b>0):
        print("AND: %s y %s son POSITIVOS" %(a,b))
    else:
        print("AND: %s ó %s ó ambos son NEGATIVOS" %(a,b))

    #Operador OR (or)
    if (a<0 or b<0):
        print("OR: %s ó %s es NEGATIVO" %(a,b))
    else:
        print("OR: %s y %s son POSITIVOS" %(a,b))

    #Operador NOT (not)
    if not(a>b):
        print("NOT: %s no es mayor que %s" %(a,b))
    else:
        print("NOT: %s no es mayor que %s" %(b,a))
         
    return 0

#Funcion para probar operadores aritmeticos
def vdOperadoresAsignacion(a,b):
    print("\nFunción de Asignación: (a: %s,b: %s)" %(a,b))

    #Igual (=)    
    a=b
    print("Igual (a=b): a:%s, b:%s" %(a,b))

    #Incremento (+=)
    a+=b
    print("Incremnto (a+=b): a:%s, b:%s" %(a,b))

    #Decremento (-)
    a-=b
    print("Decremneto (a-=b): a:%s, b:%s" %(a,b))

    #Multiplicación
    a*=b
    print("Decremneto (a*=b): a:%s, b:%s" %(a,b))

    #División
    a/=b
    print("División (a/=b): a:%s, b:%s" %(a,b))

    #Potencia
    a**=b
    print("Potencia (a**=b): a:%s, b:%s" %(a,b))

    #Módulo
    a%=b
    print("Módulo (a%=b): ","a:%s, b:%s" %(a,b))

    #División Entera
    a//=b
    print("División Entera (a//=b): ","a:%s, b:%s" %(a,b))

    return 0



import Operadores

#Cuerpo principal (main)

print("\nHola Mundo desde Python")

a=float(input('Introduce el primer valor:'))
b=float(input('Introduce el segundo valor:'))

Operadores.vdOperadoresAritmeticos(a,b)
Operadores.vdOperadoresComparacion(a,b)
Operadores.vdOperadoresLogicos(a,b)
Operadores.vdOperadoresAsignacion(a,b)

print('Interest Calculator:')
amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
years = int(input('Duration (no. of years) ?'))
total = (amount * pow(1 + (roi/100), years))
interest = total - amount
print("\nInterest = $%0.2f in %i years" %(interest,years))
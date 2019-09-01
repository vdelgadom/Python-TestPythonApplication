
#Manejo de Listas
miLista = [1,2,3,4,5]
miLista.append(6)
print (miLista)

#Agregar nuevos elementos a la lista
#miLista.append(input('País:'))

miTupla = ('a','b','c','d','e','a')
#print("Tamaño de la Tupla inicial: %i", %miTupla.count())

print (miTupla.count("a"))
print (miTupla.index("a",1))

#Manejo de Diccionarios
miDiccionario = {miLista[0]:miTupla[0]}
print (miDiccionario)

miDiccionario = {miLista[0]:miTupla, miLista[1]:miTupla}
print (miDiccionario)
from os import system
system("cls")

lista = [1,2,3,4,5,6,7,8,9]
print(lista)
print(f"Elemento 3: {lista[2]}")#desde el 0
print(lista[0:3])#desde:hasta inclusivo:excluyente, es decir te muestra hasta uno antes del que le indicas

lista.append(100)#agregar un numero al final de la lista
print(lista)
lista.extend([22,33,55])#para agregar varios valores al final en vez de uno 
print(lista)
lista.insert(2,44)#se ingresa el dato en el indice que le pongo
print(lista)
lista.remove(2)
print(lista)
print("---------------------------------------------------------------------------------------------------")
contador = 0
acumulador = 0

for i in range(len(lista)):#el len te devuelve la cantidad de elementos que tiene la lista y con esos elemntos creamos un rango 
    print(f"{i} -> {lista[i]}")
    acumulador += lista[i]
    if (lista[i] == 5):
        contador+=1

print(f"El resultado es {acumulador}")
print(f"La cantidad de 5 es de {contador}")

""" for numero in lista:
    print(numero) """

print("-----------------------------------------------------------------------------------------------------------------------")


    

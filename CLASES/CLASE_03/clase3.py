from os import system
system("cls")
c = 3 + 5j
print(c)#(3+5j)
print(c.real) #(3)
print(c.imag)#(5)
print(type(c))#<class 'complex>
#buleanos
x = True
y = False
#str
nombre = 'Veronica'
apellido = 'Perez'
print(f"Su nombre es {nombre} y su apellido {apellido}")
print(type(nombre))#class str
#lista
lista = [1, "Hola", 3.14]
print(type(lista))#class list
print(lista[1])#Hola porque la posicion 1 es hola
lista[1] = "Chau"
print(lista[1]) #chau
#tupla
lista_tuple = tuple([1, 'Hi', 3])
print(type(lista_tuple))
print(lista_tuple[1])
#lista[1] = "Chau" #va a tirar error porque no se puede modificar una tupla 
#############################################################
#diccionario lista que se maneja con una clave (key) y un valor(value) si tengo una llave tiene sus respectivos values
diccionario = {'nombre': 'Juan', 'edad' : 21}
print(diccionario['nombre']) #juan la key es nombre y el value es juan
print(diccionario['edad'])#21
#set es una lista que no respeta orden y no acepta elemntos duplicados y tampoco se peuden cambiar
s = {2,4,5,6,1,0,1}
print(s) #{1,2,4,5,6}
print(type(s))#set
 
lista_convertida = [1,2,3,4,5,1]
s = set(lista_convertida)
print(s)


from os import system
from data_stark import lista_personajes
from functools import reduce
system("cls")



def sumar(a,b):
    suma = a + b
    return suma
def restar(a,b):
    resta = a - b
    return resta
def multiplicar (a,b):
    multiplicacion = a * b
    return multiplicacion
def dividir(a,b):
    division = a / b
    return division 


def calcular (a,b,operacion):
    return operacion(a,b)



print(calcular(2,2,sumar))
print(calcular(2,2,restar))
print(calcular(2,2,multiplicar))
print(calcular(2,2,dividir))
print("=============================================")
#Objetos de primera clase
#Asignar una variable
#pueden pasarse como parametros de una funcion
#pueden retornarse
def potenciar(a,b):
    return a ** b


def calcular (a,b,operacion):
    return operacion(a,b)

####### LAMBDA

resultado = calcular(2,2, lambda a,b: a**b)
print (resultado)
print("=============================================")

####### MAP

lista = [2,3,5,7,1,5,3,8,1,4,6,6]
""" def mi_map (lista:list,valor):
    lista_duplicada = []
    for i in lista:
        elemento = i - valor
        lista_duplicada.append(elemento)
    return lista_duplicada """

nueva_lista = list(map(lambda elemento: elemento - 2, lista))#primer elemento es lo que recibe, despues de los 2 puntos es lo que hace la funcion, despues de la coma es de donde saca los elementos

print(lista)
print(nueva_lista)
print("============================================")


lista_colores = set(map(lambda personaje: personaje['color_ojos'], lista_personajes))#CON EL MAP MODIFICO LOS ELEMENTOS DE LA LISTA
lista_azul = list(map(lambda personaje: personaje['color_ojos'] =='Blue', lista_personajes))
print(lista_azul)
print(lista_colores)
print("===================================================")

########################################################\

#FILTER

""" def mi_filter(lista):
    pares = []
    for i in lista:
        if (i % 2) == 0:
            pares.append(i)
    return pares

lista_pares = mi_filter(lista)
"""
lista_filtrada = list(filter(lambda numero: numero % 2 == 0, lista))#en FILTER se tiene que cumplir un criterio para agregarse a la lista
print(lista_filtrada)
print("===================================================")
personajes_masculinos = list(filter(lambda heroe: heroe['genero']=='M',lista_personajes))
for i in personajes_masculinos:
    #print(i['nombre'])
    pass
print("=====================================================")
#REDUCE
acumulador = 0
for numero in lista:
    acumulador += numero
print(acumulador)

numero_maximo = 0
total = reduce(lambda acumulador, numero: acumulador + numero,lista, 0)#toma dos valores, el anterior y el actual 
numero_maximo = reduce(lambda numero, maximo: numero if numero > maximo else maximo,lista,0) 
print(total)
print(numero_maximo)
from os import system
system("cls")
""" 
Ejercicio 03
Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)
MATIAS DI GIROLAMO 1 D 
"""
participantes_finalistas = ["Nacho", "Julieta", "Marcos"]
respuesta_seguir = 1
contador_votos = 0
contador_nacho = 0
contador_marcos = 0
contador_julieta = 0
porcentaje_nacho = 0
porcentaje_marcos = 0
porcentaje_julieta = 0
edad_votante_nacho = 0
contador_votantes_mediana_edad = 0
acumulador_edad_femenino = 0
contador_femenino = 0
bandera_mas_joven = 0
promedio_edad_femenino = 0

while respuesta_seguir == 1:
    nombre_votante = input("Ingresar nombre del votante ")
    
    edad_votante = int(input("Ingresar edad de votante, debe ser mayor a 13 anios: "))
    while edad_votante < 13 or edad_votante > 102:
        edad_votante = int(input("Ingresar edad de votante VALIDA mayor a 13 anios: "))
    genero_votante = input("Ingresar genero de votante, masculino, femenino, o otro: ").lower()
    
    while genero_votante != "masculino" and genero_votante != "femenino" and genero_votante != "otro":
        genero_votante = input("Ingresar genero de votante VALIDO, masculino, femenino, o otro: ").lower()
        
    voto_participante = input("A quien quiere votar? EL VOTO ES POSITIVO, ingrese nombre de participante, Nacho, Julieta o Marcos: ").lower()
    while voto_participante != "nacho" and voto_participante != "julieta" and voto_participante != "marcos":
        voto_participante = input("A quien quiere votar?, ingrese nombre de participante VALIDO, Nacho, Julieta o Marcos: ").lower()
        
    if genero_votante == "femenino":
        acumulador_edad_femenino += edad_votante
        contador_femenino += 1
        promedio_edad_femenino  = acumulador_edad_femenino / contador_femenino
        
    if genero_votante == "masculino" and (edad_votante > 24 and edad_votante < 45) and (voto_participante == "nacho" or voto_participante == "julieta"):
        contador_votantes_mediana_edad += 1
    match voto_participante:  
        case"nacho":    
            contador_nacho += 1
            if bandera_mas_joven == 0 or edad_votante < edad_votante_nacho:
                nombre_votante_joven_nacho = nombre_votante
                
        case "marcos":
            contador_marcos += 1
        case "julieta":
            contador_julieta +=1
                
    contador_votos+=1
    respuesta_seguir = int(input("Ingrese 1 si quiere seguir realizando votos, de lo contrario ingrese cualquier caracter: "))
    system("cls")
    
system("cls")    
porcentaje_nacho = (contador_nacho * 100) / contador_votos
porcentaje_marcos = (contador_marcos * 100) / contador_votos
porcentaje_julieta = (contador_julieta * 100) / contador_votos

if porcentaje_marcos > porcentaje_julieta and porcentaje_marcos > porcentaje_nacho:
    print(f"CON UN TOTAL DE {porcentaje_marcos} PORCIENTO DE VOTOS, EL GANADOR ES..... MARCOS!!!!")
elif porcentaje_julieta > porcentaje_marcos and porcentaje_julieta > porcentaje_nacho:
    print(f"CON UN TOTAL DE {porcentaje_julieta} PORCIENTO DE VOTOS, EL GANADOR ES..... JULIETA!!!!")
else:
    print(f"CON UN TOTAL DE {porcentaje_nacho} PORCIENTO DE VOTOS, EL GANADOR ES..... NACHO!!!!")
    
print("El total de porcentajes fue para Marcos", porcentaje_marcos, " para Julieta fue de ", porcentaje_julieta, " y para Nacho fue de ", porcentaje_nacho)
print(f"El promedio de edad de votantes femeninos es de {promedio_edad_femenino}")
print(f"El nombre del votante mas joven de Nacho es {nombre_votante_joven_nacho}")
print(f"La cantidad de hombres de entre 25 y 40 anios que votaron a Nacho y a Julieta es de {contador_votantes_mediana_edad}")

 

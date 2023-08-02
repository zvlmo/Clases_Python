
'''
NO ES NECESARIO UTILIZAR LAS PARENTECIS EN LAS CONDICIONALES 
NO ES NECESARIO DECLARAR LAS VARIABLES
LIMITAR EL TAMANIO DE LINEA DE CODIGO HASTA 79 CARACTERES
'''
#a medida que vas ejecutando borra y limpia pantalla 
from os import system
from sys import getsizeof
system("cls")
###################################################################################################################
print('Vamos a aprender python!') 

nombre_persona = "Jose"
edad = 12
contador = 0

if edad >= 18: #dos puntos dsp de esto
    print("Sos mayor")
    #no se puede hacer contador ++
    contador += 1
else:
    print("Sos menor")

    if nombre_persona == "Carlos":
        print("Bienvenido Carlos")
    else:
        if nombre_persona == "Maria":
            print("Usted no se llama Jose")

#usar and para dos condiciones, significa su literal
if nombre_persona == "Jose" and edad == 18:
    print("Hola Jose como estas?, feliz cumpleanios!!")

print(nombre_persona,edad, contador)
#########################################################################################################################################
#el pass es para cuando no definiste todavia que vas a hacer 
while edad != 12:
    pass
#########################################################################################################################################
#def para definir las funciones
def funcion():
    pass
#########################################################################################################################################
print(getsizeof(edad)) #para ver cuanto pesa, necesita esto al inicio from sys import getsizeof

print(id(edad)) #dice el espacio de memoria
#####################################################################
#cuando haces un cast convertis un tipo de dato en otro 

numero_flotante = 3.14
numero_pasado_entero = int(numero_flotante)#pasar a entero
numero_texto = str(numero_flotante)#pasar a cadena
otro_flotante = float(numero_texto)#pasar a flotante

numero = int(input("Ingrese un numero"))
"""todo lo que ingresemos al ingresar datos va a ser un string,
hay que castearlo agregando el tipo de dato antes 
booleano tiene que ser True o False siempre en mayuscula al principio 
#print(type(numero)) para saber que devuelve """

print ("Tu numero es:" , numero)
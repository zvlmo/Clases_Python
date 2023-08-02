from os import system
system("cls")

CANTIDAD_ALUMNOS = 3
""" lista_nombres=[]
lista_apellidos=[]

for i in range(CANTIDAD_ALUMNOS):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)

for i in range(CANTIDAD_ALUMNOS):
    print(f"{i + 1}: Nombre completo {lista_nombres[i]} {lista_apellidos[i]}")
 """
print("--------------------------------------------------------------------------------------------------")
""" lista_alumnos = [{"Nombre": "Juan", "Edad":25}{"Nombre": "Maria", "Edad":19}{"Nombre": "Carlos", "Edad":22}]  """
#LISTA HARDCODEADA
lista_alumnos = [{'Nombre': 'matias', 'Edad': 12, 'Apellido': 'digi'}, {'Nombre': 'carlos', 'Edad': 20, 'Apellido': 'martinez'}, {'Nombre': 'ezequiel', 'Edad': 8, 'Apellido': 'rodriguez'}]
#PARA INGRESAR VARIOS DATOS DE UNA PERSONA Y GUARDARLOS
""" for i in range(CANTIDAD_ALUMNOS):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = int(input("Ingrese edad: "))
    un_alumno = {}
    un_alumno["Nombre"] = nombre
    un_alumno["Edad"] = edad
    un_alumno ["Apellido"] = apellido
    lista_alumnos.append(un_alumno) """
#PARA BUSCAR ADENTRO DE LA LISTA DICCIONARIO ALGO     
""" for alumno in lista_alumnos:
    apellido = alumno ["Apellido"]
    nombre = alumno ["Nombre"]
    edad = alumno["Edad"]
    print(f"{apellido} {nombre} {edad}") """ 
    
for alumno in lista_alumnos:
    edad = alumno["Edad"]
    if edad > 18:
        print(f"{alumno['Apellido']} {alumno['Nombre']} {edad}")
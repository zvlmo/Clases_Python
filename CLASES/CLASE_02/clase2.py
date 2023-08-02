from os import system
system("cls")

# lista_numeros  = list (range(0,5,1)) #primer numero es desde donde empieza, segundo hasta donde, y el tercero de cuanto en cuanto suma

acumulador = 0
#nuestra forma de iterar en python
for i in range(5):
    numero = int(input(f"Ingrese el {i + 1}er un numero: "))
    acumulador += numero   
print(f"La suma es {acumulador} en total")

lista_nombres = ["Carlos", "Juan", "Ezequiel", "Juan","Ernesto", "Pedra"]
#lista_nombres.reverse() PARA DAR VUELTA LA LISTA
for nombre in lista_nombres:
   # print(nombre)
    if nombre == "Ezequiel":
        #print("Hola Ezequiel")
        continue#fuerza a que siga la iteracion
    print(f"Hola {nombre}") #o print("Hola", nombre)
        #break
    ejemplo = "Hola"
    

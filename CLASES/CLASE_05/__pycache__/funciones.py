from os import system
system("cls")

def sumar_numeros(primer_numero:int, segundo_numero:int) -> int:
    suma = primer_numero + segundo_numero
    
    return suma
    
def restar_numeros(primer_numero:int, segundo_numero:int) -> int:
    resta = primer_numero - segundo_numero
    
    return resta

def multiplicar_numeros(primer_numero:int, segundo_numero:int) -> int:
    
    multiplicacion = primer_numero * segundo_numero
    
    return multiplicacion
def dividir_numeros(primer_numero: int, segundo_numero: int) -> float:
    dividir_numeros = None
    if segundo_numero != 0:
        dividir_numeros = primer_numero / segundo_numero
    
    return dividir_numeros



bandera_ingreso = False
while True:
    menu = int(input("1.Ingresar numeros\n2.Sumar\n3.Restar\n4.Multiplicar\n5.Dividir\n6.Salir "))
    match menu:
        case 1:
            x = int(input("Ingresar primer numero: "))
            y = int(input("Ingresar segundo numero: "))
            bandera_ingreso = True
        case 2:
            if bandera_ingreso == True:
                resultado_suma = sumar_numeros(x,y)
                print(f"El resultado de la suma es {resultado_suma}")
            else:
                print("Primero tiene que ingresar los numeros")
        case 3:
            if bandera_ingreso == True:
                resultado_resta = restar_numeros(x,y)
                print(f"El resultado de la resta es {resultado_resta}")
            else:
                print("Primero tiene que ingresar los numeros")
        case 4:
            if bandera_ingreso == True:
                resultado_multiplicar = multiplicar_numeros(x,y)
                print(f"El resultado de la multiplicacion es {resultado_multiplicar}")
            else:
                print("Primero tiene que ingresar los numeros")
        case 5:
            if bandera_ingreso == True:
                resultado_division = dividir_numeros(x,y)
                if(resultado_division != None):
                    print(f"El resultado de la division {resultado_division}")
                else:
                    print("Error no se puede dividir por cero")
            else:
                print("Primero tiene que ingresar los numeros")
        case 6:
            break
    
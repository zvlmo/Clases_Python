""" La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.
Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.
Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
MATIAS DI GIROLAMO 1 D"""
from os import system
system("cls")

acumulador_precio_bruto = 0 
acumulador_kilo = 0
bandera_alimento_caro = 0
alimento_caro = 0
promedio_por_kilo = 0

for i in range(1,4):
    peso_ingrediente = int(input("Ingresar el peso del ingrediente, entre 10 y 100 kg "))
    while peso_ingrediente < 10 or peso_ingrediente > 100:
        peso_ingrediente = int(input("Ingresar el peso del ingrediente, entre 10 y 100 kg "))
    precio_por_kilo = int(input("Ingresar el precio por kilo, mayor a 0 "))
    while precio_por_kilo < 0:
        precio_por_kilo = int(input("Ingresar el precio por kilo, mayor a 0 "))
    tipo_variedad = input("Ingresar tipo de ingrediente, vegetal, animal, mezcla ").lower()
    while tipo_variedad != "vegetal" and tipo_variedad != "animal" and tipo_variedad != "mezcla":
        tipo_variedad = input("Ingresar tipo de ingrediente, vegetal, animal, mezcla ").lower()
    if bandera_alimento_caro == 0 or precio_por_kilo > alimento_caro:
        alimento_caro = precio_por_kilo
        tipo_alimento_caro = tipo_variedad
        bandera_alimento_caro = 1
    acumulador_kilo += peso_ingrediente
    acumulador_precio_bruto += precio_por_kilo
    system("cls")

system("cls")
print("-----------------------------------------------------------------------------------------------------")
#A
print(f"El precio bruto sin descuento es de $ {acumulador_precio_bruto}")
#B
if acumulador_kilo > 100:
    precio_descuento_menor = (acumulador_precio_bruto * 15)/ 100
    print("El descuento es de %15")
    print(f"El importe con descuento es de {acumulador_precio_bruto - precio_descuento_menor}")
elif acumulador_kilo > 300:
    precio_descuento_mayor = (acumulador_precio_bruto * 25) / 100
    print("El descuento es de %25")
    print(f"El importe con descuento es de {acumulador_precio_bruto - precio_descuento_mayor}")   
    
print(f"El tipo de alimento mas caro es {tipo_alimento_caro}")

promedio_precio_kilo = acumulador_precio_bruto / acumulador_kilo
print(f"El promedio de precio por kilo es: ${promedio_precio_kilo}")
print("-----------------------------------------------------------------------------------------------------")

    

    

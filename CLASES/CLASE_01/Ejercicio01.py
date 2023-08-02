from os import system
system("cls")
'''
Ejercicio 01
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo (&quot;barbijo&quot;, &quot;jabón&quot; o &quot;alcohol&quot;)
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.
MATIAS DI GIROLAMO 1 D
'''
precio_producto = 0
cantidad_producto = 0

tipo_producto = (input("Ingresar tipo: ")).lower()

while tipo_producto != "barbijo" and tipo_producto != "jabon"and tipo_producto != "alcohol":
    tipo_producto = (input("Ingresar tipo correcto: ")).lower()
    
precio_producto = float(input("Ingresar el precio del producto: "))
while precio_producto < 1:
    precio_producto = float(input("Ingresar el precio del producto correcto: "))

cantidad_producto = int(input("Ingresar la cantidad de productos: "))
while cantidad_producto < 1:
    cantidad_producto = int(input("Ingresar la cantidad de productos: "))


marca_producto = (input("Ingresar marca: "))
fabricante_producto = (input("Ingresar fabricante: "))


print("El tipo de producto es", tipo_producto)
print("La marca del producto es" , marca_producto)
print("El fabricante del producto es", fabricante_producto)
print("El precio del producto es de:", precio_producto)
print("La cantidad de producto es de:", cantidad_producto)
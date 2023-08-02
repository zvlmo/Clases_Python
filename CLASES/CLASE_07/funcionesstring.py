mi_cadena = "   hola mundo, como estas?   "

mi_cadena = mi_cadena.strip()#muestra sin espacios ni de un lado ni del otro
print(mi_cadena) 

metodo_upper = "hola mundo"

metodo_upper = metodo_upper.upper() #muestra todo en mayus, para minuscula es .lower()
print(metodo_upper)

capitalize ="hola mundo"
capitalize = capitalize.capitalize() #convierte en mayuscula la primer letra de todo
print(capitalize)

metodo_replace = "hola mundo"
metodo_replace = metodo_replace.replace("mundo", "miguel")
print(metodo_replace)

mi_cadena = "py, java, js, c"
lista_split = mi_cadena.split(",")#crea una lista separando por lo que le ingreso 
lista_split = lista_split
for lenguaje in lista_split:
    print(lenguaje.strip())
    
separador = "/"
dia = "10"
mes = "9"
anio = "2005"

fecha  = separador.join([dia,mes,anio])#join recorre lo que le ingreso en orden y donde estan las comas ingresa lo que le declaro 
print(fecha)

cadena = '123'
cadena = cadena.zfill(5)#rellena con 0 adelante 
print(cadena)

metodo_alfa = "holamundo"
print(metodo_alfa.isalpha()) #devuelve si todos los caracteres que le pasas es alfanumerico 

metodo_alnum = "123.34"
print(metodo_alnum.isalnum())#muestra si todos son numeros

largo = "hola mundo"
print(len(cadena))#la cuenta

count = "holalala"
print(count.count("la"))#cuenta las veces que esta lo que le paso

una_cadena = "hola mundo"
print(cadena[5:10])
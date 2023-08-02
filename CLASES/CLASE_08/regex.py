import re
from os import system
system("cls")
##SPLIT
print("SPLIT")
split = (re.split(" ","Hola mundo 1 B"))# crea una lista separada por el elemento que le indicamos

split2 = (re.split("[0-9 ]+","hola mundo 1231B"))# lo mismo pero busca los caracteres de la a a la z
print(split2)

split3= re.split("hola|chau|[ ]+","hola mundo chau ")
print(split3)
print("------------------------------------")
#SEARCH
print("SEARCH")
search = (re.search("mundo ","hola mundo hola? ")).span()#devuelve none si no lo encuentra o devuelve un objeto de tipo match si lo encuentra
print(re.search("mundo","hola mundo hola? ").start())#me dice donde inicia la tupla
print(re.search("mundo","hola mundo hola? ").end())#donde termina
print(search)
print(re.search("[0-9]+","hola mundo hola? 123 y letras locas qowma ").group())#para guardar el pedazo de cadena con el que hizo match
print("----------------------------------------")

#FINDALL
print("FINDALL")
texto = "la uno 1 Dos 2 tres 3 Cuatro 44"
print(re.findall("[0-9]",texto))
print(re.findall("[0-9]+",texto))
print(re.findall("[a-z]",texto))#separado por letras
print(re.findall("[a-zA-Z0-9]+",texto))#dos condiciones y con el mas haces que te traiga la palabra o el conjunto entero, ej cuatro o 44
print(re.findall("[a-zA-Z]{2,6}",texto))#le das un minimo de caracteres
print("----------------------------------------")

#SUB
print("SUB")
texto_sub = "abc abc ccc  ddd abc aaa"

result = re.sub("abc", "xyz", texto_sub)#busca un patron y lo reemplaza 
print(result)
result2 = result
result2 = (re.sub('\\s+', " ", texto_sub))#reemplaza espacios duplicados x uno solo  \\s es un espacio
print(result2)
print("----------------------------------------------------------------")

bzrp = "QUEVEDO || BZRP Music Sessions #52"

lista_titulo_bzrp = (re.split("[ \|# ]+",bzrp))#el contra barra es para que se tome como literal la barra recta, que significa OR

print(lista_titulo_bzrp)
""" lista_titulo_bzrp[1] = (re.split(" ", lista_titulo_bzrp[1]))
print(lista_titulo_bzrp) """
print("----------------------------------------------------------------")
fecha = "2022-02-02 19:31:11"
print(re.findall("-([0-9]{2})-",fecha))# con los parentesis excluyo los guines, con el {2} le digo que tienen que ser dos numeros 
fecha  = (re.split(" [0-9]{2}:[0-9]{2}:[0-9]{2}",fecha))
print(fecha) 

""" anio = "([0-9){2,4})"
mes = "([0-9]{1,2})"
dia = "([0-9]{1,2})"

print(re.findall(f"{anio}-{mes}-{dia}", fecha)) """
letra = 'a'
print(letra)

""" 
CUANTIFICADORES 
* O o mas
+ 1 o mas
? 0 o 1
LIMITES
\b
"""
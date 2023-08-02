from os import system
system("cls")

mi_diccionario = {}

mi_diccionario["Nombre"] = "Juan"
print(mi_diccionario["Nombre"])
mi_diccionario["Edad"] = 25
print(mi_diccionario["Edad"])
print(type(mi_diccionario))

otro_diccionario = {"Nombre":"Jose","Edad" : 22, "ID" : 1}
print(otro_diccionario)
print("---------------------------------------------------------------------------------------")
""" for key in otro_diccionario:
    print(key) """
for key in otro_diccionario:
    print(f"{key}: {otro_diccionario[key]}")
print("---------------------------------------------------------------------------------------")
for valores in otro_diccionario.values():
    print(valores)
print("---------------------------------------------------------------------------------------")


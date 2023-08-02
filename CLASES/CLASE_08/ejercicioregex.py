import re

def validar_patente(patente:str):
    patente_primero = re.findall("[A-Za-z]{3}[.*-|]*[0-9]{3}",patente)
    if patente_primero: # Verifica si la lista patente_primero no está vacía
        patente_limpia = re.sub("[^A-Za-z0-9]", " ", patente_primero[0]) # Reemplaza cualquier carácter que no sea una letra o un dígito con un espacio
        print(patente_limpia)
    else:
        print("La cadena de entrada no cumple con el patrón esperado.")

validar_patente("abc.1-23")
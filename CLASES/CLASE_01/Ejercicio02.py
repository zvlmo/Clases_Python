from os import system
system("cls")
""" Ejercicio 02
Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente” 
MATIAS DI GIROLAMO 1 D"""
respuesta = 1

while respuesta == 1:   
    opcion = int(input("Ingrese numero del 1 al 8 para ver una regla de estilo: "))
    while opcion < 1 or opcion > 8:
        print("Error, regla de estilo inexistente")
        opcion = int(input("Ingrese numero del 1 al 8 para ver una regla de estilo: "))
        
    match opcion:
        case 1:
            print ("Cual es el sentido?, Según Guido van Rossum, el código es leído másveces que escrito, \n por lo que resulta importante escribir código que no sólo funcione, sino que además pueda ser leído con facilidad.")
            
        case 2:
            print ("Que es PEP? Python Enhancement Proposal es un documento que proporciona información a la comunidad de Python,\n o que describe una nueva característica.")
            
        case 3:
            print ("Que es PEP8? Es un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible y\n abarca desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener."  )
            
        case 4:
            print ("Indentado, Python no usa {} para designar bloques de código como otros lenguajes de programación,\n sino que usa bloques identados para indicar que undeterminado bloque de código pertenece a porejemplo un if.")
            
        case 5:
            print ("Tamaño máximo linea: Se recomienda limitar el tamaño de cada línea a 79 caracteres, para evitar tener que hacer scroll a la derecha.")
            
        case 6:
            print ("Líneas en blanco, El uso de espacios en blanco mejora la legibilidad del código, y es por lo que la PEP8 indica dónde debemos usar espacios y dónde no.")
            
        case 7:
            print ("Comentarios: Cualquier comentario que contradiga el código es peor que ningún comentario. \n Si actualizamos el código, se debe actualizar los comentarios para evitar crear inconsistencias. \n Evitar comentarios poco descriptivos que no aporten nada más allá de lo que ya se ve a simple vista.")
            
        case 8:
            print ("Nombres: Funciones: Uso de snake_case, letras en minúscula separadas por guión bajo: mi_funcion.\n Variables: Al igual que las funciones: variable, mi_variable.\n Clases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba. \n Métodos: Al igual que las funciones, usar snake case: metodo, mi_metodo. \n Constantes: Nombrarlas usando mayúsculas y separadas por guión bajas: UNA_CONSTANTE \n Módulos: Igual que las funciones: modulo.py, mi_modulo.py." )
    respuesta = int(input("Quiere ver otra regla?, ingrese 1 para si o 2 para no."))

""" respuesta = 1

while respuesta == 1: 
    
    opcion = int(input("Ingrese numero del 1 al 8 para ver una regla de estilo: "))
    while opcion < 1 or opcion > 8:
        print("Error, regla de estilo inexistente")
        opcion = int(input("Ingrese numero del 1 al 8 para ver una regla de estilo: "))
        
    if opcion == 1:
        print("Cual es el sentido?, Según Guido van Rossum, el código es leído másveces que escrito, \n por lo que resulta importante escribir código que no sólo funcione, sino que además pueda ser leído con facilidad.")
        
    elif opcion == 2:
        print("Que es PEP? Python Enhancement Proposal es un documento que proporciona información a la comunidad de Python,\n o que describe una nueva característica.")
        
    elif opcion == 3:
        print("Que es PEP8? Es un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible y\n abarca desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener.")  
        
    elif opcion == 4:
        print("Indentado, Python no usa {} para designar bloques de código como otros lenguajes de programación,\n sino que usa bloques identados para indicar que undeterminado bloque de código pertenece a porejemplo un if.")
        
    elif opcion == 5:
        print("Tamaño máximo linea: Se recomienda limitar el tamaño de cada línea a 79 caracteres, para evitar tener que hacer scroll a la derecha.")
        
    elif opcion == 6:
        print("Líneas en blanco, El uso de espacios en blanco mejora la legibilidad del código, y es por lo que la PEP8 indica dónde debemos usar espacios y dónde no.")
        
    elif opcion == 7:
        print("Comentarios: Cualquier comentario que contradiga el código es peor que ningún comentario. \n Si actualizamos el código, se debe actualizar los comentarios para evitar crear inconsistencias. \n Evitar comentarios poco descriptivos que no aporten nada más allá de lo que ya se ve a simple vista.")
        
    elif opcion == 8:
        print("Nombres: Funciones: Uso de snake_case, letras en minúscula separadas por guión bajo: mi_funcion.\n Variables: Al igual que las funciones: variable, mi_variable.\n Clases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba. \n Métodos: Al igual que las funciones, usar snake case: metodo, mi_metodo. \n Constantes: Nombrarlas usando mayúsculas y separadas por guión bajas: UNA_CONSTANTE \n Módulos: Igual que las funciones: modulo.py, mi_modulo.py.")
        
    respuesta = int(input("Quiere ver otra regla?, ingrese 1 para si o 2 para no."))
    
  """
    
            
    

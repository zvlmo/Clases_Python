from os import system
from data import lista_bzrp

system("cls")

def mostrar_lista_views(lista:list):
    for titulos in lista_bzrp:
        print(f"{titulos['title']} - {titulos['views']}")
    buscar_tema_mas_largo(lista_bzrp)
def calcular_maximo(lista:list,clave:str):
    """ 
    brief:
            calcula el maximo valor numerico en base a una clave
    parameters:
            lista: list -> lista sobre la que voy a hacer la busqueda
    return: 
            devuelve el maximo de algo en la lista
    """

    bandera_maximo = True
    if(type(lista)) == list and len(lista) > 0 and type(clave) == str and len(clave) > 0:
        for tema in lista_bzrp:
            if bandera_maximo == True or tema[clave] > maximo:
                maximo = tema[clave]
                bandera_maximo = False  
        return maximo
""" def mostrar_lista_temas(lista:list):
    for titulos in lista_bzrp:
        print(f"{titulos['title']}")  """
def mostrar_lista_temas(lista:list,clave = None,valor = None):
    if clave is None:
        for tema in lista_bzrp:
            print(f"{tema['title']}")    
    else:
        for tema in lista:
            if tema[clave] == valor:
                print(f"{tema['title']}")
    
def mostrar_maximo_views(lista:list):
    maxima_views = calcular_maximo(lista_bzrp, 'views')
    print(f"La cantidad maxima de reproduccion es : {maxima_views}")
    mostrar_lista_temas(lista_bzrp,'views',maxima_views)
    
def mostrar_minimo_views(lista:list):
    bandera_minimo = True
    for tema in lista_bzrp:
        if bandera_minimo == True or tema['views'] < vistas_minimo:
            vistas_minimo = tema['views']
            bandera_minimo = False
            print(f"La cantidad minima de reproduccion es : {vistas_minimo}")
def mostrar_promedio_views(lista:list):
        acumulador_views = 0
        contador_views = 0
        for tema in lista_bzrp:
            acumulador_views += tema['views']
            contador_views += 1
        promedio_views = acumulador_views / contador_views
        print(f"Sumatoria de reproducciones: {acumulador_views}")
        print(f"El promedio de views por temas es de {promedio_views}")
def buscar_tema_mas_largo(lista:list):
    maximo_largo = calcular_maximo(lista_bzrp,'length')
    print(f"Duracion maximo:{maximo_largo}")
    mostrar_lista_temas(lista_bzrp,'length', maximo_largo)

seguir = True
while seguir:
    respuesta = int(input("1. Mostrar temas\n2.Mostrar temas con views\n3.Mostrar temas mas vistos\n4.Mostrar temas menos vistos\n5.Mostrar promedio de views\n6.Salir\nIngrese una opcion: \n"))
    match respuesta:
        case 1:
           mostrar_lista_temas(lista_bzrp)
        case 2:
            mostrar_lista_views(lista_bzrp)
        case 3:
            mostrar_maximo_views(lista_bzrp)
        case 4:
            mostrar_minimo_views(lista_bzrp)
        case 5:
            mostrar_promedio_views(lista_bzrp)
        case 6:
            seguir = False
   






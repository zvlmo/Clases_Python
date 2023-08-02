from data import lista_bzrp

def mostrar_lista_temas():
    for titulos in lista_bzrp:
        print(f"{titulos['title']}") 
def mostrar_lista_views():
    for titulos in lista_bzrp:
        print(f"{titulos['title']} - {titulos['views']}")
def mostrar_maximo_views():
        bandera_maximo = True
        for tema in lista_bzrp:
            if bandera_maximo == True or tema['views'] > vistas_maximo:
                vistas_maximo = tema['views']
                bandera_maximo = False    
        print(f"La cantidad maxima de reproduccion es : {vistas_maximo}")
        for tema in lista_bzrp:
            if tema['views'] == vistas_maximo:
                print(f"{tema['title']}")
def mostrar_minimo_views():
    bandera_minimo = True
    for tema in lista_bzrp:
        if bandera_minimo == True or tema['views'] < vistas_minimo:
            vistas_minimo = tema['views']
            bandera_minimo = False
            print(f"La cantidad minima de reproduccion es : {vistas_minimo}")
def mostrar_promedio_views():
        acumulador_views = 0
        contador_views = 0
        for tema in lista_bzrp:
            acumulador_views += tema['views']
            contador_views += 1
        promedio_views = acumulador_views / contador_views
        print(f"Sumatoria de reproducciones: {acumulador_views}")
        print(f"El promedio de views por temas es de {promedio_views}")
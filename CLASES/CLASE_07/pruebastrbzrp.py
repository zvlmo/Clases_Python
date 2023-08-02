from data import lista_bzrp
def prueba(titulo:str):
   # titulo = "QUEVEDO || BZRP Music Sessions #52"
    cadena = titulo.split("||")
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    titulo = cadena2[0]
    numero = cadena2[1]
    print(f"{artista} // {titulo} {numero}")
def prueba2(titulo:str):
    cadena = titulo.split("||")
    if (len(cadena)) > 1:
        artista = cadena[0].strip()
        cadena2 = cadena[1].split("#")
        if len(cadena2) > 1:
            titulo = cadena2[0]
            numero = cadena2[1]
            print(f"{artista} // {titulo} {numero}")
def prueba4(titulo:str):
    tipo = "BZRP Music Sessions"
    parte1 = titulo.split(tipo)
    if len(parte1) == 2:
        artista = parte1[0].replace("||", " ").strip()
        numero = parte1[1].replace("#", " ").strip()
        print(f"{artista} - {tipo} - {numero}")
def test(lista:list):
    for tema in lista:
        url(tema)
        fecha = formatear_fecha(tema['date'])
        print(fecha)

def url(tema:dict):
    url = tema["url"]
    codigo = url[28:]
    print(codigo)
#'date': '2019-11-06 00:00:00'
def formatear_fecha(fecha_cadena:str):
    fecha_split = fecha_cadena.split(" ")
    fecha = fecha_split[0].split("-")
    dia = fecha[2]
    mes = fecha[1]
    anio = fecha[0]
    separador = '/'
    fecha_formato = separador.join([dia,mes,anio])
    return fecha_formato
    
    
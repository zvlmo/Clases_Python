lista = [{'nombre': 'matias','edad': 32},{'nombre': 'carlos','edad': 27},
         {'nombre': 'ezequiel','edad': 12},{'nombre': 'marcos','edad':32}]

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if (lista[i]['edad'] > lista[j]['edad'] or 
            (lista[i]['edad'] == lista[j]['edad'] and
            lista[i]['nombre'] > lista[j]['nombre'])):
            controlador = lista[i]
            lista[i] = lista[j]
            lista[j] = controlador 
for x in lista:
    print (x)

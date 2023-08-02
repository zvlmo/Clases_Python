from Class_Personaje import Personaje
from Class_PersonajeExtraterrestre import PersonajeExtraterrestre

personaje_A = Personaje(1,'IronMan','Si','No')
personaje_B = Personaje(2,'SpiderMan', 'No','No')
#personaje_A.nombre = 'SuperIronMan'#LOS ATRIBUTOS DE LA CLASE SON PUBLICOS, ENTONCES SE PUEDEN CAMBIAR
personaje_A.set_nombre('  superironman   ')
print(personaje_A.get_nombre())
print(personaje_A.retornar_descripcion())
print(personaje_B.retornar_descripcion()) 
personaje_extra = PersonajeExtraterrestre(5,'Loki','No','Si','Asgardiano')

print(personaje_extra.retornar_descripcion())
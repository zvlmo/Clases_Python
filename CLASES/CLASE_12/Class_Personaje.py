class Personaje:
    def __init__(self,id,nombre,nano,vuela)-> None: #CONSTRUCTOR DE LA CLASE
        self._id = id#(+Publico)
        self._nombre = nombre#(-Privado)Con esto no dejo que nadie use mis datos, estos son privados, si se quieren ver hay que definir un getter y un setter para cada valor
        self._usa_nanotecnologia = nano#(#Protegido) Si tiene un guin bajo, se puede ver desde la clase que se define y desde las clases derivadas
        self._puede_volar = vuela
    def set_id(self, id):
        if id > 0:
            self.__id = id
    def set_nombre(self, nombre):
        self.__nombre = nombre.strip().capitalize()
    def get_nombre(self):
        return self.__nombre
#SIEMPRE HAY QUE PASAR EL SELF
    def retornar_descripcion(self):#accion
        cadena_personaje = f"{self._id} - {self._nombre} - {self._usa_nanotecnologia} - {self._puede_volar}"
        return cadena_personaje
#ENCAPSULAMIENTO, UN OBJETO TIENE QUE ENCAPSULAR SU COMPORTAMIENTO


#PRIMER PILAR. ABSTRACCION

#SEGUNDO PILAR HERENCIA
#POLIMORFISMO

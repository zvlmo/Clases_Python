from Class_Personaje import Personaje
class PersonajeExtraterrestre(Personaje):#PERSONAJE ES LA CLASE PADRE
    def __init__(self,id, nombre, nano, vuela, raza):
        super().__init__(id, nombre, nano, vuela)#llama al metodo de la clase padre
        self._raza = raza
    def retornar_descripcion(self):
        descripcion = "{0} - {1}".format(super().retornar_descripcion(),self._raza)
        return descripcion
        
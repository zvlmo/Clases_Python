class Transporte: 
    def __init__(self, cantidad, velocidad):
        self._cantidad_pasajeros = cantidad
        self._velocidad_maxima = velocidad
        self._km_totales = 0
        self._distancia_recorrida = 0
    def frenar(self):
        print("Esta frenando")
        
    def avanzar(self, velocidad):
        if velocidad <= self._velocidad_maxima:
            print("Esta avanzando")
            self._distancia_recorrida += velocidad
        else:
            print("Esta excediendo la velocidad")        
    def mostrar(self):
        print(f"***********{type(self)}**************")
        print(f"Cantidad: {self._cantidad_pasajeros} - Velocidad: {self._velocidad_maxima} - Destino {self._km_totales} - Restan {self.get_distancia()}")
        
    def set_km_totales(self,valor):
        self._km_totales = valor
    def get_distancia(self):
        return self._km_totales - self._distancia_recorrida
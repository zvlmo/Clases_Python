from Transporte import Transporte

class Auto(Transporte):
    def __init__ (self, ruedas, marca, cantidad, velocidad):
        super().__init__(cantidad, velocidad)
        self._ruedas = ruedas
        self._marca = marca

    def frenar(self):
        print("El auto")
        super().frenar()

    def avanzar(self, velocidad):
        print("El auto")
        super().avanzar(velocidad)

    def mostrar(self):
        super().mostrar()
        print(f"Ruedas: {self._ruedas} - Puertas: {self._marca}")
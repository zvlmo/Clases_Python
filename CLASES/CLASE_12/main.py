from Caballo import Caballo
from Auto import Auto


caballo_1 = Caballo("Andaluz", "Marron",2,20)
caballo_1.set_km_totales(100)
auto_1 = Auto(4, "Fiat", 5 , 130)
auto_1.set_km_totales(500)
otro_auto = Auto(4,"Chevrolet",6,200)
otro_auto.set_km_totales(1000)
otro_caballo= Caballo("Potro Salvaje", "Negro",4,50)
otro_caballo.set_km_totales(300)

caballo_1.avanzar(120)
otro_caballo.avanzar(50)
auto_1.avanzar(120)
otro_auto.avanzar(25)
lista_transportes = [caballo_1,auto_1,otro_auto,otro_caballo]

for t in lista_transportes:
    t.mostrar()

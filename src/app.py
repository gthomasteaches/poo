from modelo.naranja import Naranja
from modelo.canasta import Canasta

mi_naranja = Naranja()
print("el peso de la naranja es: ", mi_naranja.peso)

mi_canasta = Canasta()

print("Canasta antes",mi_canasta.calcular_cantidad_naranjas())
mi_naranja.recoger(mi_canasta)
print("Canasta despues",mi_canasta.calcular_cantidad_naranjas())

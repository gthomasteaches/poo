class Canasta:

    def __init__(self):
        self.ubicacion = ""
        self.naranjas = []

    def calcular_cantidad_naranjas(self):
        return len(self.naranjas)
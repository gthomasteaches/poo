from modelo.canasta import Canasta

class Naranja:

    def __init__(self, peso):
        self.__peso =  peso 
        self.granja= "12-208" 
        self.fecha_cosecha="" 
        self.canasta= None


    def obtener_peso(self):
        return self.__peso

    def recoger(self, canasta:Canasta ):
        self.canasta = canasta
        canasta.naranjas.append(self)
        print("Naranja agregada")


    def exprimir(self ):
        return self.__peso*0.9






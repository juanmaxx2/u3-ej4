from calefactor import Calefactor
class CalefactorElectrico(Calefactor):
    __Potencia=None

    def __init__(self,Marca,Modelo,Potencia):
        super().__init__(Marca,Modelo)
        self.__Potencia=int(Potencia)

    def __str__(self):
        return self.__Marca+self.__Modelo+self.__Potencia
    
    def getCaloriaoPotencia(self):
        return self.__Potencia
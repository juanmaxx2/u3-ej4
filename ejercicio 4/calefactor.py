class Calefactor:
    __Marca=None
    __Modelo=None

    def __init__(self,Marca,Modelo):
        self.__Marca=Marca
        self.__Modelo=Modelo
    
    def __str__(self):
        return self.__Marca+self.__Modelo

    def getMarca(self):
        return self.__Marca

    def getModelo(self):
        return self.__Modelo

    def MenorCosto(self):
        pass
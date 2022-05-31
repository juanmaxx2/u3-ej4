class CalefactorElectrico:
    __Potencia=None

    def __init__(self,Marca,Modelo,Potencia):
        super().__init__(Marca,Modelo)
        self.__Potencia=Potencia
    
    def getPotencia(self):
        return self.__Potencia
        
from calefactor import Calefactor
class CalefactorGasNatural(Calefactor):
    __Matricula=None
    __Caloria=None

    def __init__(self,Marca,Modelo,Matricula,Caloria):
        super().__init__(Marca,Modelo)
        self.__Matricula=Matricula
        self.__Caloria=int(Caloria)
    
    def __str__(self):
        return self.__Marca+self.__Modelo+self.__Matricula+self.__Caloria

    def getMatricula(self):
        return self.__Matricula
    
    def getCaloriaoPotencia(self):
        return self.__Caloria
class CalefactorGasNatural:
    __Matricula=None
    __Caloria=None

    def __init__(self,Marca,Modelo,Matricula,Caloria):
        super().__init__(Marca,Modelo)
        self.__Matricula=Matricula
        self.__Caloria=Caloria

    def getMatricula(self):
        return self.__Matricula
    
    def getCaloria(self):
        return self.__Caloria
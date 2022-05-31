from calefactor import Calefactor
from calefactorElectrico import CalefactorElectrico
from calefactorGasNatural import CalefactorGasNatural
import csv
import numpy
class Manejador:
    __Cantidad=None
    __Dimension=None
    __Incremento=None

    def __init__(self,dimension=5):
        self.__Calefator=numpy.empty(dimension,datatype=Calefactor)
        self.__Dimension=dimension
        self.__Cantidad=0

    def AgregarCalefator(self,unCalefactor):
        if self.__Cantidad==self.__Dimension:
            self.__Dimension+=self.__Incremento
            self.__Calefator.resize(self.__Dimension)
        self.__Calefator[self.__Cantidad]=unCalefactor
        self.__Cantidad+=1

    def Iniciar(self):
        archivo=open('calefactor-electrico.csv',encoding="utf-8")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            unCalefactor=CalefactorElectrico(fila[0],fila[1],fila[3])
            self.AgregarCalefator(unCalefactor)
        archivo.close()
        archivo=open('calefactor-a-gas.csv',encoding="utf-8")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            unCalefactor=CalefactorGasNatural(fila[0],fila[1],fila[3],fila[4])
            self.AgregarCalefator(unCalefactor)
        archivo.close()

    def MenorCosto(self,costo,estimado,x):
        calefactor=None
        menor=10000000
        if x==1:
            tipo=CalefactorGasNatural
        elif x==2:
            tipo=CalefactorElectrico
        for  i in range(len(self.__Calefator)):
            if self.__Calefator[i]==tipo:
                tipo.MenorCosto()
                cos=self.__Calefactor[i].menorcosto(costo,estimado)
                if cos<menor:
                    menor=cos
                    calefactor=self.__Calefactor[i]
        print ('la marca del calefactor es:{} y el modelo es:{}'.format(self.__Calefator[i].getMarca(),self.__Calefator[i].getModelo()))

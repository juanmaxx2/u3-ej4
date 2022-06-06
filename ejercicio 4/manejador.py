from calefactor import Calefactor
from calefactorElectrico import CalefactorElectrico
from calefactorGasNatural import CalefactorGasNatural
import csv
import numpy as np
class Manejador:
    __Cantidad=0
    __Dimension=0
    __Incremento=5

    def __init__(self,dimension=5):
        self.__Calefactor=np.empty(dimension,dtype=Calefactor)
        self.__Dimension=dimension
        self.__Cantidad=0

    def AgregarCalefator(self,unCalefactor):
        if self.__Cantidad==self.__Dimension:
            self.__Dimension+=self.__Incremento
            self.__Calefactor.resize(self.__Dimension,refcheck=False)
        self.__Calefactor[self.__Cantidad]=unCalefactor
        self.__Cantidad+=1

    def Iniciar(self):
        archivo=open('calefactor-electrico.csv',encoding="utf-8")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            unCalefactor=CalefactorElectrico(fila[0],fila[1],fila[2])
            self.AgregarCalefator(unCalefactor)
        archivo.close()
        archivo=open('calefactor-a-gas.csv',encoding="utf-8")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            unCalefactor=CalefactorGasNatural(fila[0],fila[1],fila[2],fila[3])
            self.AgregarCalefator(unCalefactor)
        archivo.close()

    def MenorCosto(self,costo,estimado,x):
        menor=10000000
        if x==1:
            tipo=CalefactorGasNatural
        elif x==2:
            tipo=CalefactorElectrico
        for i in range(len(self.__Calefactor)):
            if isinstance(self.__Calefactor[i],tipo):
                cos=(self.__Calefactor[i].getCaloriaoPotencia()/1000)*costo*estimado
                if cos<menor:
                    menor=cos
                    indice=i
        if menor!=10000000:
            print ('la marca del calefactor es:{} y el modelo es:{}'.format(self.__Calefactor[indice].getMarca(),self.__Calefactor[indice].getModelo()))
            return self.__Calefactor[indice]

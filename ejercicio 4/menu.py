from manejador import Manejador
class Menu:
    __opcion=None

    def __init__(self):
        self.__opcion=None
    
    def Iniciar(self,cant):
        unManejador=Manejador(cant)
        unManejador.Iniciar()
        while self.__opcion!='4':
            print('\n1.Menor consumo de calefactor a gas natural')
            print('2.Menor consumo de calefactor electrico')
            print('3.Mostrar los 2 calefactores de menor consumo')
            print('4.Salir')
            self.__opcion=input('Elija la opcion del que desee realizar:')

            if self.__opcion=='1':
                costo=int(input('\nIngrese el costo por m3:'))
                estimado=int(input('ingrese la cantidad que se estima consumir por M3:'))
                i=1
                gasnat=unManejador.MenorCosto(costo,estimado,i)
            elif self.__opcion=='2':
                costo=int(input('\nIngrese el costo de el kilowatt/h:'))
                estimado=int(input('Ingrese la cantidad que se estima consumir por hora:'))
                i=2
                ele=unManejador.MenorCosto(costo,estimado,i)
            elif self.__opcion==3:
                print(ele)
                print(gasnat)
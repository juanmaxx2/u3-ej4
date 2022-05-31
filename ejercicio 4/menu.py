from manejador import Manejador
class Menu:
    __opcion=None

    def __init__(self):
        self.__opcion=None
    
    def Iniciar(self,cant):
        unManejador=Manejador(cant)
        unManejador.Iniciar()
        while self.__opcion!='3':
            print('\n1.')
            print('2.')
            print('3.')
            print('4.')
            self.__opcion=input('Elija la opcion del que desee realizar:')

            if self.__opcion=='1':
                costo=input('\nIngrese el costo por m3')
                estimado=input('ingrese la cantidad que se estima consumir por M3')
                i=1
                unManejador.MenorCosto(costo,estimado,i)
            elif self.__opcion=='2':
                costo=input('\nIngrese el costo de el kilowatt/h')
                estimado=('Ingrese la cantidad que se estima consumir por hora')
                i=2
                unManejador.MenorCosto(costo,estimado,i)
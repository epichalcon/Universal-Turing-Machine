from os import truncate

class Invalid_End(Exception):
    def __init__(self, expression, message) -> None:
        self.expression = expression
        self.message = message

class MTU():
    __cinta:'list[str]'
    __posicion:int

    '''
    La cinta usara '-' para el separador del registro inicial
    y '/' para el separador del registro general
    '''
    def __init__(self, cinta:str) -> None:
        if cinta[-1] != '#':
            raise Invalid_End(cinta, 'la cinta debe acabar en #')
        self.__cinta = list(cinta)
        self.__posicion = cinta.index('/')

    def execute(self):
        self.__estado0()
        return self.__cinta

    def output(self):
        asterisc = self.__cinta.index('*')
        separador = self.__cinta.index('-')
        cinta = self.__cinta[:separador]
        cinta[asterisc] = self.__cinta[separador + 3]
        return str(cinta)

    def __transicion(self,car,direccion):
        self.__cinta[self.__posicion] = car
        if direccion == 'd':
            self.__posicion += 1
        if direccion == 'i':
            self.__posicion -= 1

    def __get_char(self):
        return self.__cinta[self.__posicion].__str__()

# Modulo localizador
    def __estado0(self):
        valido = ['0','1','a','b','/']

        while self.__get_char() in valido:
            self.__transicion(self.__get_char(),'i')
        
        if self.__get_char() == '-':
            self.__transicion(self.__get_char(),'d')
            self.__estado1()
        
    def __estado1(self):
        valido = ['a','b']
        while self.__get_char() in valido:
            self.__transicion(self.__get_char(),'d')

        if self.__get_char() == '0':
            self.__transicion('a','d')
            self.__estado2()

        elif self.__get_char() == '1':
            self.__transicion('b','d')
            self.__estado3()

        elif self.__get_char() == '/':
            self.__transicion('/','d')
            self.__estado9()

    def __estado2(self):
        valido = ['0','1']
        while self.__get_char() in valido:
            self.__transicion(self.__get_char(),'d')

        if self.__get_char() == '/':
            self.__transicion('/','d')
            self.__estado4()

    def __estado3(self):
        valido = ['0','1']
        while self.__get_char() in valido:
            self.__transicion(self.__get_char(),'d')

        if self.__get_char() == '/':
            self.__transicion('/','d')
            self.__estado5()

    def __estado4(self):
        valido = ['a','b','/']
        while self.__get_char() in valido:
            self.__transicion(self.__get_char(),'d')
        
        if self.__get_char() == '0':
            self.__transicion('a','i')
            self.__estado0()

        elif self.__get_char() == '1':
            self.__transicion('b','d')
            self.__estado6()

    def __estado5(self):
        valido = ['a','b','/']
        while self.__get_char() in valido:
            self.__transicion(self.__get_char(),'d')
        
        if self.__get_char() == '1':
            self.__transicion('b','i')
            self.__estado0()

        elif self.__get_char() == '0':
            self.__transicion('a','d')
            self.__estado6()

        elif self.__posicion == len(self.__cinta):
            print('terminado')

    def __estado6(self):
        valido = ['0','1']
        while self.__get_char() in valido:
            if self.__get_char() == '0':
                self.__transicion('a','d')
            elif self.__get_char() == '1':
                self.__transicion('b','d')

        if self.__get_char() == '/':
            self.__transicion('/','i')
            self.__estado7()

    def __estado7(self):
        valido = ['0','1','a','b','/']

        while self.__get_char() in valido:
            self.__transicion(self.__get_char(),'i')
        
        if self.__get_char() == '-':
            self.__transicion(self.__get_char(),'d')
            self.__estado8()

    def __estado8(self):
        valido = ['0','1','a','b']

        while self.__get_char() in valido:
            if self.__get_char() == 'a':
                self.__transicion('0','d')
            elif self.__get_char() == 'b':
                self.__transicion('1','d')
            else:
                self.__transicion(self.__get_char(), 'd')
        
        if self.__get_char() == '/':
            self.__transicion(self.__get_char(),'i')
            self.__estado0()

# Modulo transcriptor
    def __estado9(self):
        validos = ['a','b','/']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'd')
        
        if self.__get_char() == '0':
            self.__transicion('a', 'i')
            self.__estado10()

        elif self.__get_char() == '1':
            self.__transicion('b', 'i')
            self.__estado11()

    def __estado10(self):
        validos = ['a','b','/']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'i')
        
        validos = ['0','1','-']
        if self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'd')
            self.__estado12()

    def __estado11(self):
        validos = ['a','b','/']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'i')
        
        validos = ['0','1','-']
        if self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'd')
            self.__estado13()

    def __estado12(self):
        if self.__get_char() == '/':
            self.__transicion('/', 'i')
            self.__estado14()
        
        elif self.__get_char() == 'a' or self.__get_char() == 'b':
            self.__transicion('0', 'd')
            self.__estado9()
        
    def __estado13(self):
        if self.__get_char() == '/':
            self.__transicion('/', 'i')
            self.__estado15()
        
        elif self.__get_char() == 'a' or self.__get_char() == 'b':
            self.__transicion('1', 'd')
            self.__estado9()

# Modulo simulador
    def __estado14(self):
        if self.__get_char() == '0':
            self.__transicion('0','i')
            self.__estado16()

        elif self.__get_char() == '1':
            self.__transicion('1','i')
            self.__estado17()

    def __estado15(self):
        if self.__get_char() == '0':
            self.__transicion('0','i')
            self.__estado18()

        elif self.__get_char() == '1':
            self.__transicion('1','i')
            self.__estado19()

    def __estado16(self):
        validos = ['0','1','-']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'i')

        if self.__get_char() == '*':
            self.__transicion('0','d')
            self.__estado20()

    def __estado17(self):
        validos = ['0','1','-']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'i')

        if self.__get_char() == '*':
            self.__transicion('1','d')
            self.__estado20()

    def __estado18(self):
        validos = ['0','1','-']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'i')

        if self.__get_char() == '*':
            self.__transicion('0','i')
            self.__estado20()

    def __estado19(self):
        validos = ['0','1','-']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'i')

        if self.__get_char() == '*':
            self.__transicion('1','i')
            self.__estado20()

    def __estado20(self):
        if self.__get_char() == '0':
            self.__transicion('*', 'd')
            self.__estado21()

        elif self.__get_char() == '1':
            self.__transicion('*', 'd')
            self.__estado22()
        
    def __estado21(self):
        validos = ['0','1','-']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'd')

        if self.__get_char() == '/':
            self.__transicion('/','i')
            self.__estado23()

    def __estado22(self):
        validos = ['0','1','-']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'd')

        if self.__get_char() == '/':
            self.__transicion('/','i')
            self.__estado24()

    def __estado23(self):
        if self.__get_char() == '0' or self.__get_char() == '1':
            self.__transicion('0', 'd')
            self.__estado25()

    def __estado24(self):
        if self.__get_char() == '0' or self.__get_char() == '1':
            self.__transicion('1', 'd')
            self.__estado25()

    def __estado25(self):
        validos = ['a','b','/']
        while self.__get_char() in validos:
            self.__transicion(self.__get_char(), 'd')

        validos = ['0','1','#']
        if self.__get_char() in validos or self.__posicion == len(self.__cinta):
            self.__transicion(self.__get_char(),'i')
            self.__estado26()

    def __estado26(self):
        validos = ['a','b','/']
        while self.__get_char() in validos:
            if self.__get_char() == 'a':
                self.__transicion('0', 'i')
            elif self.__get_char() == 'b':
                self.__transicion('1', 'i')
            else:
                self.__transicion('/', 'i')
        
        if self.__get_char() == '0':
            self.__transicion('0','d')
            self.__estado0()

        elif self.__get_char() == '1':
            self.__transicion('1','d')
            self.__estado0()
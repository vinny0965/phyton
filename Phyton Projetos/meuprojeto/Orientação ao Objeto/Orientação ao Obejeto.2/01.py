class Teste:
    a=None
    __b=None

    def __init___(self,a,__b):
        self.a=a
        self.__b=__b

    def setB(valorB):
        __b=valorB

teste=Teste()
teste.setB(10)

print(teste.getB())
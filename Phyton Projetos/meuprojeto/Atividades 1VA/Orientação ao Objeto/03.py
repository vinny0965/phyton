class funcionario:
    nome = None
    salario = None
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def ImprimirFuncionario(self):
        print(self.nome,self.salario)
func1 = funcionario('Jamison',79000.0)
func2 = funcionario('Vinicius',7000.0)

func1.ImprimirFuncionario()
func2.ImprimirFuncionario()
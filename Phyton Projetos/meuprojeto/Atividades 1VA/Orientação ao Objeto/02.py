"""Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e
salário. Escreva um pequeno programa que teste sua classe
"""""
class Funcionario:
    nome = None
    salario = None
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario
    def ImprimirFuncionario(self):
        print(self.nome, self.salario)
func1 = Funcionario('Jamisson',994.0)
func2 = Funcionario('Davi',954.0)

func1.ImprimirFuncionario()
func2.ImprimirFuncionario()
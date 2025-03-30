#Questão 4 - Herança e Polimorfismo (Difícil)
#Crie uma classe Funcionario com um método calcular_salario() que retorna um salário base. 
# Depois, crie duas classes Gerente e Desenvolvedor que herdam de Funcionario e sobrescrevem 
# o método calcular_salario(), considerando que:
#O Gerente recebe o dobro do salário base.
#O Desenvolvedor recebe 50% a mais do salário base.
#Crie instâncias de ambas as classes e exiba os salários calculados.

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, salario_base: float) -> None:
        self.salario_base = salario_base
    
    @abstractmethod
    def calcular_salario(self) -> None:
        pass

class Gerente(Funcionario):
    def __init__(self, salario_base: float)-> None:
        super().__init__(salario_base)

    def calcular_salario(self)-> float:
        return self.salario_base*2

class Desenvolvedor(Funcionario):
    def __init__(self, salario_base: float)-> None:
        super().__init__(salario_base)

    def calcular_salario(self)-> float:
        return self.salario_base*1.5

desenvolvedor = Desenvolvedor(1000)
print(desenvolvedor.calcular_salario())

gerente = Gerente(1000)
print(gerente.calcular_salario())
    
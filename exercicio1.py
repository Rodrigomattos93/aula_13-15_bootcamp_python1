#Questão 1 - Criando uma Classe (Fácil)
#Crie uma classe chamada Carro com os atributos marca e modelo. 
# Adicione um método descricao que retorna uma string formatada com essas informações. 
# Crie um objeto dessa classe e exiba a descrição.

class Carro():
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo
    def descricao(self) -> str:
        return f"Foi criado um objeto da classe Carro com os atributos marca {self.marca} e modelo {self.modelo}"

carro = Carro(marca = "Fiat", modelo = "Fastback")
print(carro.descricao())

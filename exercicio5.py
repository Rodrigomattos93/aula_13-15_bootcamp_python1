#Questão 5 - Desafio Final: Recursividade com Classes (Muito Difícil)
#Crie uma classe Fibonacci com um método recursivo calcular(n) que retorna o n-ésimo 
#termo da sequência de Fibonacci.
#Exemplo:
#fib = Fibonacci()
#print(fib.calcular(6))  # Saída: 8 (0, 1, 1, 2, 3, 5, 8)

class Fibonacci():
    def __init__(self, lista = [0, 1]):
        self.lista = lista
        
    def calcular(self, n: int) -> str:
        self.lista.append(self.lista[-1] + self.lista[-2])
        ult_digito = self.lista[-1]

        if n == len(self.lista):
            return str(ult_digito) + " (" + str(self.lista).replace("[", "").replace("]", "") + ")"
        else:
            return self.calcular(n)

fib = Fibonacci()
print(fib.calcular(10))  



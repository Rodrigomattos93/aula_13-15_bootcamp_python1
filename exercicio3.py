#Questão 3 - Recursividade (Médio)
#Implemente uma função recursiva chamada soma_digitos(n), 
# que recebe um número inteiro positivo n e retorna a soma dos seus dígitos.

def soma_digitos(numero_inteiro: int) -> int:
    numero_inteiro = str(numero_inteiro)

    if len(numero_inteiro) == 0:
        return 0
    else:
        return int(numero_inteiro[0]) + soma_digitos(numero_inteiro[1:])

print(soma_digitos(999))


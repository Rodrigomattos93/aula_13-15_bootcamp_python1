#Questão 2 - Classes Abstratas (Médio)
#Crie uma classe abstrata FormaGeometrica com um método abstrato calcular_area(). 
# Em seguida, crie duas subclasses, Circulo e Retangulo, que implementam o método para calcular 
# a área de acordo com suas fórmulas matemáticas.

from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio: float) -> None:
        self.raio = raio
    
    def calcular_area(self) -> float:
        return math.pi * self.raio**2 

class Retangulo(FormaGeometrica):
    def __init__(self, aresta_maior: float, aresta_menor: float):
        self.aresta_maior = aresta_maior
        self.aresta_menor = aresta_menor
    
    def calcular_area(self) -> float:
        return self.aresta_menor * self.aresta_maior

circulo = Circulo(2)
retangulo = Retangulo(2, 3)

print(circulo.calcular_area())
print(retangulo.calcular_area())

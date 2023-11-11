
#Classe Bola: Crie uma classe que modele uma bola:

#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def __str__(self):
        return f'a Cor da bola é {self.cor}, sua circunferencia é {self.circunferencia} e ela é feita de {self.material}'

b1 = bola('vermelho', 2, 'plastico')
print(b1)

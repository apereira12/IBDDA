#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número.
# E no final, retorne também a quantidade de tentativas necessárias.

import random

num = int(input('Favor informar o Número de 1 a 10: '))
tentativa = 1
def dados(tentativa,num):
    select = random.randrange(1, 11)

    while num != select:
        print('Você errou, continue tentando')
        num = int(input('Escolha outro Número de 1 a 10: '))
        tentativa +=1

    print(f'Parabéns você acertou precisou de {tentativa}')

dados(tentativa,num)

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
# perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

import random as rd

def jogos():

    qtdJogos= int(input('Favor informar o número de jogos'))

    listas = [rd.choices(range(1, 61), k=6) for i in range(qtdJogos)]
    print(listas)



jogos()
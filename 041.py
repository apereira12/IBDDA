#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores



def calculo():
    x = int(input('Favor informar o valor: '))
    maior = x
    menor = x
    Ntermos = 1
    continuar = ''

    while continuar != "N":
        y = int(input('Favor informar o valor: '))
        continuar = input('Você deseja continuar? S/N ').upper()
        if y > maior:
            maior = y
        if y < menor:
            menor = y
        Ntermos +=1
        x += y
    return f'a soma é {x}, a média é {x/Ntermos},o menor número é {menor}, o maior número é {maior}'

print(calculo())








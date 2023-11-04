#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

'''Qual é o total gasto na compra
Quantos produtos custam mais de R$1000,00
Qual é o produto mais barato'''



def programa():
   dicio = {}
   while True:
       produto = input('Favor informar o item: ')
       valor = float(input('Favor informar o valor do item: '))
       dicio[produto] = valor
       escolha = input('Você deseja continuar? s/n: ').upper()
       if escolha == "N":
           print('Você finalizou sua lista')
           break
   return dicio

dicio = programa()
print(dicio.items())









